# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

**Perbandingan pendekatan Author-centric vs Concept-centric:**

| Aspek | Author-centric (Hindari) | Concept-centric (Gunakan) |
|-------|--------------------------|---------------------------|
| Struktur | Per penulis/paper ("Rahman et al. menyatakan...") | Per konsep/metode ("Pendekatan berbasis transformer") |
| Tujuan | Ringkasan isi paper | Perbandingan metode & identifikasi gap |
| Contoh paragraph | "Rahman (2023) pakai CNN. Lee (2022) pakai LSTM. Zhang (2021) pakai RF." | "Tiga pendekatan dominan: CNN digunakan oleh 4 paper untuk representasi fitur visual; LSTM untuk data sekuensial; RF sebagai baseline klasik." |
| Hasil akhir | Daftar paper | Peta pengetahuan + gap yang teridentifikasi |

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database utama**: IEEE Xplore, ACM DL, Scopus
   - Akses IEEE/ACM melalui jaringan kampus atau VPN institusi
   - Alternatif bebas biaya: Google Scholar, ResearchGate ([researchgate.net](https://www.researchgate.net)), arXiv ([arxiv.org](https://arxiv.org))
2. **Boolean query** yang terdokumentasi eksplisit
   - Contoh: `("anomaly detection" OR "intrusion detection") AND ("deep learning" OR "neural network") NOT ("medical imaging")`
   - Gunakan tanda kutip untuk frasa eksak; AND/OR/NOT mengontrol scope
3. **Snowballing** — dua arah:
   - **Backward snowballing**: buka daftar referensi di paper kunci → telusuri paper yang dikutip
   - **Forward snowballing**: di Google Scholar, klik "Cited by" di bawah paper kunci → temukan paper yang mengutipnya
   - Ulangi 1–2 tingkat untuk membangun cakupan komprehensif
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Sistem Informasi Pelayanan Haji dan Umroh Berbasis Web
Database   : SINTA, IEEE Xplore, Academia.edu
Query      : ("information system" OR "sistem informasi") AND ("hajj" OR "umroh" OR "haji") AND ("web application" OR "web-based")
Tahun      : 2021-2026
Hasil awal : 5 paper → Screening → 5 paper final (semua relevan)

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| Bahar & Saepudin | 2026 | Framework Zachman, UML | Kemenag Sukabumi | Arsitektur sistem terstruktur 6 perspektif | Scope terbatas (haji saja) |
| Arvita | 2021 | Prototype, UML | Travel Jambi | Sistem web registrasi + manajemen data | Belum ada evaluasi keamanan |
| Novariadi | 2021 | Interview & Observasi | Kemenag Kuantan Singingi | E-Katalog database PHP & MySQL | Hanya katalog, bukan registrasi end-to-end |
| Mohamad et al. | 2023 | DFD + GIS | Travel Kendari | Sistem GIS + Google Maps API | Hanya paket/lokasi, belum administrasi |
| Maryana & Fatah | 2025 | Waterfall, UML | Kemenag Bondowoso | Pendaftaran online + verifikasi pembayaran | Masih fase desain, belum implementasi |

Pola yang ditemukan:
  Metode dominan     : Zachman, Waterfall, Prototype; UML/DFD; PHP-MySQL stack; Google Maps API
  Dataset umum       : Institusi lokal (Kemenag regional, travel lokal); belum ada standardisasi dataset
  Limitasi berulang  : Fragmentasi sistem (registrasi ≠ pembayaran ≠ GIS mapping); scope per-komponen; evaluasi terbatas

GAP IDENTIFICATION

Gap 1: [Jenis: method]
  Deskripsi    : Tidak ada sistem terintegrasi end-to-end (registrasi + dokumen + pembayaran + pemetaan lokasi travel)
  Bukti        : Semua 5 paper hanya mengatasi 1-2 komponen terpisah; fragmentasi data antar sistem
  Signifikansi : Calon jamaah harus mengakses multiple platform; user experience buruk; data redundancy tinggi

Gap 2: [Jenis: context]
  Deskripsi    : Semua evaluasi pada konteks lokal regional, belum ada harmonisasi nasional
  Bukti        : Studi di 5 kota berbeda dengan spesifikasi lokal; tidak ada perbandingan lintas-instansi
  Signifikansi : Sulit untuk generalisasi; tidak ada best practices yang terstandarisasi di level nasional

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
| Zachman Framework (Bahar & Saepudin 2026) | Enterprise architecture design untuk sistem kompleks haji | Common practice 6-perspektif di organisasi besar | Bahar & Saepudin (2026) |
| GIS + Web Integration (Mohamad et al. 2023) | Pemetaan lokasi travel + integrasi web; aspek discovery UX | Best practice industri travel dengan Google Maps API | Mohamad et al. (2023) |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan database akademik.

> **Panduan pencarian:**
> - Database: IEEE Xplore, ACM DL, Google Scholar, atau ResearchGate
> - Tulis query Boolean yang digunakan: contoh `("object detection" OR "image classification") AND ("edge computing") NOT ("medical")`. Dokumentasikan query secara eksplisit.
> - Akses gratis: buka Google Scholar → cari judul paper → klik [PDF] jika tersedia, atau akses lewat campus VPN

**Topik riset:** Sistem Informasi Pelayanan Haji dan Umroh Berbasis Web
**Query pencarian:** ("information system" OR "sistem informasi") AND ("hajj" OR "umroh" OR "haji") AND ("web application" OR "web-based")
**Database:** SINTA, IEEE Xplore, Academia.edu

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Bahar & Saepudin | 2026 | Framework Zachman, UML | Kemenag Sukabumi | Arsitektur sistem terstruktur (Scope, Owner, Designer, Implementation, Technology, Function) | Hanya fokus aspek haji (tidak termasuk manasik, transportasi, kesehatan) |
| 2 | Arvita | 2021 | Prototype, UML (Usecase, Class, Activity) | Travel Jambi | Sistem web fungsional dengan fitur registrasi, manajemen data, laporan | Belum ada evaluasi keamanan data |
| 3 | Novariadi | 2021 | Interview, Observasi, Studi Pustaka | Kemenag Kuantan Singingi | E-Katalog database dengan PHP & MySQL | Hanya fokus pada katalog/pengarsipan, tidak mencakup proses pendaftaran |
| 4 | Mohamad et al. | 2023 | Data Flow Diagram (DFD) | Travel Kendari | Sistem dengan GIS + Google Maps API untuk pemetaan lokasi travel | Hanya info paket/lokasi, tidak terintegrasi dengan proses administrasi jamaah |
| 5 | Maryana & Fatah | 2025 | Waterfall, UML | Kemenag Bondowoso | Sistem pendaftaran online dengan formulir digital & verifikasi pembayaran | Masih dalam fase desain, belum implementasi penuh |

**Pola yang terlihat — Metode dominan:** 
- **Framework/Methodology:** Zachman, Waterfall, Prototype (Iteratif), DFD
- **Technology Stack:** PHP, MySQL, Google Maps API, UML/BPMN untuk modeling
- **Domain fokus:** Web information system, e-registration, document management, geographic information

**Limitasi yang berulang:** 
- Scope terbatas (hanya satu aspek dari proses haji/umroh yang komprehensif)
- Belum ada integrasi end-to-end antara registrasi, pembayaran, dokumentasi, dan pemetaan lokasi travel
- Aspek keamanan data dan integrasi API pihak ketiga kurang dibahas
- Evaluasi sistem (testing, user satisfaction) masih minimal

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [x] Ya / [ ] Tidak | Hanya 3 dari 5 sistem mencapai implementasi penuh; 2 sistem masih dalam fase desain (prototype/belum production-ready). Tidak ada data tentang akurasi validasi data atau response time sistem |
| Method Gap | [x] Ya / [ ] Tidak | Tidak ada studi yang mengintegrasikan seluruh framework (registrasi + dokumentasi + pembayaran + GIS mapping) dalam satu sistem terpadu. Setiap studi hanya mengatasi satu atau dua komponen |
| Data Gap | [x] Ya / [ ] Tidak | Belum ada dataset publik atau benchmark untuk sistem informasi haji. Semua studi menggunakan data lokal dari satu institusi (Kemenag atau travel lokal) tanpa generalisasi |
| Context Gap | [x] Ya / [ ] Tidak | Semua studi dilakukan pada konteks lokal (Sukabumi, Jambi, Kuantan Singingi, Kendari, Bondowoso). Belum ada evaluasi di level nasional atau perbandingan lintas-instansi |

**Gap utama yang dipilih:** Method Gap — Integrasi end-to-end sistem informasi haji yang mencakup registrasi, manajemen dokumen, verifikasi pembayaran, dan pemetaan lokasi travel dalam satu platform terpadu
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Fragmentasi sistem saat ini menyebabkan calon jamaah harus mengakses multiple systems untuk registrasi (di Kemenag), pembayaran (di travel), dan informasi lokasi (di Google Maps atau web travel). Integrasi terpadu akan meningkatkan user experience, mengurangi data redundancy, dan memfasilitasi transparansi end-to-end dari proses pendaftaran hingga keberangkatan.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | Framework Zachman untuk Enterprise Architecture Design (Bahar & Saepudin 2026) | Secara langsung mengatasi desain arsitektur sistem haji yang kompleks, mencakup perspektif Planner, Owner, Designer, dan Implementation | Digunakan oleh organisasi besar (Kemenag Sukabumi) sebagai framework standard untuk enterprise systems; 6 perspektif Zachman menjadi common practice | Ya, SOTA: publikasi 2026 dan menggunakan framework yang paling terstruktur untuk pemetaan arsitektur | Bahar & Saepudin (2026), SINTA |
| 2 | Sistem Informasi Geografis + Web Integration untuk Travel Information (Mohamad et al. 2023) | Menambahkan dimensi geografis (pemetaan lokasi travel dengan Google Maps API) yang belum ada di studi lainnya; merepresentasikan aspek "discovery" dalam UX | Kombinasi GIS + web framework menjadi best practice di industri travel; diaplikasikan di multiple travel agencies (Kendari region) | SOTA: publikasi 2023 dengan teknologi mutakhir (Google Maps API + PHP/MySQL stack yang masih relevan) | Mohamad et al. (2023), JSITK |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [x] Tidak
> Justifikasi: Kedua baseline dipilih karena (1) representasi dari metodologi mainstream (Zachman, GIS), (2) publikasi terbaru (2023-2026), (3) aplikasi pada konteks nyata (institusi haji dan travel), dan (4) komplementer (satu fokus pada architecture, satu fokus pada geographic discovery). Keduanya mengatasi gap yang berbeda dalam sistem informasi haji.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> **Perbedaan Fundamental:**
> - **"Belum ada yang meneliti" (tanpa bukti):** Sebuah klaim yang tidak didukung oleh dokumentasi pencarian sistematis. Peneliti tidak menunjukkan query yang digunakan, database yang dicek, atau kriteria inklusi/eksklusi. Ini jatuh kategori "absence of evidence is not evidence of absence."
> - **Research gap yang valid:** Didukung oleh bukti pencarian terstruktur (documented query, database list, snowballing), analisis pola dari literature existing, dan identifikasi kontras antara "apa yang sudah dilakukan" vs "apa yang belum atau tidak optimal."
>
> **Cara Membuktikan Gap Benar-Benar Ada:**
> 1. **Systematic Search (Backward Snowballing):** Mulai dari paper kunci (contoh: Bahar & Saepudin 2026 untuk Zachman framework haji), telusuri referensi mereka, dan dokumentasikan semua paper terkait. Ulangi 1-2 tingkat.
> 2. **Snowballing Maju (Forward Citation):** Di Google Scholar, lihat "Cited by" dari paper kunci → temukan paper yang membangun di atasnya → catat apakah ada yang mengatasi gap atau justru mewariskan limitation.
> 3. **Analisis Pola dari 5+ Paper:** Seperti pada latihan ini: semua 5 paper menunjukkan fragmentasi (registrasi terpisah dari GIS, dari dokumentasi). Ini bukan coincidence — ini adalah pattern yang menunjukkan gap metodologis yang genuine.
> 4. **Context Gap Confirmation:** Verifikasi bahwa gap tidak hanya berada di akademia, tetapi juga di praktik industri. Contoh: wawancara dengan staff Kemenag atau travel agencies akan membuktikan bahwa sistem saat ini memang terpisah-pisah.
> 5. **Dokumentasi Eksplisit:** Tulis: "Query: [...], Database: [IEEE, SINTA, ...], Tahun: [2018-2026], Hasil: [X paper menemukan A, Y paper menemukan B, tetapi tidak ada yang mengintegrasikan A+B]."
>
> **Kesimpulan:** Gap yang valid bukan sekadar "belum diteliti," tetapi "ada kontradiksi, fragmentasi, atau limitation yang teridentifikasi melalui bukti empiris dari literature existing dan diperkuat oleh context praktis di lapangan."
