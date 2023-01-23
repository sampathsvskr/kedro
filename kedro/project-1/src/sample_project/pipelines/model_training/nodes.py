"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 0.18.4
"""
import pandas as pd 
import numpy as np

def train_model(x_train : pd.DataFrame, y_train : pd.DataFrame):
    '''Node to create the model'''
    from sklearn.linear_model import LogisticRegression
    model=LogisticRegression()
    model.fit(x_train,y_train)    
    return model

def get_predictions(model , x_test : pd.DataFrame) -> np.ndarray:
    '''Node to predict'''
    y_pred=model.predict(x_test)    
    return y_pred

def print_accuracy(y_test : np.ndarray,y_pred : np.ndarray):
    '''Node for printing accuracy'''
    from sklearn.metrics import accuracy_score
    
    accuracy=accuracy_score(y_test,y_pred)*100
    print("Accuracy of the model is {:.2f}".format(accuracy))

