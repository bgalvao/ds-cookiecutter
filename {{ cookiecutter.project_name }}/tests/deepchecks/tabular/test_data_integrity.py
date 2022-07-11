from deepchecks.tabular import Dataset
from deepchecks.tabular.checks import data_integrity as di


def test_ConflictingLabels(
    dataset: Dataset,
    columns: Union[Hashable, List[Hashable], None] = None,
    ignore_columns: Union[Hashable, List[Hashable], None] = None,
):
    check = di.ConflictingLabels(columns, ignore_columns)
    # add conditions here
    # check.add_condition(name, condition_func)
    assert check.run(dataset).passed_conditions()


def test_DataDuplicates(
    dataset: Dataset,
    columns: Union[Hashable, List[Hashable], None] = None,
    ignore_columns: Union[Hashable, List[Hashable], None] = None,
):
    check = di.DataDuplicates(columns, ignore_columns)
    # add conditions here
    # check.add_condition(name, condition_func)
    assert check.run(dataset).passed_conditions()


def test_FeatureFeatureCorrelation(dataset: Dataset):
    check = di.FeatureFeatureCorrelation()
    # add conditions here
    # check.add_condition(name, condition_func)
    assert check.run(dataset).passed_conditions()


def test_FeatureLabelCorrelation(dataset: Dataset):
    check = di.FeatureLabelCorrelation()
    # add conditions here
    # check.add_condition(name, condition_func)
    assert check.run(dataset).passed_conditions()


def test_IsSingleValue(dataset: Dataset):
    check = di.IsSingleValue()
    # add conditions here
    # check.add_condition(name, condition_func)
    assert check.run(dataset).passed_conditions()


def test_MixedDataTypes(dataset: Dataset):
    check = di.MixedDataTypes()
    # add conditions here
    # check.add_condition(name, condition_func)
    assert check.run(dataset).passed_conditions()


def test_MixedNulls(dataset: Dataset):
    check = di.MixedNulls()
    # add conditions here
    # check.add_condition(name, condition_func)
    assert check.run(dataset).passed_conditions()


def test_OutlierSampleDetection(dataset: Dataset):
    check = di.OutlierSampleDetection()
    # add conditions here
    # check.add_condition(name, condition_func)
    assert check.run(dataset).passed_conditions()


def test_SpecialCharacters(dataset: Dataset):
    check = di.SpecialCharacters()
    # add conditions here
    # check.add_condition(name, condition_func)
    assert check.run(dataset).passed_conditions()


def test_StringLengthOutOfBounds(dataset: Dataset):
    check = di.StringLengthOutOfBounds()
    # add conditions here
    # check.add_condition(name, condition_func)
    assert check.run(dataset).passed_conditions()


def test_StringMismatch(dataset: Dataset):
    check = di.StringMismatch()
    # add conditions here
    # check.add_condition(name, condition_func)
    assert check.run(dataset).passed_conditions()
