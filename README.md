# ds-cookiecutter
A cookiecutter for data science projects with MLOps capabilities using an opinionated stack:

- [MLFlow](https://mlflow.org) for experiment tracking 👩🏽‍🔬📑 and easy model server building. 👨🏼‍🔧
- [Prefect 2.0](https://orion-docs.prefect.io/) for ~~work~~dataflow orchestration. 🔢🔀
- Testing
    - [Deepchecks](https://deepchecks.com) for data and model validation. 🧪
    - [pytest](https://docs.pytest.org/en/7.1.x/) to run Deepchecks in your codebase. ✅
- Iterative tools
    - [DVC](https://dvc.org) for data and model versioning and cached experiment pipelines. 🎛️
    - [MLEM](https://mlem.ai/) as an alternative tool for model deployment.😺
- [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html) for data exploration and literate programming. 📚

Roadmap:

- [ ] write tests.
- [ ] write GitHub Actions.
- [ ] write GitLab CI/CD (`./gitlab-ci.yml`).
- [ ] consider adding Great Expectations.


Inspired by [Cookiecutter Modern Data Science
](https://github.com/crmne/cookiecutter-modern-datascience).