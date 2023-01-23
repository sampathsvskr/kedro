"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from sample_project.pipelines import feature_engineering as fe
from sample_project.pipelines import model_training as mt

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """

    fe_pipeline = fe.create_pipeline()
    model_training = mt.create_pipeline()
    
    
    return {
        "fe_pipeline" : fe_pipeline,
        "model_training": model_training,
        "__default__" : fe_pipeline + model_training
    }
