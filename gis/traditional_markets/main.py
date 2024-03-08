from configparser import RawConfigParser
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import os
import requests
import dotenv
import numpy as np

dotenv.load_dotenv()
SGIS_SERVICE_ID = os.getenv("SGIS_SERVICE_ID")
SGIS_SECRET_KEY= os.getenv("SGIS_SECRET_KEY")


def get_html_from_url(i=1,i_end=1400):
    """Get html from traditional market webpage

    Yields:
        _type_: _description_
    """
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    for k in range(i,i_end):
        url = f" https://www.sbiz.or.kr/sijangtong/nation/onnuri/pop/onnuriShopListKeyPopupAjax.do?cpage={k}&mkt_cd=&shop_table=SJTT.MKT_ELE_SHOP&deal_item=&shop_nm=&county_cd=&city_cd=02&txtParam=&txtKey=A.MARKET_NAME" 
        driver.get(url)
        html = driver.page_source
        yield html
    driver.quit()

def parser_traditional_market_html(html)->list:
    """HTML 안에 있는 table을 꺼내 데이터로 정제합니다.

    Args:
        html (_type_): _description_

    Returns:
        list: table에 존재하는 각 row를 list형태로 내보냅니다.
    """
    cnts = []
    j = 1
    for i,item in enumerate(html):
        soup = BeautifulSoup(item,"html.parser")
        table = soup.find("table")
        trs = table.find_all("tr")
        for tr in trs[j:]:
            data = tr.find_all('td')
            data = [ele.get_text() for ele in data]
            cnts.append(data)
            if i == 0:
                j =2
    return cnts


def request_to_SGIS():
    consumer_key = str(SGIS_SERVICE_ID)
    consumer_secret = str(SGIS_SECRET_KEY)
    base_url = "https://sgisapi.kostat.go.kr/OpenAPI3/auth/authentication.json"
    post_data ={"consumer_key":consumer_key, "consumer_secret":consumer_secret}
    r = requests.get(base_url,post_data)
    print(r)
    return r.json()["result"]


if __name__ =="__main__":
    html = get_html_from_url(i_end=5)
    contents = parser_traditional_market_html(html)
    raw_contents = pd.DataFrame(contents[1:],columns=contents[0])
    raw_contents = raw_contents.dropna()
    print(raw_contents)
    SGIS_access_token = request_to_SGIS()["accessToken"]