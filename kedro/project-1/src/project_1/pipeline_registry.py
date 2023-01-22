"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from project_1.pipelines import feature_engineering as fe

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """

    fe_pipeline = fe.create_pipeline()
    
    
    return {
        "fe_pipeline" : fe_pipeline,
        "__default__" : fe_pipeline
    }
