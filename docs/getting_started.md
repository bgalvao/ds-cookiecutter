# Getting Started

## Installation

1. Install Mamba
    - Installing from the [miniforge distribution](https://github.com/conda-forge/miniforge#mambaforge) is recommended if you do not have `conda`
    - Otherwise`conda install -c conda-forge mamba`.
2. Install cookiecutter: `mamba install cookiecutter -y`
    - Managing your installations in separate environments is highly recommended.
3. Generate the project structure: `cookiecutter gh:bgalvao/ds-cookiecutter`
4. Install the data science stack: `mamba create --name cookiecake --file dev.txt`


## Start Jupyter Lab

If you have not changed the project name, then `./cookiecake` is the path where the project was generated. Adapt accordingly:

```shell
cd cookiecake
mamba activate cookiecake  # activate conda env
jupyter lab  # start jupyter lab
```

Now you are ready to follow the Usage docs. :smile:
