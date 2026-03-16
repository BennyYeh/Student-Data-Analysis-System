import pandas as pd
from src.database.db_connection import connect_db

def load_csv_to_db():

    engine = connect_db()

    df = pd.read_csv("data/student_data.csv", encoding="cp950")

    df.to_sql(
        name="students",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("資料匯入成功")