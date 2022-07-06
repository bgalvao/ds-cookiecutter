# ds-cookiecutter
A cookiecutter for data science projects with MLOps capabilities using an opinionated stack:

- [MLFlow](https://mlflow.org) for experiment tracking 👩🏽‍🔬📑 and easy model server building. 👨🏼‍🔧
- [Prefect 2.0](https://orion-docs.prefect.io/) for ~~work~~dataflow orchestration. 🔢🔀
- Testing
    - [Deepchecks](https://deepchecks.com) for data and model validation. 🧪
    - [pytest](https://docs.pytest.org/en/7.1.x/) to run Deepchecks in your codebase. ✅
- Iterative tools
    - [DVC](https://dvc.org) for data and model versioning and cached experiment pipelines. 🎛️
    - [MLEM](https://mlem.ai/) as an alternative tool for model deployment. 😺
- [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html) for data exploration and literate programming. 📚
- [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) as the package manager. 🐍🛠️📦

Inspired by [Cookiecutter Modern Data Science](https://github.com/crmne/cookiecutter-modern-datascience).

## Install

1. Install [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) dependency so that the post-gen hook runs.
2. Install cookiecutter.
3. `cookicutter https://github.com/kintsugi-mlops/ds-cookiecutter`


## Roadmap:

- [ ] write tests.
- [ ] write GitHub Actions.
- [ ] write GitLab CI/CD (`./gitlab-ci.yml`).
- [ ] consider adding Great Expectations.
