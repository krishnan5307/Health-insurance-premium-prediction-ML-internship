import os
import sys

from insurance.exception import InsuranceException
from insurance.util.util import load_object

import pandas as pd
import numpy as np


class InsuranceData: 
        

    def __init__(self,

                  age: int,
                  children: int,
                  bmi: float,                  
                  sex: str,
                  smoker: str,
                  region: str,
                  expenses: float =None,
                  ):           
        try:
            self.age = age
            self.children = children
            self.bmi = bmi
            self.sex = sex
            self.smoker = smoker
            self.region = region
            self.expenses = expenses
        except Exception as e:
            raise InsuranceException(e, sys) from e

    def get_insurance_input_data_frame(self):

        try:
            insuarnce_input_dict = self.get_insurance_data_as_dict()
            df= pd.DataFrame(insuarnce_input_dict)
            return df

        except Exception as e:
            raise InsuranceException(e, sys) from e

    def get_insurance_data_as_dict(self):
        try:
            input_data = {
                "age": [self.age],
                "children": [self.children],
                "bmi": [self.bmi],
                "sex": [self.sex],
                "smoker": [self.smoker],
                "region": [self.region],
                             }
            return input_data
        except Exception as e:
            raise InsuranceException(e, sys)


class InsurancePredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise InsuranceException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir))) # function is int() and iterable is list of dir
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise InsuranceException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()      ## from saved model folder
            model = load_object(file_path=model_path)
            expenses = model.predict(X)
            return expenses
        except Exception as e:
            raise InsuranceException(e, sys) from e