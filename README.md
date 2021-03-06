# Cookiecake
An opinionated Data Science Cookiecutter. Featuring:

- [MLFlow](https://mlflow.org) for experiment tracking ๐ฉ๐ฝโ๐ฌ๐ and easy model server building. ๐จ๐ผโ๐ง
- [Prefect 2.0](https://orion-docs.prefect.io/) for data workflow orchestration. ๐ข๐๐ป
- Testing
    - [Deepchecks](https://deepchecks.com) for data and model validation. ๐งช
    - [pytest](https://docs.pytest.org/en/7.1.x/) to run Deepchecks in your codebase. โ
- Iterative tools
    - [DVC](https://dvc.org) for data and model versioning and cached experiment pipelines ๐๏ธ  - ensuring **_experiment reproducibility_**.
    - [MLEM](https://mlem.ai/) as an alternative tool for model deployment.๐บ
- [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html) for data exploration and literate programming. ๐
- [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) as the package manager. ๐๐ ๏ธ๐ฆ

Inspired by [Cookiecutter Modern Data Science](https://github.com/crmne/cookiecutter-modern-datascience).

## Install

1. Install [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) dependency so that the post-gen hook runs.
2. Install cookiecutter.
3. `cookiecutter https://github.com/kintsugi-mlops/ds-cookiecutter`


## project structure

```
.
โโโ data
โ  โโโ 0_raw          # data queried from the DWH and sources
โ  โโโ 1_processed    # feature transformations and filtering
โ  โโโ 2_train_test   # a train test split
โโโ models            # a directory to save models and metrics to
โโโ notebooks         # literate programming for EDA and testing code
โโโ pipeline          # Prefect annotated tasks to use for workflow deployment and in notebooks
โ  โโโ data           # all operations regarding ./data
โ  โโโ evaluate       # evaluations after training the model with metrics and reports, writes to ./models
โ  โโโ model          # trains and writes a model to ./models
โโโ references        # explanatory materials
โโโ tests			  # tests for running in the CI/CD pipeline and locally
   โโโ deepchecks
      โโโ tabular     # boilerplate pytest-deepchecks to be customized
```
