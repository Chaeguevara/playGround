from zenml import pipeline
from steps.clean_data import clean_df
from steps.ingest_data import ingest_df
from steps.model_train import train_model
from steps.evaluation import evaluate_model


# cache를 사용하면 모델이 변환되지 않았다면 그대로 사용 가능함 --> memory efficient?
@pipeline(enable_cache=True)
def train_pipeline(data_path: str):
    df = ingest_df(data_path)
    clean_df(df)
    train_model(df)
    evaluate_model(df)
