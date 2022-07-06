mamba install \
  --file "{{ cookiecutter.project_name }}/environment.txt" \
  -n "{{ cookiecutter.env_name }}"

mamba install -n "{{ cookiecutter.env_name }}" pip -y
mamba activate "{{ cookiecutter.env_name }}"
pip install "prefect>=2.0b" mlem
