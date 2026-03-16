from sqlalchemy import create_engine

def connect_db():

    engine = create_engine(
        "sqlite:///students.db",
        echo=False
    )

    return engine