import streamlit as st
import pandas as pd
import os

# ==========================
# KONFIGURASI WEBSITE
# ==========================
st.set_page_config(
    page_title="Toko Pashmina 🧕",
    page_icon="🧕",
    layout="wide"
)

# ==========================
# STYLE / BACKGROUND
# ==========================
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(
135deg,
#ffe5ec,
#f0e6ff,
#e8f0fe
);
}

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

h1{
text-align:center;
color:#d90429;
font-size:60px;
}

div[data-testid="column"]{
background:white;
padding:15px;
border-radius:20px;
box-shadow:0px 6px 15px rgba(0,0,0,0.12);
}

</style>
""", unsafe_allow_html=True)

# ==========================
# BANNER
# ==========================
if os.path.exists("Banner.jpg"):
    st.image("Banner.jpg", use_container_width=True)

# ==========================
# JUDUL
# ==========================
st.title("🧕 Toko Pashmina")
st.caption("Premium • Soft • Elegant Hijab Collection ✨")

st.divider()

# ==========================
# BACA CSV
# ==========================
file_data = "data_pashmina.csv"

if os.path.exists(file_data):

    df = pd.read_csv(file_data)

    kategori_list = df["kategori"].unique()

    for kat in kategori_list:

        st.header(f"✨ {kat}")

        data_kat = df[df["kategori"] == kat]

        cols = st.columns(3)

        for index, row in data_kat.reset_index().iterrows():

            with cols[index % 3]:

                # ==========================
                # FOTO (FIX PATH AMAN)
                # ==========================
                nama_foto = os.path.join(
                    os.path.dirname(__file__),
                    str(row["foto"]).strip()
                )

                if os.path.exists(nama_foto):
                    st.image(nama_foto, use_container_width=True)
                else:
                    st.caption(f"🚫 Foto tidak ditemukan: {row['foto']}")

                # ==========================
                # NAMA PRODUK
                # ==========================
                st.subheader(row["nama"])

                # ==========================
                # HARGA
                # ==========================
                st.markdown(f"### 💸 Rp {row['harga']:,}")

                # ==========================
                # STATUS
                # ==========================
                st.success(f"Status: {row['status']}")

                # ==========================
                # TOMBOL ORDER
                # ==========================
                if st.button(
                    f"🛒 Order {row['nama']}",
                    key=f"order_{kat}_{index}"
                ):
                    st.success("Pesanan ditambahkan ke keranjang!")

        st.divider()

else:
    st.error("File data_pashmina.csv tidak ditemukan!")

# ==========================
# FOOTER
# ==========================
st.subheader("📍 Hubungi Kami")

col1, col2 = st.columns(2)

with col1:
    st.info("""
🏪 **Toko Pashmina**

Yogyakarta, Indonesia 🇮🇩
""")

with col2:

    no_hp = "6281234567890"
    pesan = "Halo Kak! Saya ingin memesan pashmina 🧕"
    link = f"https://wa.me/{no_hp}?text={pesan.replace(' ','%20')}"

    st.link_button(
        "📱 Pesan via WhatsApp",
        link
    )

st.caption("© 2026 Toko Pashmina — Elegance in Every Fold ✨")
