
Welcome to the documentation of Cookiecake![^1] - an opinionated Data Science Cookiecutter. Featuring:

[^1]: The [best cake](https://www.196flavors.com/portugal-bolo-de-bolacha/) there is in the world.

## A modern and open-source data science stack

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

None of these tools lock you down to any vendor[^2] and are entirely self-hostable where applicable.

[^2]: but some may offer their own hosted solution.

Inspired by [Cookiecutter Modern Data Science](https://github.com/crmne/cookiecutter-modern-datascience) and [OpenMLOps](https://github.com/datarevenue-berlin/openmlops).


## What is this project

This is a cookiecutter to generate a project template for you to structure your data science work using best practices and modern tooling.

## What this project is not

This is not:

- an ETL template - your data sources are assumed to be consolidated in a data warehouse / lake.
- an Infrastructure as Code (IaC) source: you will need to set up your infrastructure and look into how to connect the code of this template to your infrastructure yourself. [OpenMLOps](https://github.com/datarevenue-berlin/openmlops), for instance, is using Terraform for spinning up their solution in AWS.



