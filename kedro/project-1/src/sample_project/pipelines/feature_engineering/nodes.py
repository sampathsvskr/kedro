"""
This is a boilerplate pipeline 'fetaure_engineering'
generated using Kedro 0.18.4
"""
import pandas as pd
from typing import List
from sklearn.model_selection import train_test_split


def get_fetaures_and_target(data : pd.DataFrame, target_col : str) -> List[pd.DataFrame]:
    ''' Node to get the data and seperate features and target column '''
    
    X,y = data.drop(columns= [target_col]), data[target_col]    
    return data,X,y


def split_data(X : pd.DataFrame, y : pd.DataFrame , params : dict):
    ''' split the data for training and testing'''   
    X_train,X_test,y_train,y_test = train_test_split(X,y, test_size= params["split_ratio"] , random_state= params["random_state"])
    return dict( train_x = X_train, train_y = y_train , test_x = X_test, test_y = y_test )
    
