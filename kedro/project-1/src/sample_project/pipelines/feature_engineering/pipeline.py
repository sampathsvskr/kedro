"""
This is a boilerplate pipeline 'fetaure_engineering'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import get_fetaures_and_target , split_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([

         node(
            get_fetaures_and_target,
            inputs= ["raw_data","params:target_col"],
            outputs = ["save_data","fetaures_df","target_df"], #fetaures_df and target_df will be in memory as dataset is not defined in catalog
            name = "encoding_categorical_columns"
         ),

         node(
            split_data,
            inputs= {"X":"fetaures_df","y":"target_df","params":"parameters"},
            outputs = dict( train_x = "train_x", train_y = "train_y" , test_x = "test_x" , test_y = "test_y")
         )
    ])
