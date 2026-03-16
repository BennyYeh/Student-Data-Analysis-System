import pandas as pd
from src.database.db_connection import connect_db

def load_data():

    engine = connect_db()

    query = "SELECT * FROM students"

    df = pd.read_sql(query,engine)

    return df


def gender_average(df):

    return df.groupby("gender")["score"].mean()


def department_average(df):

    return df.groupby("department")["score"].mean()


def score_statistics(df):

    return {

        "count":len(df),
        "max":df["score"].max(),
        "min":df["score"].min(),
        "mean":df["score"].mean()

    }