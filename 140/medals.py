import pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def athletes_most_medals(data=data):
    df = pd.read_csv(data)
    gr = df.groupby(by=["Gender", "Athlete"]).count()
    m, w = gr.loc["Men"]["Medal"], gr.loc["Women"]["Medal"]
    return {
        m.idxmax(): m.max(),
        w.idxmax(): w.max()
    }
