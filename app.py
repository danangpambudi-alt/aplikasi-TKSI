import streamlit as st

# Judul Aplikasi
st.set_page_config(page_title="Aplikasi TKSI Digital", layout="wide")

def hitung_skor_tksi(jk, child, tok, shuttle, move, bleep, lari600):
    # Logika hitung skor berdasarkan Norma TKSI[cite: 1]
    if jk == 'L':
        s_child = 5 if child >= 17 else 4 if child >= 14 else 3 if child >= 11 else 2 if child >= 8 else 1
        s_tok = 5 if tok >= 8 else 4 if tok >= 6 else 3 if tok >= 3 else 2 if tok >= 1 else 1
        s_shuttle = 5 if shuttle <= 23.18 else 4 if shuttle <= 27.19 else 3 if shuttle <= 30.18 else 2 if shuttle <= 34.2 else 1
        s_move = 5 if move >= 17 else 4 if move >= 14 else 3 if move >= 11 else 2 if move >= 10 else 1
        s_bleep = 5 if bleep > 7.07 else 4 if bleep >= 4.04 else 3 if bleep >= 2.02 else 2 if bleep >= 1.02 else 1
        s_lari = 5 if lari600 <= 2.52 else 4 if lari600 <= 4.57 else 3 if lari600 <= 5.27 else 2 if lari600 <= 6.63 else 1
    else: # Putri[cite: 1]
        s_child = 5 if child >= 14 else 4 if child >= 11 else 3 if child >= 10 else 2 if child >= 9 else 1
        s_tok = 5 if tok >= 6 else 4 if tok >= 4 else 3 if tok >= 2 else 2 if tok >= 1 else 1
        s_shuttle = 5 if shuttle <= 24.58 else 4 if shuttle <= 28.29 else 3 if shuttle <= 31.02 else 2 if shuttle <= 35.74 else 1
        s_move = 5 if move >= 16 else 4 if move >= 12 else 3 if move >= 10 else 2 if move >= 8 else 1
        s_bleep = 5 if bleep > 4.05 else 4 if bleep >= 3.03 else 3 if bleep >= 2.01 else 2 if bleep >= 1.02 else 1
        s_lari = 5 if lari600 <= 3.54 else 4 if lari600 <= 4.79 else 3 if lari600 <= 6.04 else 2 if lari600 <= 7.3 else 1
    
    nilai_akhir = ((s_child + s_tok + s_shuttle + s_move + s_bleep + s_lari) / 6) * 20
    return s_child, s_tok, s_shuttle, s_move, s_bleep, s_lari, nilai_akhir

st.title("🏃‍♂️ Digital TKSI: Rekap Nilai Otomatis")

with st.sidebar:
    st.header("Identitas Siswa")
    nama = st.text_input("Nama Siswa")
    jk = st.selectbox("Jenis Kelamin", ["L", "P"])

st.subheader("Masukkan Hasil Tes")
c1, c2 = st.columns(2)
with c1:
    res_child = st.number_input("Child Ball", 0.0)
    res_tok = st.number_input("Tok Ball", 0.0)
    res_shuttle = st.number_input("Shuttle Run (detik)", 0.0)
with c2:
    res_move = st.number_input("Move The Ball", 0.0)
    res_bleep = st.number_input("Bleep Test (L.B, misal 7.07)", 0.0)
    res_lari = st.number_input("Lari 600m (M.D, misal 2.52)", 0.0)

if st.button("Hitung Sekarang"):
    if nama:
        s1, s2, s3, s4, s5, s6, total = hitung_skor_tksi(jk, res_child, res_tok, res_shuttle, res_move, res_bleep, res_lari)
        st.success(f"Hasil Akhir {nama}: {total:.1f}")
        st.write(f"Detail Skor: Child({s1}), Tok({s2}), Shuttle({s3}), Move({s4}), Bleep({s5}), Lari({s6})")
    else:
        st.warning("Mohon isi nama siswa.")
