# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Sistem Informasi, E-Government, Manajemen Layanan Publik
  Konteks  : Kementerian Haji dan Umrah Kota Sukabumi (Indonessia)

System Context
  Input       : Permintaan informasi dari calon jemaah haji (pendaftaran porsi, pembatalan, pelimpahan, penggabungan mahram), dokumen persyaratan
  Process     : Proses komunikasi langsung ke kantor, verifikasi dokumen manual, pencatatan status layanan secara konvensional, pengelolaan porsi haji
  Output      : Informasi layanan haji, status proses, balasan dokumen, konfirmasi pendaftaran
  Outcome     : Calon jemaah memahami alur layanan dan dapat melakukan pendaftaran/permohonan dengan jelas; petugas dapat mengelola data terpusat
  Constraints : Kantor hanya buka jam kerja, keterbatasan sumber daya petugas, sistem belum terintegrasi digital, akses informasi terbatas
  Stakeholders: Calon jemaah haji, petugas Kemenag, kepala kantor, administrator sistem

Fenomena → Problem
  Fenomena yang diamati             : Calon jemaah sering mengalami kebingungan dan keterlambatan dalam mendapatkan informasi layanan haji; banyak keluhan tentang proses pendaftaran yang tidak transparan
  Gejala (symptom) yang terukur     : Tingkat kunjungan langsung ke kantor tinggi (data dari kantor: >70% calon jemaah harus datang 2-3x), waktu proses pendaftaran >7 hari, transparansi status 0% (tidak ada update online)
  Masalah yang didiagnosis          : Sistem pelayanan masih manual dan offline; tidak ada platform digital terpusat untuk akses informasi 24/7; pengelolaan dokumen tidak efisien; komunikasi asinkron tidak tersedia
  Masalah riset (researchable)      : Bagaimana merancang dan mengimplementasikan arsitektur sistem informasi berbasis web menggunakan Enterprise Architecture framework (Zachman) yang mampu meningkatkan akses informasi, transparansi status, dan efisiensi proses pelayanan haji?
  Variabel yang terukur             : Waktu akses informasi (detik), tingkat transparansi status (<metrik kepuasan pengguna 0-100), efisiensi proses (hari), jumlah kunjungan langsung ke kantor, tingkat akurasi informasi

Problem Quality Check
  [X] Clarity — Satu orang membaca akan paham: sistem offline → perlu solusi web terintegrasi menggunakan framework Zachman
  [X] Measurability — Ada metrik: timing, transparency score, process efficiency, visit reduction, accuracy rate
  [X] Relevance — Penting untuk domain: layanan publik haji adalah prioritas nasional
  [X] Testability — Bisa gagal: jika platform tidak meningkatkan akses (>=80% calon jemaah puas) atau transparansi (<60%)
  [X] Impact — Ada kontribusi: framework Zachman dapat dipelajari pada domain layanan publik lokal; model arsitektur dapat direplika ke kemenag lain

Problem Statement (1 paragraf):
  Pelayanan informasi haji pada Kementerian Haji dan Umrah Kota Sukabumi masih terkendala oleh sistem manual dan offline, menyebabkan calon jemaah harus datang langsung ke kantor (>70% calon jemaah), menunggu lama (>7 hari), dan menghadapi transparansi status yang minim (0% update online). Sistem belum terintegrasi dengan platform digital, sehingga informasi tentang pendaftaran porsi, pembatalan, pelimpahan, dan penggabungan mahram sulit diakses dan tidak konsisten. Penelitian ini bertujuan merancang dan mengimplementasikan arsitektur sistem informasi berbasis web menggunakan Framework Zachman yang dapat: (1) meningkatkan akses informasi 24/7, (2) memberikan transparansi status real-time (target >80% kepuasan pengguna), dan (3) meningkatkan efisiensi proses selama ≥30% (pengurangan waktu proses dan kunjungan ke kantor). Dengan pendekatan Enterprise Architecture, sistem yang dihasilkan dapat menjadi model replicable untuk layanan publik serupa di instansi pemerintah lain.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Digitalisasi Layanan Informasi Haji menggunakan Platform Web

| Tahap | Hasil |
|-------|-------|
| Reality | Calon jemaah di Kota Sukabumi sering menghadapi kebingungan dan keterlambatan saat mencari informasi tentang pendaftaran porsi haji, pembatalan, pelimpahan, dan penggabungan mahram |
| Observed Issue (Symptom) | Tingkat kunjungan langsung ke kantor Kemenag >70% calon jemaah, waktu rata-rata proses >7 hari, 0% transparansi status online, keluhan calon jemaah tinggi (data dari lapangan jurnal) |
| Diagnosed Problem (Root Cause) | Sistem pelayanan masih manual dan offline (belum ada aplikasi web resmi); pengelolaan dokumen tidak terintegrasi; petugas tidak dapat memberikan update status secara real-time; komunikasi asinkron tidak tersedia; arsitektur sistem tidak terdokumentasi |
| Researchable Problem | Bagaimana merancang arsitektur sistem informasi berbasis web menggunakan Framework Zachman yang dapat meningkatkan akses informasi, transparansi status, dan efisiensi proses pelayanan haji di Kemenag Kota Sukabumi? |
| Measurable Variable | Metrik akses (waktu loading <2 detik), metrik transparansi (tingkat kepuasan pengguna target >80%), metrik efisiensi (pengurangan waktu proses ≥30%), metrik penggunaan (% calon jemaah yang mengakses platform), metrik akurasi informasi (tingkat kesalahan <5%) |

**Apakah terjebak solution-first thinking?** [X] Ya / [ ] Tidak
> Jika ya, kembali ke tahap mana? Pada awalnya sempat terjebak pada tahap "Designer" (langsung memikirkan cara membuat aplikasi dengan Zachman), namun kembali ke tahap "Reality" untuk menggali gejala terukur dan root cause sebelum merancang solusi.

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Request dari calon jemaah (pertanyaan tentang pendaftaran, pembatalan, pelimpahan porsi, penggabungan mahram), dokumen persyaratan (KTP, sertifikat vaksin, surat nikah, dll), permintaan informasi biaya dan jadwal keberangkatan |
| Process | Validasi identitas calon jemaah → Verifikasi dokumen kelengkapan → Pencatatan data ke sistem → Update status permohonan → Pengiriman notifikasi ke calon jemaah → Cetak dokumen konfirmasi |
| Output | Informasi layanan haji lengkap (prosedur, jadwal, biaya), status permohonan real-time (pending/diproses/disetujui/ditolak), dokumen konfirmasi, notifikasi update via email/SMS, laporan data jemaah untuk Kemenag |
| Outcome | Calon jemaah dapat mengakses informasi 24/7 tanpa datang ke kantor; transparansi status meningkat; proses pendaftaran lebih cepat; petugas dapat mengelola data jemaah secara efisien dan terpusat; kepercayaan masyarakat meningkat |
| Constraints | Infrastruktur internet yang stabil di kantor Kemenag, keamanan data jemaah (compliance regulasi), jam operasional server, ketergantungan pada integrasi sistem backend yang existing di Kemenag, skalabilitas untuk menangani peak season (musim haji) |
| Stakeholders | Calon jemaah haji (pengguna akhir), petugas Kemenag (admin/operator data), kepala kantor (decision maker), developer backend dan frontend, database engineer, supervisor IT Kemenag, pemerintah lokal (oversight), asosiasi travel haji |

**Komponen mana yang paling relevan dengan masalah riset?** Input, Process, dan Output — karena masalah inti adalah "bagaimana mengkonversi proses manual → digital" sehingga informasi dapat diakses lebih cepat dan akurat. Constraints juga kritis karena keterbatasan infrastruktur dan compliance harus dipertimbangkan saat design web-based system.

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Sangat jelas: konteks (Kemenag Sukabumi), sistem saat ini (manual offline), masalah spesifik (>70% harus datang, >7 hari, 0% transparansi online), dan solusi yang dicari (web terintegrasi dengan Zachman) terdefinisi dengan baik |
| Measurability | 5 | Metrik kuantitatif spesifik tersedia: waktu akses (<2 detik), kepuasan pengguna (>80%), efisiensi proses (≥30% pengurangan), kunjungan langsung (target >50% berkurang), akurasi informasi (<5% error), dan baseline data diambil dari jurnal |
| Relevance | 5 | Sangat relevan: layanan haji adalah program prioritas nasional Indonesia, Kementerian Haji & Umrah adalah stakeholder resmi, penelitian ini langsung menghadapi masalah real di lapangan, dan hasil dapat di-scale ke kantor Kemenag lain |
| Testability | 4 | Bisa diuji: dapat membandingkan metrik before-after (sistem manual vs aplikasi web); jika platform tidak mencapai target (>80% kepuasan atau akses <2 detik), maka hipotesis terbukti salah; namun kompleksitas banyak variabel eksternal (kecepatan internet, adopsi user) |
| Impact | 5 | Kontribusi signifikan: Framework Zachman diaplikasikan pada domain layanan publik lokal (gap pengetahuan); model arsitektur dapat direplika ke Kemenag lain dan institusi publik serupa; improvement efisiensi berdampak ekonomi dan kepuasan masyarakat |

**Skor total:** 24 / 25

**Problem statement versi final (1 paragraf):**
> Pelayanan informasi haji pada Kementerian Haji dan Umrah Kota Sukabumi mengalami ketidakefisienan akibat sistem yang masih manual dan offline. Fakta lapangan menunjukkan >70% calon jemaah harus mengunjungi kantor secara langsung, proses pendaftaran memakan waktu >7 hari, dan tidak ada transparansi status layanan (0% update online), sehingga menyulitkan calon jemaah untuk memahami alur pendaftaran porsi, pembatalan, pelimpahan, dan penggabungan mahram. Penelitian ini dirancang untuk merancang dan mengimplementasikan arsitektur sistem informasi berbasis web menggunakan Framework Zachman yang mampu: (1) meningkatkan akses informasi 24/7 dengan waktu loading <2 detik, (2) memberikan transparansi status real-time dengan target kepuasan pengguna >80%, dan (3) meningkatkan efisiensi operasional minimal 30% (pengurangan waktu proses dan kunjungan ke kantor). Diharapkan model arsitektur ini dapat menjadi blueprint replicable untuk layanan publik serupa di institusi pemerintah lain, sehingga berkontribusi pada literatur Enterprise Architecture di domain e-government Indonesia.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> **Masalah saat Coding (Engineering Issue):**
> - **Definisi:** Bug atau error adalah anomali dalam kode/sistem yang sudah berjalan → output tidak sesuai harapan (crash, data corrupt, fitur error)
> - **Pendekatan:** Segera debug → trace execution flow → identifikasi source code line → fix bug → test ulang (cepat, iteratif)
> - **Scope:** Fokus pada *how to solve the problem* → kalau sudah berjalan, dianggap selesai
> - **Dokumentasi:** Minimal, usually hanya issue tracking & code comments
>
> **Masalah Riset (Research Problem):**
> - **Definisi:** Problem adalah *gap dalam pengetahuan* atau *gap antara kondisi saat ini dengan yang ideal* → tidak diketahui solusi terbaiknya
> - **Pendekatan:** Methodical investigation → define problem tela perlu, measurable dengan jelas → design experiment/study → collect evidence → prove/disprove hypothesis → generalize finding (lambat, terstruktur)
> - **Scope:** Fokus pada *understanding & proving* → harus bisa direplikasi oleh researcher lain, hindari solution-first thinking
> - **Dokumentasi:** Ekstensif → problem statement, literature review, methodology, results, discussion, conclusion → dipublikasikan
>
> **Perbedaan Fundamental:**
> 1. **Tujuan:** Engineering = *solve an immediate problem*; Research = *understand why & generate new knowledge*
> 2. **Sumber Masalah:** Engineering = bug in code/system; Research = gap in understanding/practice
> 3. **Kepastian Solusi:** Engineering = solusi sudah diketahui (debug); Research = solusi belum diketahui, harus diinvestigasi
> 4. **Keberhasilan:** Engineering = working system; Research = peer-reviewed evidence, replicable findings
> 5. **Waktu Scope:** Engineering = segera; Research = bertahun-tahun (PhD research)
>
> **Pada kasus Aplikasi Haji:** Problem riset bukan hanya "bikin aplikasi web" (engineering) tapi "bagaimana Enterprise Architecture Framework (Zachman) dapat diterapkan pada domain e-government Indonesia & seberapa efektif hasilnya?" (research). Ini mengapa perlu Problem Formation Model yang ketat—agar tidak melompat langsung ke koding tanpa masalah yang jelas.
