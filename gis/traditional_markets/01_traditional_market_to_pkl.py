from selenium import webdriver
import pandas as pd

from bs4 import BeautifulSoup

def get_html_from_url():
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    i = 1
    i_end = 1400
    for k in range(i,i_end):
        url = f" https://www.sbiz.or.kr/sijangtong/nation/onnuri/pop/onnuriShopListKeyPopupAjax.do?cpage={k}&mkt_cd=&shop_table=SJTT.MKT_ELE_SHOP&deal_item=&shop_nm=&county_cd=&city_cd=02&txtParam=&txtKey=A.MARKET_NAME" 
        driver.get(url)
        html = driver.page_source
        yield html
    driver.quit()

html = get_html_from_url()


headings = None
cnts = []
j = 1
for i,item in enumerate(html):
    print(i)
    soup = BeautifulSoup(item)
    table = soup.find("table")
    trs = table.find_all("tr")
    for tr in trs[j:]:
        data = tr.find_all('td')
        data = [ele.get_text() for ele in data]
        cnts.append(data)
        if i == 0:
            j =2
print(cnts)
print(len(cnts))
df = pd.DataFrame(cnts)
print(df)
df.to_pickle("./traditonal.pkl")
