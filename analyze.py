import streamlit as st
import pandas as pd

st.set_page_config(page_title="Analisis Data AMR", layout="wide")
st.title("📈 Analisis Lengkap Data Pelanggan AMR")

uploaded_file = st.file_uploader("📤 Upload File Data INSTANT AMR (XLSX)", type=["xlsx"])

# Default Threshold jika belum diset
default_thresholds = {
    "v_drop": 200,
    "arus_min": 0.05,
    "power_zero_I_gt": 0.5,
    "cos_phi_kecil": 0.4,
    "unbalance_I": 0.5,
    "arus_hilang": 0.02,
    "arus_max": 1.0,
    "over_voltage": 240,
    "over_current": 5,
}

for k, v in default_thresholds.items():
    if k not in st.session_state:
        st.session_state[k] = v

if uploaded_file:
    try:
        df_raw = pd.read_excel(uploaded_file, sheet_name="Sheet2", header=0)

        if "LOCATION_TYPE" not in df_raw.columns:
            st.error("Kolom 'LOCATION_TYPE' tidak ditemukan di Sheet2.")
        else:
            df = df_raw[df_raw["LOCATION_TYPE"].str.upper() == "CUSTOMER"].copy()
            st.success(f"Ditemukan {len(df)} baris data CUSTOMER")

            st.markdown("### 🔍 Sampel Data Pelanggan")
            display_cols = [col for col in df.columns if any(x in col.upper() for x in ["LOCATION", "VOLTAGE", "CURRENT", "POWER"])]
            st.dataframe(df[display_cols].head(10))

            # Deteksi indikator teknikal (menggunakan threshold)
            df["v_drop"] = (df["VOLTAGE_L1"] < st.session_state["v_drop"]) |                            (df["VOLTAGE_L2"] < st.session_state["v_drop"]) |                            (df["VOLTAGE_L3"] < st.session_state["v_drop"])

            df["arus_hilang"] = (df["CURRENT_L1"] < st.session_state["arus_min"]) &                                 (df["CURRENT_L2"] < st.session_state["arus_min"]) &                                 (df["CURRENT_L3"] < st.session_state["arus_min"])

            df["power_lost"] = (df["POWER_ACTIVE_TOTAL"] <= 0) & (
                (df["CURRENT_L1"] > st.session_state["power_zero_I_gt"]) |                 (df["CURRENT_L2"] > st.session_state["power_zero_I_gt"]) |                 (df["CURRENT_L3"] > st.session_state["power_zero_I_gt"])
            )

            df["over_voltage"] = (df["VOLTAGE_L1"] > st.session_state["over_voltage"]) |                                  (df["VOLTAGE_L2"] > st.session_state["over_voltage"]) |                                  (df["VOLTAGE_L3"] > st.session_state["over_voltage"])

            df["over_current"] = (df["CURRENT_L1"] > st.session_state["over_current"]) |                                  (df["CURRENT_L2"] > st.session_state["over_current"]) |                                  (df["CURRENT_L3"] > st.session_state["over_current"])

            df["Jumlah Potensi TO"] = df[[
                "v_drop", "arus_hilang", "power_lost", "over_voltage", "over_current"
            ]].sum(axis=1)

            df["SUM_WEIGHTED"] = df["Jumlah Potensi TO"] * 6

            st.markdown("### 🚨 Hasil Deteksi Anomali")
            st.dataframe(df[[
                "LOCATION_CODE", "v_drop", "arus_hilang", "power_lost",
                "over_voltage", "over_current", "Jumlah Potensi TO", "SUM_WEIGHTED"
            ]].head(30))

            st.markdown("### 📥 Unduh Hasil Analisis")
            to_export = df[[
                "LOCATION_CODE", "v_drop", "arus_hilang", "power_lost",
                "over_voltage", "over_current", "Jumlah Potensi TO", "SUM_WEIGHTED"
            ]]
            st.download_button("💾 Download Excel", to_export.to_excel(index=False), "hasil_analisis_lengkap.xlsx")

    except Exception as e:
        st.error(f"Gagal membaca file: {e}")
else:
    st.info("Silakan upload file INSTANT AMR terlebih dahulu.")
