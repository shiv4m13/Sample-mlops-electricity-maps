print("#############################")
print("Starting")
print("#############################")
try:
   from fastapi import FastAPI, HTTPException, Body
   print("Starting1")
   import pandas as pd
   print("Starting2")
   import json
   print("Startin3")
   import pickle
   print("Startin4")
   import traceback
   print("Startin4")
   print("Pandas done")
   from pathlib import Path
   print("Pandas done23")
   from typing import Any, Dict
   print("Pandas done2")
   from electricitymap.forecasting.training.preprocessors import LassoPreprocessor
   print("ELectricitymap Done")
except Exception as e:
   print("Starting6")
BASE_PATH = Path(
   "."
)
print("#########################")
print(BASE_PATH)
print("#########model startin loadding################")

def load_model():
   print("################load_model inside()###################")
   try:
      with open(BASE_PATH / "artifacts" / "model" / "model.pkl", "rb") as f:
          model = pickle.load(f)
      return model
   except Exception as e:
      print("########### Error load_model() ##################")
      print(e)
      print("#############################")
      return None
      
print("#########passs model startin loadding################")

def load_preprocessor():
   print("################load_preprocessor inside()###################")
   try:
      with open(
          BASE_PATH / "artifacts" / "US-CENT-SWPP_production_wind_preprocessor.pkl", "rb"
      ) as f:
          preprocessor = pickle.load(f)
          return preprocessor
   except Exception as e:
      print("########### Error load_preprocessor() ##################")
      print(e)
      print("#############################")
      return None

print("#########passs3 model startin loadding################")
print("################load_model ()##################")
model = load_model()
print("##############model loaded done ####################")
preprocessor = load_preprocessor()
print("##############preprocessor loaded done ####################")

print("####################### handler ###############")
def handler(event, context):
   try:
      print("############### Event Recived ############")
      body = json.loads(event['body'])
      df = pd.DataFrame(body['data'], columns=body['columns'])
      print("############### df ############")
      X,_ = preprocessor.transform(df)
      print("############### X,_ ############")
      prediction  = model.predict(X.values)
      print("############### pred ############")
      prediction = [x for x in prediction]
      print("############### conver ############")
      result = json.dumps(prediction)
      print("############### sending abck ############")
      return {
           'statusCode': 200,
           'body': result
       }
   except Exception as e:
      print(f"############## Error {e} ########################")
      return {
           'statusCode': 400,
           'body': str(e)
       }
