from typing import Hashable, List, Union

import pandas as pd
import pytest
from deepchecks.tabular import Dataset
from deepchecks.tabular.checks import train_test_validation as ttv


def test_CategoryMismatchTrainTest(
    train_dataset: Dataset,
    test_dataset: Dataset,
    columns: Union[Hashable, List[Hashable], None] = None,
    ignore_columns: Union[Hashable, List[Hashable], None] = None,
):
    check = ttv.CategoryMismatchTrainTest(
        columns, ignore_columns, max_features_to_show, max_features_to_show
    )
    assert check.run(train_dataset, test_dataset).passed_conditions()


def test_DatasetsSizeComparison(train_dataset: Dataset, test_dataset: Dataset):
    check = ttv.DatasetsSizeComparison()
    check.add_condition_test_train_size_ratio_greater_than(0.2)
    assert check.run(train_dataset, test_dataset).passed_conditions()


def test_DateTrainTestLeakageDuplicates(train_dataset: Dataset, test_dataset: Dataset):
    check = ttv.DateTrainTestLeakageDuplicates()
    check.add_condition_leakage_ratio_less_or_equal(0.0)
    assert check.run(train_dataset, test_dataset).passed_conditions()


def test_DateTrainTestLeakageOverlap(train_dataset: Dataset, test_dataset: Dataset):
    check = ttv.DateTrainTestLeakageOverlap()
    assert check.run(train_dataset, test_dataset).passed_conditions()


def test_DominantFrequencyChange(train_dataset: Dataset, test_dataset: Dataset):
    check = ttv.DominantFrequencyChange()
    assert check.run(train_dataset, test_dataset).passed_conditions()


def test_FeatureLabelCorrelationChange(train_dataset: Dataset, test_dataset: Dataset):
    check = ttv.FeatureLabelCorrelationChange()
    assert check.run(train_dataset, test_dataset).passed_conditions()


def test_IdentifierLeakage(train_dataset: Dataset):
    check = ttv.IdentifierLeakage()
    assert check.run(train_dataset).passed_conditions()


def test_IndexTrainTestLeakage(train_dataset: Dataset, test_dataset: Dataset):
    check = ttv.IndexTrainTestLeakage()
    assert check.run(train_dataset, test_dataset).passed_conditions()


def test_NewLabelTrainTest(train_dataset: Dataset, test_dataset: Dataset):
    check = ttv.NewLabelTrainTest()
    assert check.run(train_dataset, test_dataset).passed_conditions()


def test_StringMismatchComparison(
    train_dataset: Dataset,
    test_dataset: Dataset,
    columns: Union[Hashable, List[Hashable], None] = None,
    ignore_columns: Union[Hashable, List[Hashable], None] = None,
):
    check = ttv.StringMismatchComparison(columns, ignore_columns)
    assert check.run(train_dataset, test_dataset).passed_conditions()


def test_TrainTestFeatureDrift(
    train_dataset: Dataset,
    test_dataset: Dataset,
    columns: Union[Hashable, List[Hashable], None] = None,
    ignore_columns: Union[Hashable, List[Hashable], None] = None,
):
    check = ttv.TrainTestFeatureDrift(columns, ignore_columns)
    assert check.run(train_dataset, test_dataset).passed_conditions()


def test_TrainTestLabelDrift(train_dataset: Dataset, test_dataset: Dataset):
    check = ttv.TrainTestLabelDrift()
    assert check.run(train_dataset, test_dataset).passed_conditions()


def test_TrainTestSamplesMix(
    train_dataset: Dataset,
    test_dataset: Dataset,
    margin_quantile_filter: float = 0.025,
    max_num_categories_for_drift: int = 10,
):
    check = ttv.TrainTestSamplesMix(
        margin_quantile_filter, max_num_categories_for_drift
    )
    assert check.run(train_dataset, test_dataset).passed_conditions()


def test_WholeDatasetDrift(train_dataset: Dataset, test_dataset: Dataset):
    check = ttv.WholeDatasetDrift()
    assert check.run(train_dataset, test_dataset).passed_conditions()
