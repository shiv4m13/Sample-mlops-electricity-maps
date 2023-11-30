import pickle
from pathlib import Path
import pandas as pd

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




def run():
   model = load_model()
   features = load_features()
   preprocessor = load_preprocessor()

   # print(features)
   X, _ = preprocessor.transform(features)

   # print(X.values)
   prediction = model.predict(X.values)
   print(prediction)




if __name__ == "__main__":
   run()
