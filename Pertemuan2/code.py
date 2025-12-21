import pandas as pd
import numpy as np
import sqlalchemy as db
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

def get_matplotlib_plot():
    database = dn.create_engine("sqlite:///data_hujan.sqlite")
    conn = database.connect()

    data_mentah = pd.read_csv("data_gabungan_final.csv")

    data_curah_hujan = data_mentah.groupby("Wilayah")
    data_curah_hujan_avg = data_curah_hujan.agg(
        rata_rata = ("CH", "mean")
    )
    data_curah_hujan_avg_fix = data_curah_hujan_avg

    plt.style.use('dark_background')
    sns.lineplot(
        data = data_curah_hujan_avg_fix,
        x = "Wilayah"
        y = "rata-rata"
        markers = "0"
        color = "red"
    )

    plt.title("Rata Rata CH tiap Wilayah", fontweight = "bold")
    plt.xlabel("Wilayah", fontweight = "bold")
    plt.ylabel("Rata - Rata", fontweight = "bold")
    img = io.BytesIO
    plt.savefig("output.png")
    img.seek(0)
    plt.close()