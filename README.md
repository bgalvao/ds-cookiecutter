# ds-cookiecutter
A cookiecutter for data science projects with MLOps capabilities using an opinionated stack:

- [MLFlow](https://mlflow.org) for experiment tracking 👩🏽‍🔬📑 and easy model server building. 👨🏼‍🔧
- [Prefect 2.0](https://orion-docs.prefect.io/) for data workflow orchestration. 🔢🔀🎻
- Testing
    - [Deepchecks](https://deepchecks.com) for data and model validation. 🧪
    - [pytest](https://docs.pytest.org/en/7.1.x/) to run Deepchecks in your codebase. ✅
- Iterative tools
    - [DVC](https://dvc.org) for data and model versioning and cached experiment pipelines. 🎛️
    - [MLEM](https://mlem.ai/) as an alternative tool for model deployment. 😺
    - [DVC](https://dvc.org) for data and model versioning and cached experiment pipelines 🎛️  - ensuring **_experiment reproducibility_**.
    - [MLEM](https://mlem.ai/) as an alternative tool for model deployment.😺
- [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html) for data exploration and literate programming. 📚
- [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) as the package manager. 🐍🛠️📦

Inspired by [Cookiecutter Modern Data Science](https://github.com/crmne/cookiecutter-modern-datascience).

<<<<<<< Updated upstream
## Install

1. Install [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) dependency so that the post-gen hook runs.
2. Install cookiecutter.
3. `cookicutter https://github.com/kintsugi-mlops/ds-cookiecutter`


## Roadmap:

- [ ] write tests.
- [ ] write GitHub Actions.
- [ ] write GitLab CI/CD (`./gitlab-ci.yml`).
- [ ] consider adding Great Expectations.

## project structure

```
.
├── data
│  ├── 0_raw          # data queried from the DWH and sources
│  ├── 1_processed    # feature transformations and filtering
│  └── 2_train_test   # a train test split
├── models            # a directory to save models and metrics to
├── notebooks         # literate programming for EDA and testing code
├── pipeline          # Prefect annotated tasks to use for workflow deployment and in notebooks
│  ├── data           # all operations regarding ./data
│  ├── evaluate       # evaluations after training the model with metrics and reports, writes to ./models
│  └── model          # trains and writes a model to ./models
├── references        # explanatory materials
└── tests			  # tests for running in the CI/CD pipeline and locally
   └── deepchecks
      └── tabular     # boilerplate pytest-deepchecks to be customized
```



## Roadmap:

- [ ] write tests
  - [x] wrote cookiecutter of Deepchecks ([bgalvao/mlops-pytests](https://github.com/bgalvao/mlops-pytests))
  - [ ] consider adding Great Expectations.
- [ ] write GitLab CI/CD (`./gitlab-ci.yml`).
  - [ ] Nice-to-have: write GitHub Actions.
