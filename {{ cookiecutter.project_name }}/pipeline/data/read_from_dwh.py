from dask.dataframe import read_sql_query
import dask
import pandas as pd
from prefect import task, flow
from os.path import join


@task(tags=["data", "write"], retries=2)
def write_dataframe_to_disk(
    df: dask.dataframe | pd.DataFrame,
    file_dir: str = "data/0_source/source_data",
    file_format: str = ".csv",
) -> None:
    file_formats = [".csv", ".parquet"]
    if file_format not in accepted_file_formats:
        raise ValueError(
            f"Expected file format has to be one of the following: \n{file_formats}"
        )
    if file_format is ".csv":
        df.to_csv(file_dir, "data.csv")
    if file_format is ".parquet":
        df.to_parquet(file_dir, "data.parquet")


@task(tags=["data", "read"], retries=3, retry_delay_seconds=5)
def read_dataframe_from_sql_db(
    sql_query: str,
    index_col: str,
    dialect: str = "postgres",
    driver: str = "asyncpg",
    server: str = "sqlserver.example.net",
    user: str = "john_doe",
    password: str = "do not write this in plain text",
    db_name: str = "johndoesdb",
    port: int = None,
) -> dask.dataframe | pd.DataFrame:

    connection_string = (
        f"{dialect}+{driver}://{user}:{password}@{server}:{port}/{db_name}"
        if port is not None
        else f"{dialect}+{driver}://{user}:{password}@{server}/{db_name}"
    )
    df = read_sql_query(sql, connection_string, index_col)

    return df


@flow(name="Source dataset")
def read_dataframe_from_source(sql_query: str):
    read_dataframe_from_sql_db(sql_query)


if __name__ == "__main__":
    sql_query = ""
    if len(sql_query) == 0:
        raise NotImplementedError("SQL query is not written")
    read_dataframe_from_sql_db(sql_query, write_to_disk=True)
