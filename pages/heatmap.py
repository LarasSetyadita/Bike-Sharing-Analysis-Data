import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi untuk menampilkan heatmap
def tampilkan_heatmap():
    # Load data
    df = pd.read_csv('./data/u_hour_df.csv')  # Ganti dengan nama file dataset

    correlation = df.corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax)

    ax.set_title("Heatmap Korelasi Semua Variabel", fontsize=14)
    st.pyplot(fig)


def main():
    st.title("📊 Heatmap Korelasi Data Sepeda")

    # Tampilkan heatmap
    tampilkan_heatmap()

if __name__ == '__main__':
    main()
