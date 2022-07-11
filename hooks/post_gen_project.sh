#!/usr/bin/bash
set -e
mamba create -n "{{ cookiecutter.env_name }}"
source $HOME/.bashrc
mamba init bash
mamba activate "{{ cookiecutter.env_name }}"
mamba install --file "environment.txt"
mamba install pip -y
pip install "prefect>=2.0b" mlem

echo "Enjoy your MLOps-enabled data science project! 🍜"
