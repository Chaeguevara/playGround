import logging
import pandas as pd
from zenml import step


class IngestData:
    """ path로 부터 데이터를 읽어옴
    Ingesting the data from the data_path
    
    """
    def __init__(self, data_path: str):
        self.data_path = data_path

    def get_data(self):
        logging.info(f"Ingesting data from {self.data_path}")
        return pd.read_csv((self.data_path))
        
@step
def ingest_df(data_path: str) -> pd.DataFrame:
    """ 데이터 경로로 부터 데이터를 읽어 처리를 한다.
    Ingesting the data from the data path.

    Args:
        test: lblah
    """
    try:
        ingest_data = IngestData(data_path)
        df = ingest_data.get_data()
        return df
    
    except Exception as e:
        logging.error(f"Error while ingesting data: {e}")
        return e



