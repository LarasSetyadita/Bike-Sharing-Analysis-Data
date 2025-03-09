import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def grafik():
    avg_rentals_hour_2011 = pd.read_csv('./data/avg_rentals_hour_2011.csv')
    avg_rentals_hour_2012 = pd.read_csv('./data/avg_rentals_hour_2012.csv')

    tahun_terpilih = st.radio("Pilih Tahun:", [2011, 2012])

    # Pilihan musim dengan Multi Select
    musim_terpilih = st.multiselect("Pilih Musim:", ["springer", "summer", "fall", "winter"], default=["springer", "summer", "fall", "winter"])

    # Menentukan DataFrame berdasarkan pilihan tahun
    if tahun_terpilih == 2011:
        data_terpilih = avg_rentals_hour_2011
    else:
        data_terpilih = avg_rentals_hour_2012

    # Filter data berdasarkan musim yang dipilih
    filtered_data = data_terpilih[data_terpilih["season"].isin(musim_terpilih)]

    # Cek apakah data ada setelah difilter
    if not filtered_data.empty:
        # Membuat plot
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(data=filtered_data, x="hour", y="count", hue="season", marker="o", ax=ax)

        # Menambahkan judul dan label
        ax.set_title(f"Tren Penyewaan Sepeda per Jam Berdasarkan Musim Tahun {tahun_terpilih}", fontsize=14)
        ax.set_xlabel("Jam", fontsize=12)
        ax.set_ylabel("Jumlah Sewa", fontsize=12)
        ax.legend(title="Musim")

        # Menampilkan grafik di Streamlit
        st.pyplot(fig)
    else:
        st.warning("Tidak ada data untuk kombinasi tahun dan musim yang dipilih.")  # Menampilkan grafik di Streamlit

def main():
    st.title("📊 Analisis Tren Penyewaan Sepeda Perjam Setiap Musim")

    # Menampilkan grafik
    grafik()

#########################
# menjalankan kode main #
#########################
if __name__ == '__main__':
    main()