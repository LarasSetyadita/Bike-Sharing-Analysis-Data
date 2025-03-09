import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi untuk menampilkan heatmap
def tampilkan_heatmap():
    # Load data
    df = pd.read_csv('./dashboard/u_hour_df.csv')  # Ganti dengan nama file dataset

    correlation = df.corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax)

    ax.set_title("Heatmap Korelasi Semua Variabel", fontsize=14)
    st.pyplot(fig)


def main():
    st.title("📊 Heatmap Korelasi Data Sepeda")

    # Tampilkan heatmap
    tampilkan_heatmap()
    st.subheader("Keterangan: ")
    st.write('berdasarkan heatmap yang telah dibuat, korelasi tertinggi antara kolom hour,dan year, serta menengah pada kolom season. Korelasi yang terjadi antara permintaan sewa sepeda dengan hari terbilang sangat kecil yaitu 0.03 sehingga bisa dikatakan bahwa tidak terdapat korelasi yang terjadi antara hari dan jumlah permintaan sewa sepeda.')

if __name__ == '__main__':
    main()
