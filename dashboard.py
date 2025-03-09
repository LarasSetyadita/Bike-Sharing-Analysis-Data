import streamlit as st

def main():
    st.title("Selamat datang di Dashbard persewaan sepeda")
    st.subheader("Dashboard ini menampilkan analisis data persewaan sepedan untuk tugas Dicoding")
    st.write("Pilihlah menu yang berada pada sebelah kiri untuk menggunakan dashboard ini!")
    st.image("./images/5243.jpg", caption="Image by pch.vector on Freepik", use_container_width=True)

#########################
# menjalankan kode main #
#########################
if __name__ == '__main__':
    main()