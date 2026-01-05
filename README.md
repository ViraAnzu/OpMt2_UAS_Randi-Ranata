# Particle Swarm Optimisation (PSO) – UAS Optimasi Metode 2

Project ini merupakan tugas UAS mata kuliah **Optimasi Metode 2**, yang bertujuan untuk mengimplementasikan algoritma **Particle Swarm Optimization (PSO)** mulai dari perhitungan manual menggunakan Excel, implementasi program menggunakan Python, hingga modifikasi studi kasus interaktif berbasis Streamlit.

---

## Deskripsi Singkat
Particle Swarm Optimization (PSO) adalah algoritma optimasi berbasis populasi yang terinspirasi dari perilaku sosial kawanan burung atau ikan. Dalam project ini, PSO digunakan untuk mencari solusi optimal dari suatu fungsi objektif satu dimensi secara bertahap dan terstruktur.

Project ini dikembangkan secara bertahap agar mudah dipahami, mulai dari konsep dasar hingga implementasi interaktif.

---

## Apa itu Particle Swarm Optimisation (PSO)?
Particle Swarm Optimization (PSO) merupakan algoritma optimasi heuristik yang bekerja dengan sekumpulan partikel. Setiap partikel merepresentasikan kandidat solusi dan bergerak di ruang pencarian berdasarkan:

- Pengalaman terbaiknya sendiri (**personal best / pBest**)
- Pengalaman terbaik seluruh partikel (**global best / gBest**)

Pergerakan partikel dikendalikan oleh persamaan kecepatan dan posisi sebagai berikut:

\[
v = wv + c_1 r_1 (pBest - x) + c_2 r_2 (gBest - x)
\]

\[
x = x + v
\]

Algoritma ini bersifat iteratif hingga mencapai kondisi konvergen atau jumlah iterasi tertentu.

---

## Tujuan Project
Tujuan utama dari project ini adalah:
1. Memahami konsep dasar algoritma Particle Swarm Optimization
2. Mengimplementasikan perhitungan PSO secara manual menggunakan Microsoft Excel
3. Menterjemahkan perhitungan tersebut ke dalam bentuk program Python
4. Mengembangkan studi kasus sederhana yang mudah dipahami
5. Membuat aplikasi interaktif berbasis Streamlit untuk visualisasi proses optimasi

---

## Ruang Lingkup & Tahapan Pengerjaan
Project ini dikerjakan melalui beberapa tahapan utama:

1. **Perhitungan Manual (Excel)**
   - Inisialisasi partikel
   - Evaluasi fungsi objektif
   - Penentuan pBest dan gBest
   - Iterasi PSO secara bertahap

2. **Implementasi Python**
   - Translasi rumus PSO dari Excel ke Python
   - Validasi hasil agar konsisten dengan perhitungan manual

3. **Studi Kasus Interaktif**
   - Modifikasi PSO dengan studi kasus sederhana
   - Visualisasi proses konvergensi
   - Interaksi pengguna melalui Streamlit

---

## Studi Kasus
Studi kasus yang digunakan adalah pencarian nilai minimum dari fungsi:

\[
f(x) = (x - a)^2
\]

di mana:
- `a` merupakan target nilai yang dapat diatur oleh pengguna
- PSO digunakan untuk mencari nilai `x` yang meminimalkan fungsi tersebut

Studi kasus ini dipilih karena mudah dipahami dan efektif untuk menjelaskan konsep optimasi.

---

## Teknologi yang Digunakan
- **Python**
- **NumPy**
- **Matplotlib**
- **Streamlit**
- **Microsoft Excel**
- **Google Colab**
- **GitHub**

---

## Struktur Repository
```text
.
├── UAS_OPMT2.py                  # Implementasi PSO dasar
├── UAS_StudiKasus.py             # PSO dengan studi kasus interaktif
├── UAS_OpMt2_Randi Ranata.xlsx   # Perhitungan manual PSO di Excel
├── requirements.txt              # Library yang dibutuhkan
└── README.md                     # Dokumentasi project
```

---

## Cara Menjalankan Program
```
-Menjalankan PSO (Python)-
pip install -r requirements.txt
python UAS_OPMT2.py

-Menjalankan Aplikasi Streamlit-
streamlit run UAS_StudiKasus.py
```

---

## Hasil & Visualisasi

Hasil dari program menunjukkan bahwa algoritma PSO mampu menemukan solusi optimal secara bertahap. Proses konvergensi dapat diamati melalui grafik pergerakan nilai global best (gBest) pada setiap iterasi.

Visualisasi interaktif memudahkan pengguna untuk memahami bagaimana partikel bergerak menuju solusi optimal.
https://uas-opmt2-studikasus.streamlit.app/

<img width="724" height="1143" alt="image" src="https://github.com/user-attachments/assets/add6f970-8202-4edd-ba39-08b484fba9db" />

---

## Kesimpulan

Berdasarkan hasil implementasi, Particle Swarm Optimization terbukti efektif dalam menyelesaikan permasalahan optimasi sederhana. Pendekatan bertahap dari Excel ke Python hingga aplikasi interaktif membantu dalam memahami konsep algoritma secara menyeluruh.

---

## Author

Randi Ranata - 24130500004
