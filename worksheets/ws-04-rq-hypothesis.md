# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : Belum ada sistem informasi haji yang terintegrasi end-to-end (registrasi + manajemen dokumen + verifikasi pembayaran + pemetaan lokasi travel). Literatur menunjukkan fragmentasi: Zachman untuk arsitektur, GIS untuk pemetaan, prototype untuk registrasi — namun tidak ada integrasi terpadu dalam satu platform

Research Question:
  Tipe         : [x] Comparison  [ ] Improvement  [ ] Exploratory
  Formulasi    : Apakah arsitektur sistem informasi haji terintegrasi (Framework Zachman + GIS + Payment) menghasilkan peningkatan signifikan dalam akses informasi, transparansi status, dan efisiensi proses dibandingkan sistem fragmentasi manual?
  Variabel IV  : Tipe arsitektur sistem (Integrated/Zachman vs Fragmented/Manual) - nominal
  Variabel DV  : (1) Waktu akses (detik), (2) Transparansi status (0-100), (3) Efisiensi proses (hari), (4) Kepuasan pengguna (Likert 1-5)
  Metrik       : Primary: Response time <2 detik, Transparency >80%, Process efficiency <1 hari. Secondary: User satisfaction >4/5
  Dataset      : Data Kemenag Sukabumi (Bahar & Saepudin 2026): ~2000 calon jemaah/tahun, dokumen persyaratan, jadwal porsi
  Baseline     : Sistem manual saat ini (0% online access) + Zachman framework (Bahar 2026) + GIS-integrated (Mohamad 2023)

Quality Check RQ:
  [x] Variabel spesifik — IV (tipe arsitektur), DV (4 variabel)
  [x] Metrik jelas — Response time, transparency score, efficiency days, satisfaction Likert
  [x] Baseline ada — Sistem manual + 2 framework dari literatur
  [x] Konteks disebutkan — Kemenag Sukabumi, calon jemaah, domain haji
  [x] Memerlukan eksperimen — A/B testing, pilot deployment, measurement

Contribution Statement:
  Apa yang baru diketahui : Arsitektur Zachman + GIS + Payment Gateway terintegrasi meningkatkan akses 24/7 dengan transparansi real-time, mengurangi waktu proses dari >7 hari ke <1 hari, kepuasan >80% pada sistem pelayanan publik haji
  Jenis kontribusi        : [x] Improvement (arsitektur terbukti lebih baik) + [x] Comparison (integrated vs fragmented)
  Gap yang diisi          : Method Gap (integrasi end-to-end) + Context Gap (evaluasi nasional Kemenag)

Hypothesis Pair:
  H₀ : Tidak ada perbedaan signifikan dalam waktu akses, transparansi, efisiensi, dan kepuasan antara sistem terintegrasi dan sistem manual
  H₁ : Sistem terintegrasi menghasilkan: waktu akses <2 detik (vs >300s manual), transparansi >80% (vs 0%), efisiensi <1 hari (vs >7 hari), kepuasan >4/5
  Threshold              : p-value <0.05, Cohen's d >0.8, minimum 30% improvement
  Justifikasi threshold  : Standard signifikansi akademik; effect size large untuk perbedaan praktis; 30% improvement sesuai ROI institusi publik
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Belum ada studi yang mengintegrasikan seluruh framework (registrasi + dokumentasi + pembayaran + GIS mapping). Semua 5 paper hanya mengatasi 1-2 komponen terpisah. Evaluasi hanya lokal regional, belum nasional.

**RQ versi pertama (tulis bebas):**
> Bagaimana merancang sistem informasi haji yang terintegrasi? Apakah sistem terpadu lebih baik dari sistem fragmentasi saat ini?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | Ya | Framework Zachman + GIS API + Payment Gateway |
| Metrik terukur | Ya | Waktu akses (<2 detik), transparansi (0-100), efisiensi (hari), kepuasan (Likert 1-5) |
| Baseline | Ya | Sistem manual saat ini vs Zachman (Bahar 2026) vs GIS (Mohamad 2023) |
| Dataset/konteks | Ya | Data Kemenag Sukabumi, ~2000 jemaah/tahun, domain haji |

**Tipe RQ:** [x] Comparison / [ ] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah arsitektur sistem informasi haji terintegrasi (Framework Zachman + GIS + Payment) menghasilkan peningkatan waktu akses <2 detik, transparansi >80%, efisiensi proses <1 hari, dan kepuasan pengguna >80% dibandingkan sistem fragmentasi manual pada Kemenag Sukabumi?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Tidak ada perbedaan signifikan dalam waktu akses, transparansi, efisiensi, dan kepuasan antara sistem terintegrasi dan sistem manual |
| H₁ | Sistem terintegrasi menghasilkan: waktu akses <2 detik (vs >300s manual), transparansi >80% (vs 0%), efisiensi <1 hari (vs >7 hari), kepuasan >4/5 |
| Metrik | Primary: Response time (second), Transparency score (0-100), Process efficiency (days). Secondary: User satisfaction (Likert 1-5) |
| Threshold | p-value <0.05, Cohen's d >0.8, minimum 30% improvement |
| Justifikasi threshold | Standard akademik signifikansi (p<0.05); effect size large (d>0.8) menunjukkan perbedaan praktis; 30% improvement sesuai ROI institusi publik |

**Apakah hipotesis ini falsifiable?** [x] Ya / [ ] Tidak
> Cara membuktikannya salah: Jika response time >2 detik ATAU transparansi <80% ATAU efisiensi >1 hari ATAU satisfaction <4/5 ATAU p-value >0.05, maka H₁ ditolak dan H₀ diterima.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Apakah sistem terintegrasi Zachman+GIS meningkatkan waktu akses, transparansi, efisiensi, dan kepuasan dibanding sistem manual? |
| Variable (IV) | Tipe arsitektur sistem (Integrated vs Fragmented/Manual) — Nominal |
| Variable (DV) | (1) Response time (ratio, detik), (2) Transparency score (ratio, 0-100), (3) Process efficiency (ratio, hari), (4) User satisfaction (ordinal, Likert 1-5) |
| Metric | Primary: Response time <2s, Transparency >80%, Efficiency <1 day. Secondary: Satisfaction >4/5 |
| Data source | System logs (automated metrics), User questionnaire (satisfaction), Kemenag records (process time before/after) |
| Analysis method | Descriptive statistics (mean, SD), Independent t-test atau Mann-Whitney U (ordinal), Effect size (Cohen's d), Paired comparison before-after |

**Apakah rantai lengkap?** [x] Ya / [ ] Tidak
> Semua tahap dari RQ abstrak hingga analisis konkret terdokumentasi. Tidak ada lompatan logis antara tahapan.

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Aplikasi Web Informasi Layanan Haji pada Kementerian Haji dan Umrah Kota Sukabumi dengan Menggunakan Framework Zachman (Bahar & Saepudin 2026)

**RQ yang diekstrak:** Bagaimana merancang aplikasi web informasi layanan haji menggunakan Framework Zachman yang dapat meningkatkan efisiensi, transparansi, dan kualitas pelayanan?

**Komponen yang hilang:** 
- **Metode spesifik:** Zachman disebutkan tapi tidak ada baseline perbandingan (sistem apa sebelumnya?)
- **Metrik terukur:** Hanya "meningkatkan efisiensi" tanpa KPI konkret (waktu, % improvement)
- **Baseline:** Tidak jelas dibanding dengan apa; sistem manual? sistem lain?
- **Falsifiability:** Tidak ada threshold kesuksesan; RQ tidak bisa dibuktikan salah
- **Design eksperimen:** Paper hanya prototipe, tidak ada user testing atau metrik kuantitatif

**Kesimpulan:** Paper tersebut adalah **design-focused** (cocok engineering), bukan **research-focused**. Untuk menjadi research question rigorous, harus ditambahkan: (1) comparison baseline, (2) quantified metrics + KPI, (3) hypothesis testing, (4) before-after measurement atau A/B testing.
