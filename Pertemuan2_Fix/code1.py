# Library
import pandas as pd  #Untok olah data Excel, CSV
import numpy as np #Sama saja dengan pandas namun versinya lebih sederhana
import sqlalchemy as db #Ini untuk SQL
import matplotlib.pyplot as plt #Ini Untuk Plot gambar
import seaborn as sns #Ini untuk plot gambar juga
import io
import base64

def get_matplotlib_plot():
  # Database
  database = db.create_engine("sqlite:///data_hujan.sqlite")
  conn = database.connect()


  #Ambil CSV
  data_mentah = pd.read_csv("data_gabungan_final.csv")


  #Ambil data CH
  data_curah_hujan =data_mentah.groupby("Wilayah") # Ambil Wilayah dulu
  data_curah_hujan_avg = data_curah_hujan.agg(
    rata_rata = ("CH","mean")
  )
  data_curah_hujan_avg_fix = data_curah_hujan_avg.reset_index()


  #Plot_gambar

  plt.style.use('dark_background')
  sns.lineplot(
    data= data_curah_hujan_avg_fix,
    x = "Wilayah",
    y = "rata_rata",
    markers="0",
    color = "red"
  )
  plt.title("Rata Rata CH tiap Wilayah", fontsize = "20", fontweight = "bold")
  plt.xlabel("Wilayah",fontweight = "bold")
  plt.ylabel("Rata - Rata",fontweight = "bold")
  img = io.BytesIO()
  plt.savefig(img , format='png')
  img.seek(0)
  plot_url = base64.b64encode(img.getvalue()).decode()
  plt.close()



  response_data = {
    "status": "berhasil",
    "pesan" : "Grafik Telah berhasil !",
    "gambar_base64" : plot_url

  }

  return response_data


