"""
This is a boilerplate pipeline 'fetaure_engineering'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import get_target_classes , encode_categorical_columns , split_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([

        node(
            get_target_classes ,
            inputs = ["raw_data","params:target_col"],
            outputs = "classes",
            name =  "get_classes"      
         ),

         node(
            encode_categorical_columns,
            inputs= {"data":"raw_data","target_col":"params:target_col"},
            outputs = "encoded_data",
            name = "encoding_categorical_columns"
         ),

         node(
            split_data,
            inputs= ["encoded_data", "classes", "parameters" ],
            outputs = dict( train_x = "train_x", train_y = "train_y" , test_x = "test_x" , test_y = "test_y")
         )
    ])
