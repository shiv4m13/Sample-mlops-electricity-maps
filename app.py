from fastapi import FastAPI, HTTPException, Body

import json
import pickle
import traceback
import pandas as pd
from pathlib import Path
from typing import Any, Dict
from electricitymap.forecasting.training.preprocessors import LassoPreprocessor

BASE_PATH = Path(
   "."
)

def load_model():
   with open(BASE_PATH / "artifacts" / "model" / "model.pkl", "rb") as f:
       model = pickle.load(f)
   return model

def load_features() -> pd.DataFrame:
   df = pd.read_parquet(BASE_PATH / "features.parquet")
   return df

def load_inference_features() -> pd.DataFrame:
   df = pd.read_parquet(BASE_PATH / "features_inference.parquet")
   return df


def load_preprocessor():
   with open(
       BASE_PATH / "artifacts" / "US-CENT-SWPP_production_wind_preprocessor.pkl", "rb"
   ) as f:
       preprocessor = pickle.load(f)
   return preprocessor


model = load_model()
preprocessor = load_preprocessor()

def handler(event, context):
    try:
        df = pd.DataFrame(event['data']['data'], columns=event['data']['columns'])
        X,_ = preprocessor.transform(df)
        prediction  = model.predict(X.values)
        prediction = [x for x in prediction]
        result = json.dumps(prediction)
        return result
    except Exception as e:
        print(traceback.format_exc())
        return str(traceback.format_exc())
