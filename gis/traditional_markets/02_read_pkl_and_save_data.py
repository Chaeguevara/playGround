import pandas as pd
import dotenv
import os
import requests
import csv
from datetime import datetime

dotenv.load_dotenv()
SGIS_SERVICE_ID = os.getenv("SGIS_SERVICE_ID")
SGIS_SECRET_KEY= os.getenv("SGIS_SECRET_KEY")

def pre_process_pickle(path:str) -> pd.DataFrame:
    df = pd.read_pickle(path)
    print(df.shape)
    df.dropna(axis=0,inplace=True)
    print(df.shape)
    # delete first row and set as heading
    df.columns = df.iloc[0]
    df = df[1:]
    #df.to_csv("./traditonal.csv")
    return pd.DataFrame(df)

def get_access_key_of_SGIS():
    consumer_key = str(SGIS_SERVICE_ID)
    consumer_secret = str(SGIS_SECRET_KEY)
    base_url = "https://sgisapi.kostat.go.kr/OpenAPI3/auth/authentication.json"
    post_data ={"consumer_key":consumer_key, "consumer_secret":consumer_secret}
    r = requests.get(base_url,post_data)
    print(r)
    return r.json()["result"]

def get_coordinate(row,acc_key):
    base_url = "https://sgisapi.kostat.go.kr/OpenAPI3/addr/geocodewgs84.json"
    data = {"accessToken":str(acc_key),
                 "address":row["주소"]
                 }
    r = requests.get(base_url,data)
    row['lat'] = ''
    row['lng'] = ''
    print(f"{r.status_code=}")
    if r.status_code != 200:
        return row
    data_json = r.json()
    if data_json['errCd'] == 0:
        row["lat"] = data_json['result']['resultdata'][0]['y']
        row["lng"] = data_json['result']['resultdata'][0]['x']
    print(row)
    return row



if __name__ == "__main__":
    df = pre_process_pickle("./traditonal.pkl")
    # test_df = df.iloc[5:12]
    # print(df.head())
    res = get_access_key_of_SGIS()
    access_key = res["accessToken"]
    # test_df = test_df.apply(lambda x: get_coordinate(x,access_key),axis=1)
    # print(test_df)
    row_len = df.shape[0]
    interval = 100 # save evry 100
    end_range = int(row_len / interval)
    with open("./error_idx.csv","w") as err_csv:
        for i in range(275,end_range):
            try:
                cur_df = df[i*interval:interval*(i+1)]
                cur_df = cur_df.apply(lambda x: get_coordinate(x,access_key),axis=1)
                cur_df.to_csv(f"./traditional_w_coordinate_{i*interval}-{interval*(i+1)}.csv")
            except ConnectionError as e:
                print(e)
                err_csv.write(str(i))
            access_key = get_access_key_of_SGIS()["accessToken"]
        print(i)
        i = (i+1)*interval
        try:
            cur_df = df[i:i+interval]
            cur_df = cur_df.apply(lambda x: get_coordinate(x,access_key),axis=1)
            cur_df.to_csv(f"./data/traditional_w_coordinate_{i}-{i+interval}.csv")
        except ConnectionError as e:
            print(e)
            err_csv.write(str(i))
        err_csv.close()

