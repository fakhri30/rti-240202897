# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: Apakah arsitektur sistem terintegrasi (Zachman+GIS+Payment) menghasilkan peningkatan akses, transparansi, efisiensi, kepuasan dibanding sistem fragmented manual?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
| Tipe Arsitektur Sistem | IV | Pendekatan arsitektur (terintegrasi vs fragmentasi) | 2 kategori: Integrated / Fragmented | Nominal | N/A | Toggle mode sistem | IV yang merepresentasikan kondisi eksperimen |
| Waktu Akses Informasi | DV | Kecepatan akses data layanan haji | Response time <2 detik vs baseline >300 detik | Ratio | Detik (second) | Server log timestamp (automated) | Memenuhi UX standard industri; <2s target |
| Transparansi Status | DV | Tingkat visibility status permohonan jamaah | Score 0-100 berdasarkan update frequency | Ratio | Score (0-100) | Automated tracking + user survey | Mengukur real-time visibility (integrated vs manual 0%) |
| Efisiensi Proses | DV | Durasi dari pendaftaran hingga konfirmasi | Hari proses (target <1 hari vs baseline >7 hari) | Ratio | Hari (days) | Timestamp mulai-selesai database | Metrik langsung dampak bisnis (ROI) |
| Kepuasan Pengguna | DV | Persepsi jamaah terhadap sistem | Likert scale 1-5 (target >4 vs baseline ~2) | Ordinal | Rating (1-5) | Post-task questionnaire SUS-style | Mengukur user experience & adoption |
| Infrastruktur Internet | CV | Kualitas koneksi jaringan Kemenag | Bandwidth (Mbps) & uptime (%) | Ratio | Mbps, % | Network monitoring tool | Kontrol: harus stabil untuk fair comparison |
| Skill Petugas | CV | Keahlian operator sistem Kemenag | Hours training completed | Ratio | Jam (hours) | Training log | Kontrol: semua petugas terlatih sama |
| Dataset Jemaah | CV | Volume & karakteristik data | N=2000/tahun, demografi mixed | Nominal | Jumlah | Admin records Kemenag | Kontrol: dataset konsisten across conditions |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [x] Setiap langkah terdokumentasi — dari RQ deskriptif hingga metrik konkret
  [x] Tidak ada "lompatan logis" — DV jelas dari konsep ke operasi
  [x] Metrik mengukur apa yang dimaksud (construct validity) — response time = akses, Likert = kepuasan
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Apakah arsitektur sistem terintegrasi (Zachman+GIS+Payment) menghasilkan peningkatan waktu akses <2 detik, transparansi >80%, efisiensi <1 hari, kepuasan >4/5 dibanding sistem fragmented manual?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan | Target |
|----------|------|---------------|----------------|-------------|--------|--------|
| Tipe Arsitektur | IV | Pendekatan sistem (integrated vs manual/fragmented) | 2 kondisi: Integrated vs Fragmented | Nominal | — | Both tested |
| Response Time | DV | Kecepatan akses informasi layanan haji | Time dari request ke response | Ratio | Detik | <2 detik |
| Transparency Score | DV | Tingkat visibility & update real-time status | % requests updated <1 jam | Ratio | Score 0-100 | >80% |
| Process Duration | DV | Total waktu registrasi hingga konfirmasi | Calendar days dari timestamp | Ratio | Hari | <1 hari |
| User Satisfaction | DV | Persepsi jamaah (ease, speed, clarity, trust) | Likert questionnaire (5 items, mean) | Ordinal | Rating 1-5 | >4/5 |
| Network Infrastructure | CV | Bandwidth & uptime server | Mbps & % uptime | Ratio | Mbps, % | Stabil >99% |
| User Training | CV | Skill level operator Kemenag | Hours formal training | Ratio | Jam | Standar 40 jam |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [x] Tidak
> Semua tahapan jelas: dari konsep abstrak (akses cepat) ke operasi konkret (response time <2 detik)

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Metrik | Representative | Sensitive | Feasible | Justifikasi |
|--------|---|---|---|---|
| Response Time | 5/5 | 5/5 | 5/5 | Langsung mewakili "akses cepat"; peka terhadap performa; otomatis via server logs |
| Transparency Score | 4/5 | 5/5 | 4/5 | Mewakili visibility; peka terhadap perubahan (manual=0%, integrated >80%); perlu aggregasi |
| Process Duration | 5/5 | 4/5 | 5/5 | Langsung ROI bisnis; peka (7 hari vs 1 hari jelas); feasible dari database timestamps |
| User Satisfaction | 5/5 | 3/5 | 4/5 | Mewakili persepsi holistik; kurang sensitif (Likert discrete); memerlukan survey |

**Apakah perlu secondary metric?** [x] Ya / [ ] Tidak
> User Satisfaction (Likert) sebagai secondary karena: (1) primary metrics fokus pada performance objektif, (2) satisfaction mengukur adoption/UX yang berbeda, (3) stakeholder (Kemenag) butuh user acceptance data, bukan hanya technical metrics.

**Contoh kasus ceiling effect untuk metrik ini:**
> **Response Time:** Jika baseline >300 detik dan integrated <2 detik, improvement sudah maximal. Solusi: gunakan percentile (p95, p99) atau breakdown by query complexity. **Process Duration:** Jika sudah <1 hari sulit meningkat lebih lanjut. Solusi: measure intermediate stages (registration time, verification time, approval time) sebagai diagnostic metrics.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | Apakah semua data point terkumpul? | ~98% log terekam otomatis; ~70% user respons survey | Reminder otomatis untuk survey; backup manual entry jika log gagal |
| Consistency | Apakah ada kontradiksi internal? | Timestamp harus konsisten (no futuredate); response time >0; satisfaction 1-5 | Validation rules database; alert jika anomali detected |
| Validity | Apakah benar-benar mengukur yang dimaksud? | Response time = query-response latency (valid); satisfaction = SUS-validated questionnaire | Use standardized questionnaire; pilot test dengan 5 user |
| Representativeness | Apakah sampel mewakili populasi target? | N=~2000 jemaah/tahun; coverage: new (30%), returning (70%), peak season (50%) | Stratified sampling; disaggregate by user type; seasonal weighting |

**Pre-registration Checklist:**
  [x] Metrik sudah dipilih SEBELUM eksperimen (pre-registered)
  [x] Primary vs secondary metrik jelas (primary: response time, transparency, efficiency; secondary: satisfaction)
  [x] Threshold kesuksesan terdefinisi (p<0.05, Cohen's d>0.8, 30% improvement minimum)
  [x] Analisis method sudah ditentukan (t-test, Mann-Whitney U untuk ordinal, effect size)
  [x] Data quality control plan ada (validation rules, anomaly detection, stratified sampling)

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> **P-hacking** = memilih metrik SETELAH melihat data untuk membuat hasil signifikan. Contoh: "Response time rata-rata p=0.08 (not sig), tapi p95 p=0.03 (sig) — pilih p95!". Ini meningkatkan false positive rate dan membuat hasil unreplicable.
>
> **Eksplorasi Data Sah** = pre-register primary metrics terlebih dahulu, exploratory metrics dilaporkan terpisah dengan label "exploratory" dan p-value correction applied. Perbedaan kunci:
> - **P-hacking:** Metrik dipilih tanpa pre-registration, p-value disesuaikan untuk signifikan, exploratory dilaporkan sebagai confirmatory
> - **Sah:** Metrik pre-registered sebelum eksperimen, exploratory metrics transparan, p-value correction applied, effect size included
>
> Untuk penelitian ini: Kami pre-register 4 DV metrics + threshold p<0.05 SEBELUM eksperimen. Jika ada insights baru saat analisis (misalnya "response time sensitif pada query type"), dilaporkan sebagai **exploratory finding**, bukan bukti untuk H₁.
