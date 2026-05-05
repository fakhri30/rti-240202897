# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (DSR). Penting untuk membedakan keduanya:

| Paradigma | Cara Kerja | Contoh di TI |
|-----------|-----------|---------------|
| **Positivis** | Uji hipotesis dengan eksperimen terkontrol | Apakah CNN lebih akurat dari RF pada dataset X? |
| **Design Science Research** | Bangun artefak (sistem/model/framework) untuk menguji proposisi | Dapatkah arsitektur hybrid CNN+LSTM membuktikan peningkatan recall ≥5%? |
| **Interpretivis** | Pahami makna melalui konteks & kualitatif | Bagaimana peneliti manafsirkan anomali data sensor IoT? |

Dalam DSR, artefak **bukan tujuan akhir** — ia adalah instrumen untuk menghasilkan pengetahuan. Pertanyaan riset tetap harus difalsifikasi.

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Fakhri Fahmi R  
Tanggal          : 16 April 2026  

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Dataset apa yang digunakan dan apakah ada perbandingan dengan metode lain?
   - Data yang dibutuhkan untuk verifikasi: Dataset asli, metode evaluasi, confusion matrix, serta hasil perbandingan dengan baseline model

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [ ] Interpretivis  [x] Design Science  [ ] Mixed
   - Alasan: Penelitian di bidang teknologi informasi sering berfokus pada pembangunan sistem atau artefak (seperti aplikasi atau model) untuk menyelesaikan masalah nyata dan menguji performanya

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Dataset dianggap representatif terhadap kondisi nyata
   - Sumber bias potensial: Bias dataset (tidak seimbang), overfitting, dan pemilihan metrik evaluasi yang tidak tepat
   - Langkah mitigasi: Menggunakan dataset yang beragam, melakukan cross-validation, serta membandingkan dengan beberapa metode lain

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Data eksperimen dan hasil pengujian model
   - Batasan yang diakui sejak awal: Keterbatasan dataset, ruang lingkup penelitian, serta keterbatasan metode yang digunakan

---

---

#  Latihan 1 — Identifikasi Distorsi

**Paper yang dipilih:**
- **Judul:** Aplikasi Web Informasi Layanan Haji pada Kementerian Haji dan Umrah Kota Sukabumi dengan Menggunakan Framework Zachman  
- **Penulis (Tahun):** Zainul Bahar, Sudin Saepudin (2026)  
- **DOI:** https://doi.org/10.61124/sinta.v3i1.140  

---

## Tabel Analisis Distorsi

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|------|-------------------|-----------------|
| Reality → Data | Observasi langsung + studi literatur terkait pelayanan haji | Data hanya dari satu instansi (Sukabumi), tidak representatif |
| Data → Processing | Pengolahan kebutuhan sistem menggunakan Framework Zachman | Interpretasi kebutuhan bisa subjektif (bias peneliti) |
| Processing → Analysis | Analisis kebutuhan sistem, pembuatan model (UML, ERD) | Tidak ada validasi eksternal terhadap model |
| Analysis → Inference | Menyimpulkan bahwa sistem web meningkatkan efisiensi & transparansi | Tidak ada eksperimen kuantitatif |
| Inference → Knowledge | Klaim bahwa sistem dapat meningkatkan pelayanan publik | Generalisasi berlebihan |

---

**Distorsi paling besar di tahap:**  
> Analysis → Inference  

**Dua distorsi spesifik:**
1. Tidak ada pengujian empiris (tidak ada data sebelum vs sesudah sistem)  
2. Generalisasi hanya dari satu studi kasus  

---

#  Latihan 2 — Analisis Kasus Etika

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Peneliti harus melaporkan hasil dengan dan tanpa outlier |
| Transparansi | Harus dijelaskan alasan penghapusan outlier |
| Peer review | Akan dipertanyakan jika data dihapus tanpa alasan jelas |

---

**Keputusan akhir dan justifikasi:**

Outlier tidak boleh dihapus hanya untuk membuat hasil signifikan. Peneliti harus menyajikan kedua hasil (dengan dan tanpa outlier) serta memberikan alasan ilmiah yang jelas agar menjaga integritas penelitian.

---

#  Latihan 3 — Posisi Paradigma

**Topik riset:**  
Perancangan sistem informasi layanan haji berbasis web menggunakan Framework Zachman  

---

## Analisis Paradigma

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian (1–5) | 2 — tidak ada uji hipotesis | 2 — tidak fokus makna sosial | 5 — membangun artefak |
| Jenis data | Data kebutuhan sistem | Observasi pengguna | Model sistem, ERD, UML |
| Limitasi | Tidak ada eksperimen | Kurang konteks sosial | Minim validasi empiris |

---

**Paradigma yang dipilih:**  
> Design Science Research (DSR)  

**Alasan:**  
Penelitian ini membangun artefak berupa sistem informasi berbasis web untuk menyelesaikan masalah nyata, sehingga sesuai dengan pendekatan DSR.

---

#  Refleksi

Sebelumnya, klaim seperti “sistem meningkatkan efisiensi” sering diterima tanpa dipertanyakan. Setelah memahami rantai distorsi, saya akan mempertanyakan bagaimana data dikumpulkan, apakah ada bias, apakah dilakukan pengujian empiris, serta apakah hasil dapat digeneralisasi.

---