from deepchecks.tabular import Dataset
from deepchecks.tabular.checks import model_evaluation as me


def test_BoostingOverfit(
    train_dataset: Dataset,
    test_dataset: Dataset,
    model,
    alternative_scorer: Tuple[str, Union[str, Callable]] = None,
    num_steps: int = 20,
):
    check = me.BoostingOverfit(alternative_scorer, num_steps)
    # add conditions here
    assert check.run(train_dataset, test_dataset, model).passed_conditions()


def test_CalibrationScore(train_dataset: Dataset):
    check = me.CalibrationScore()
    # add conditions here
    assert check.run(train_dataset, model).passed_conditions()


def test_ConfusionMatrixReport(test_dataset: Dataset):
    check = me.ConfusionMatrixReport()
    # add conditions here
    assert check.run(test_dataset, model).passed_conditions()


def test_ModelInferenceTime(test_dataset: Dataset, n_samples):
    check = me.ModelInferenceTime(n_samples)
    # add conditions here
    assert check.run(test_dataset, model).passed_conditions()


def test_RocReport(test_dataset: Dataset, excluded_classes):
    check = me.RocReport()
    # add conditions here
    assert check.run(test_dataset, model).passed_conditions()


def test_ModelErrorAnalysis(train_dataset: Dataset, test_dataset: Dataset):
    # deprecated in 0.8.1
    check = me.ModelErrorAnalysis()
    # add conditions here
    assert check.run(train_dataset, test_dataset, model).passed_conditions()


def test_ConstantModelComparison(train_dataset: Dataset, test_dataset: Dataset):
    check = me.SimpleModelComparison(simple_model_type="constant")
    # add conditions here
    assert check.run(train_dataset, test_dataset, model).passed_conditions()


def test_RandomModelComparison(
    train_dataset: Dataset, test_dataset: Dataset, random_state: int = 42
):
    check = me.SimpleModelComparison(
        simple_model_type="random", random_state=random_state
    )
    # add conditions here
    assert check.run(train_dataset, test_dataset, model).passed_conditions()


def test_TreeModelComparison(
    train_dataset: Dataset, test_dataset: Dataset, random_state: int = 42
):
    check = me.SimpleModelComparison(
        simple_model_type="tree", random_state=random_state
    )
    # add conditions here
    assert check.run(train_dataset, test_dataset, model).passed_conditions()


def test_TrainTestPredictionDrift(
    train_dataset: Dataset,
    test_dataset: Dataset,
    margin_quantile_filter: float = 0.025,
    max_num_categories_for_drift: int = 10,
):
    check = me.TrainTestPredictionDrift(
        margin_quantile_filter=margin_quantile_filter,
        max_num_categories_for_drift=max_num_categories_for_drift,
    )
    # add conditions here
    assert check.run(train_dataset, test_dataset, model).passed_conditions()


def test_UnusedFeatures(
    train_dataset: Dataset,
    test_dataset: Dataset,
    feature_importance_threshold: float = 0.2,
    feature_variance_threshold: float = 0.4,
    random_state: int = 42,
):
    check = me.UnusedFeatures(
        feature_importance_threshold=feature_importance_threshold,
        feature_variance_threshold=feature_variance_threshold,
        random_state=random_state,
    )
    # add conditions here
    assert check.run(train_dataset, test_dataset, model).passed_conditions()
