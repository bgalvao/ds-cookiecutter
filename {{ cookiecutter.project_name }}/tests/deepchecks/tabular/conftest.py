from deepchecks.tabular import Dataset
from pandas import DataFrame

import pytest

deepchecks_dataset_params = {
    "label": None,
    "features": None,
    "cat_features": None,
    "index_name": None,
    "set_index_from_dataframe_index": False,
    "datetime_name": None,
    "set_datetime_from_dataframe_index": False,
    "convert_datetime": True,
    "datetime_args": None,
    "max_categorical_ratio": 0.01,
    "max_categories": None,
    "label_type": None,
}

dataset_pytest_scope = "package"


@pytest.fixture(scope=dataset_pytest_scope)
def train_df() -> DataFrame:
    raise NotImplementedError()


@pytest.fixture(scope=dataset_pytest_scope)
def test_df() -> DataFrame:
    raise NotImplementedError()


@pytest.fixture(scope=dataset_pytest_scope)
def whole_df() -> DataFrame:
    raise NotImplementedError()


@pytest.fixture(scope=dataset_pytest_scope)
def train_dataset(train_df: DataFrame) -> Dataset:
    return Dataset(train_df, **deepchecks_dataset_params)


@pytest.fixture(scope=dataset_pytest_scope)
def test_dataset(test_df: DataFrame) -> Dataset:
    return Dataset(test_dataset, **deepchecks_dataset_params)


@pytest.fixture(scope=dataset_pytest_scope)
def whole_dataset(whole_df: DataFrame) -> Dataset:
    return Dataset(whole_dataset, **deepchecks_dataset_params)


# only test_model_validation.py will need this fixture
@pytest.fixture(scope="module")
def model():
    raise NotImplementedError()
    # assert hasattr(model, 'predict_proba')
