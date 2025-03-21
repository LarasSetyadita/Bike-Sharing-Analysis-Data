import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def grafik():
    avg_rentals_day = pd.read_csv('./dashboard/avg_rentals_day.csv')
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=avg_rentals_day, x="day", y="count", hue="year", ax=ax)

    ax.set_title("Rata-rata Penyewaan Sepeda per Hari berdasarkan Tahun")
    ax.set_xlabel("Hari")
    ax.set_ylabel("Rata-rata Jumlah Penyewaan")
    ax.legend(title="Tahun")

    st.pyplot(fig)  # Menampilkan grafik di Streamlit

def main():
    st.title("Rata-rata Sewa Sepeda Harian")

    # Menampilkan grafik
    grafik()
    st.subheader("Keterangan: ")
    st.write('Tren jumlah persewaan sepeda tidak menunjukkan perbedaan yang signifikan terhadap perbedaan hari. Namun terdapat perbedaan yang mencolok antara jumlah sepeda yang berhasil disewanan pada tahun 2011 dan 1012')

#########################
# menjalankan kode main #
#########################
if __name__ == '__main__':
    main()