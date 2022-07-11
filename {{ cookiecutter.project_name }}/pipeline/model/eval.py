from prefect import task

from deepchecks.tabular import Dataset
from deepchecks.tabular.suites import full_suite, model_evaluation
from deepchecks.core.suite import SuiteResult

import pandas as pd


@task(name="Evaluate model and data")
def run_evaluation_suite(
    model, train_dataset: Dataset, test_dataset: Dataset
) -> SuiteResult:
    return full_suite(model, train_dataset, test_dataset).run()


@task(name="Save model and data evaluation report")
def save_eval_report(report: SuiteResult):
    report.save_as_html("models/report.html")


if __name__ == "__main__":
    model = read_model("models/model.pkl")
    train_dataset = pd.read_parquet("data/2_train_test/train.parquet").set_index(
        index_col
    )
    test_dataset = pd.read_parquet("data/2_train_test/test.parquet").set_index(
        index_col
    )
    report = run_evaluation_suite(model, train_dataset, test_dataset)
    save_eval_report(report)
