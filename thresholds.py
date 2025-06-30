# Halaman Threshold Lengkap
import streamlit as st

st.set_page_config(page_title="Setting Parameter Threshold", layout="wide")
st.title("🔧 Setting Lengkap Parameter Threshold Deteksi Anomali")

st.markdown("### Operasi Logika OR")
st.info("Indikator memenuhi threshold jika **salah satu L1, L2, atau L3** terpenuhi. Digunakan untuk menentukan potensi Target Operasi (TO).")

# --- Tegangan Drop ---
with st.expander("⚡ Tegangan Drop"):
    st.caption("Terjadi saat salah satu L1, L2, L3 bernilai kecil dan positif, arus besar.")
    col1, col2, col3 = st.columns(3)
    tm_drop = col1.number_input("Tegangan Menengah tm <", value=56.00)
    tr_drop = col2.number_input("Tegangan Rendah tr <", value=180.00)
    i_btm = col3.number_input("Arus Besar Bawah tm |I| >", value=0.50)
    i_btr = col1.number_input("Arus Besar Bawah tr |I| >", value=0.50)

# --- Tegangan Hilang ---
with st.expander("🔌 Tegangan Hilang"):
    col1, col2 = st.columns(2)
    v_lost_tm = col1.number_input("Tegangan Hilang tm =", value=0.00)
    v_lost_tr = col2.number_input("Tegangan Hilang tr =", value=0.00)
    i_vlost_tm = col1.number_input("Arus Besar Bawah tm |I| >", value=-1.00)
    i_vlost_tr = col2.number_input("Arus Besar Bawah tr |I| >", value=-1.00)

# --- Cos Phi Kecil ---
with st.expander("💡 Cos Phi Kecil"):
    col1, col2 = st.columns(2)
    cos_tm = col1.number_input("Cos phi ≤ tm", value=0.40)
    cos_tr = col2.number_input("Cos phi ≤ tr", value=0.40)
    i_cos_tm = col1.number_input("Arus Besar tm cos phi kecil |I| >", value=0.80)
    i_cos_tr = col2.number_input("Arus Besar tr cos phi kecil |I| >", value=0.80)

# --- Arus Hilang ---
with st.expander("🚫 Arus Hilang"):
    col1, col2 = st.columns(2)
    i_lost_tm = col1.number_input("Arus Hilang tm <", value=0.02)
    i_lost_tr = col2.number_input("Arus Hilang tr <", value=0.02)
    i_lost_max_tm = col1.number_input("Arus Maksimum tm >", value=1.00)
    i_lost_max_tr = col2.number_input("Arus Maksimum tr >", value=1.00)

# --- Arus Netral > 130% Maksimum ---
with st.expander("🧭 Arus Netral Lebih Besar dari Maks"):
    col1, col2 = st.columns(2)
    i_n_min = col1.number_input("Batas Bawah Arus Netral >", value=1.00)
    i_n_max = col2.number_input("Batas Atas Arus Netral >", value=10.00)

# --- Over Current ---
with st.expander("🔥 Over Current"):
    col1, col2 = st.columns(2)
    i_over_tm = col1.number_input("Arus M Maks tm >", value=5.00)
    i_over_tr = col2.number_input("Arus M Maks tr >", value=5.00)

# --- Over Voltage ---
with st.expander("⚡ Over Voltage"):
    col1, col2 = st.columns(2)
    v_over_tm = col1.number_input("Tegangan Maks tm >", value=62.00)
    v_over_tr = col2.number_input("Tegangan Maks tr >", value=241.00)

# --- Reverse Power ---
with st.expander("🔄 Reverse Power"):
    col1, col2 = st.columns(2)
    p_rev_tm = col1.number_input("Active Power < 0 tm", value=0.00)
    p_rev_tr = col2.number_input("Active Power < 0 tr", value=0.00)
    i_rev_tm = col1.number_input("Arus > tm", value=0.50)
    i_rev_tr = col2.number_input("Arus > tr", value=0.70)

# --- Unbalance Arus ---
with st.expander("🔃 Arus Unbalance"):
    col1, col2 = st.columns(2)
    ub_tm = col1.number_input("Toleransi Unbalance tm", value=0.50)
    ub_tr = col2.number_input("Toleransi Unbalance tr", value=0.50)

# --- Active Power Lost ---
with st.expander("💥 Kehilangan Daya Aktif"):
    p_lost = st.number_input("Batas bawah arus jika power = 0 |I| >", value=0.50)

# --- Arus Kecil Tegangan Kecil ---
with st.expander("📉 Arus Kecil & Tegangan Kecil"):
    col1, col2 = st.columns(2)
    dv_tm = col1.number_input("ΔV Tegangan tm >", value=2)
    dv_tr = col2.number_input("ΔV Tegangan tr >", value=8)

# --- Freeze, Loop, dll ---
with st.expander("🧊 Freeze / Looping / Kriteria Tambahan"):
    st.caption("Kriteria freeze, looping, dan lainnya dapat disesuaikan di backend khusus.")

# --- Kriteria TO ---
with st.expander("📌 Kriteria Penentuan TO"):
    col1, col2, col3 = st.columns(3)
    indikator_min = col1.number_input("Jumlah Indikator Terpenuhi ≥", value=1)
    bobot_min = col2.number_input("Jumlah Bobot ≥", value=2)
    top_n = col3.number_input("Jumlah Data ditampilkan", value=50)

st.success("✅ Semua threshold berhasil dimuat. Lanjutkan ke analisis.")