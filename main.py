import streamlit as st
from config import DEFAULT_USERNAME, DEFAULT_PASSWORD

st.set_page_config(page_title='Login - Dashboard AMR', layout='centered')

# Auto-redirect jika sudah login
if st.session_state.get("logged_in"):
    st.markdown("<meta http-equiv='refresh' content='0;url=./Analyze'>", unsafe_allow_html=True)
    st.stop()

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

st.markdown("<h1 style='text-align: center;'>🔐 Sistem Deteksi Anomali Pelanggan AMR</h1>", unsafe_allow_html=True)
st.markdown("Silakan masuk untuk melanjutkan:")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD:
        st.session_state['logged_in'] = True
        st.experimental_rerun()
    else:
        st.error("Username atau password salah.")
