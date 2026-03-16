import pandas as pd
import random

def generate_student_data(n):

    genders = ["男","女"]
    departments = ["CS","MIS","Data","AI"]

    data = []

    for i in range(n):

        name = f"Student{i+1}"
        gender = random.choice(genders)
        age = random.randint(18,24)
        score = random.randint(50,100)
        department = random.choice(departments)

        data.append([name,gender,age,score,department])

    df = pd.DataFrame(
        data,
        columns=["name","gender","age","score","department"]
    )

    df.to_csv("data/student_data.csv",index=False,encoding="cp950")

    return df