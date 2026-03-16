import matplotlib.pyplot as plt

def gender_chart(df):

    df.groupby("gender")["score"].mean().plot(kind="bar")
    plt.title("男女平均")
    plt.show()


def department_chart(df):

    df.groupby("department")["score"].mean().plot(kind="bar")
    plt.title("科系平均")
    plt.show()


def score_distribution(df):

    df["score"].hist(bins=20)
    plt.title("成績分布")
    plt.show()