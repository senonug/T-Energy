# Dashboard Deteksi Anomali AMR PLN

Dashboard ini digunakan untuk mendeteksi potensi Target Operasi (TO) dari data pelanggan AMR berdasarkan parameter teknikal seperti arus, tegangan, dan daya aktif.

## 📦 Fitur
- Login aman (username/password)
- Upload file INSTANT AMR (Sheet2)
- Deteksi otomatis: tegangan drop, arus hilang, daya negatif, dsb
- Pengaturan threshold anomali
- Ekspor hasil ke Excel

## 🚀 Cara Menjalankan
1. Install dependensi:
```bash
pip install -r requirements.txt
```

2. Jalankan aplikasi:
```bash
streamlit run main.py
```

## 🔐 Login
- **Username:** admin  
- **Password:** admin

## 📝 Catatan
- Hanya data `LOCATION_TYPE == CUSTOMER` yang diproses
- File yang didukung: `.xlsx` dengan `Sheet2`
