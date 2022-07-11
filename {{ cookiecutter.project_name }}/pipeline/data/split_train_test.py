"""
Logic for splitting the dataset into train and test sets.
"""

import pandas as pd
import dask
from typing import Tuple, Union

import prefect
from os.path import join


@prefect.task
def load_data(
    filepath: str = "data/1_processed/processed.csv",
) -> Union[pd.DataFrame, dask.dataframe]:
    return pd.read_csv(filepath)


@prefect.task
def train_test_indices(dataset: pd.DataFrame) -> (pd.Index, pd.Index):
    raise NotImplementedError()


@prefect.task
def split_dataset(
    dataset: pd.DataFrame,
    train_idx: pd.Index,
    test_idx: pd.Index,
    saving_dir: str = "data/2_train_test/",
    saving_file_format="csv",
):
    train, test = dataset.loc[pd.Index], dataset.loc[pd.Index]

    file_format = ["csv", "parquet"]
    if file_format not in file_format:
        raise ValueError("Invalid sim type. Expected one of: %s" % sim_types)

    if saving_dir is not None:
        if file_format is "csv":
            train.to_csv(join(saving_dir, "train.csv"))
            test.to_csv(join(saving_dir, "test.csv"))
        if file_format is "parquet":
            train.to_parquet(join(saving_dir, "train.parquet"))
            test.to_parquet(join(saving_dir, "test.parquet"))

    return train, test
