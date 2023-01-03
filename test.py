
#import required modules
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

import joblib
from sklearn.preprocessing import OneHotEncoder

from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor
import time



def preprocess_data(df):
    jet_relevant_data = df.drop(["cycle", "op1", "op2", "op3", "sensor1", "sensor5", "sensor6", "sensor10",
				 "sensor16", "sensor18", "sensor19"], axis=1)
    scaler = joblib.load('scaler_transformation.pkl')
    scaled_features = scaler.transform(jet_relevant_data.drop(['id'], axis=1)) 
    scaled_features = pd.DataFrame(scaled_features, columns=jet_relevant_data.drop(['id'], axis=1).columns)
    
    print(scaled_features.head())
    return scaled_features 



#read test data  
test_data = pd.read_csv(r"D:\AKSHAY\study\python\Project\CMaps\test_FD001.txt", sep = "\s+", header = None)
test_data.columns = ["id","cycle","op1","op2","op3","sensor1","sensor2","sensor3","sensor4","sensor5"
                    ,"sensor6","sensor7","sensor8","sensor9","sensor10","sensor11","sensor12","sensor13"
                    ,"sensor14","sensor15","sensor16","sensor17","sensor18","sensor19"
                    ,"sensor20","sensor21"]
test_data.head()

X_test = preprocess_data(test_data)


#predicting test data on model


test_mod = joblib.load('xbg_best.pkl')

y_pred_test = test_mod.predict(X_test[0:3])

for i in range(len(y_pred_test)):
    print(f'Engine {i+1} work up to {y_pred_test[i]} many iterations')


#print(y_pred_test)





    