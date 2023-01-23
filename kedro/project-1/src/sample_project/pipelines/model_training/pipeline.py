"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import train_model, get_predictions, print_accuracy

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(train_model,
            inputs = ["train_x","train_y"],
            outputs = "save_model",
            name = "training"
        ),
        node(get_predictions,
            inputs = ["save_model","test_x"],
            outputs = "pred_x",
            name = "prediction"
        ),
        node(print_accuracy,
            inputs = ["pred_x","test_y"],
            outputs = None,
            name = "scoring"
        )
    ])
