## install as many prefect dependencies as possible from conda-forge

The command `pip install "prefect>=2.0b"` installs the following dependencies

- `griffe`
- `slack_sdk`
- `boto3`
- `azure_storage_blob`
- `asyncpg`
- `botocore`

which could have been installed by `conda -c conda-forge` or `mamba` in order to avoid [side effects introduced by pip]().

## prefect task and flow decorators' params

**`@task`s**:
- `name`
- `description`
- `tags`
- `version`
- `cache_key_fn`
- `cache_expiration`
- `retries`
- `retry_delay_seconds`

**`@flow`s**:
- `name`
- `version`
- `task_runner`
- `description`
- `timeout_seconds`
- `validate_parameters`
- `retries`
- `retry_delay_seconds`
