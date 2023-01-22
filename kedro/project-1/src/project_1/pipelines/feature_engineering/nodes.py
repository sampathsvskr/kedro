"""
This is a boilerplate pipeline 'fetaure_engineering'
generated using Kedro 0.18.4
"""
import pandas as pd
from typing import List
from sklearn.model_selection import train_test_split

def get_target_classes(data : pd.DataFrame , target_col : str) -> List[str]:
    '''Node for getting classes from the target column of iris dataset'''    
    return data[target_col].unique()


def encode_categorical_columns(data : pd.DataFrame, target_col : str) -> pd.DataFrame:
    ''' Node for encoding categorical columns '''
    df= pd.get_dummies(data, prefix="",prefix_sep="" ,columns= [target_col])    
    return df


def split_data(data : pd.DataFrame, classes : list , params : dict):
    print(params)    
    X,y = data.drop(columns= classes), data[classes]
    X_train,X_test,y_train,y_test = train_test_split(X,y, test_size= params["split_ratio"] , random_state= params["random_state"])

    return dict( train_x = X_train, train_y = y_train , test_x = X_test, test_y = y_test )
    
