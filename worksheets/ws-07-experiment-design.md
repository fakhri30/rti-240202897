# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question : Apakah penggunaan Google Meet lebih efektif dibandingkan Zoom dalam pembelajaran daring ditinjau dari kemampuan berpikir kritis, kepuasan pengguna, dan kemudahan penggunaan?
Hypothesis        : H₁: Google Meet menghasilkan kemampuan berpikir kritis, kepuasan pengguna, dan kemudahan penggunaan yang lebih tinggi secara signifikan dibandingkan Zoom dalam pembelajaran daring
Tipe Eksperimen   : [x] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control (Eksperimen 1) | Pembelajaran daring menggunakan Google Meet dengan fitur standar | Google Meet | Dataset: 29 mahasiswa kelas IV SD; Materi: Pembelajaran tematik; Durasi: 3 bulan; Metode: Pembelajaran sinkron; Pretest kemampuan berpikir kritis: rata-rata 52.24 |
| Treatment (Eksperimen 2) | Pembelajaran daring menggunakan Zoom dengan fitur standar | Zoom | Dataset: 28 mahasiswa kelas IV SD; Materi: Pembelajaran tematik (identik); Durasi: 3 bulan; Metode: Pembelajaran sinkron; Pretest kemampuan berpikir kritis: rata-rata 52.14 |

Fairness Checklist:
  [x] Dataset identik untuk semua kondisi — Kedua kelompok adalah mahasiswa kelas IV SD dengan karakteristik serupa, jumlah sampel hampir sama (29 vs 28)
  [x] Preprocessing setara — Kedua kelompok mendapat pretest dan posttest yang sama, materi pembelajaran identik
  [x] Tuning effort setara — Kedua aplikasi digunakan dengan fitur standar (gratis), tidak ada optimasi khusus, durasi penggunaan sama (3 bulan)
  [x] Environment identik — Pembelajaran pada kondisi pandemi yang sama, waktu pembelajaran sinkron, koneksi internet dari rumah (real-world condition)
  [x] Metrik evaluasi sama — Kemampuan berpikir kritis (pretest-posttest), kepuasan pengguna (kuesioner Likert 1-7), kemudahan penggunaan (ease of use questionnaire)

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    | Selection bias: Perbedaan karakteristik awal kelompok | Pretest untuk memastikan kemampuan awal setara (52.24 vs 52.14 — hampir identik); random assignment jika memungkinkan |
| Internal    | Maturation effect: Peningkatan karena perkembangan alami siswa | Gunakan gain score (posttest - pretest) untuk analisis; bandingkan improvement rate antar kelompok |
| Internal    | History effect: Kejadian eksternal selama 3 bulan | Dokumentasikan kejadian signifikan; pengukuran simultan untuk kedua kelompok |
| External    | Generalisasi terbatas: Hasil hanya untuk kelas IV SD | Jelaskan batasan generalisasi; replikasi pada sampel berbeda untuk validasi |
| External    | Kondisi internet tidak terkontrol: Kualitas koneksi bervariasi | Survey kualitas koneksi sebagai variabel kontrol; analisis subgroup berdasarkan kualitas koneksi |
| Construct   | Instrumen tes berpikir kritis mungkin tidak komprehensif | Gunakan instrumen tervalidasi (soal HOTS); triangulasi dengan observasi |
| Construct   | Social desirability bias pada kuesioner kepuasan | Kuesioner anonim; kombinasi dengan data objektif (log penggunaan, attendance) |
| Conclusion  | Sample size kecil (N=29, N=28) | Power analysis sebelum penelitian; gunakan effect size untuk interpretasi; pertimbangkan replikasi |
| Conclusion  | Multiple testing: Banyak metrik meningkatkan false positive | Tentukan primary outcome sebelum analisis; koreksi Bonferroni untuk multiple comparisons |

Statistical Plan:
  Uji statistik   : Independent Sample T-Test untuk kemampuan berpikir kritis (data ratio); Mann-Whitney U Test untuk kepuasan pengguna (data ordinal Likert); Descriptive statistics untuk ease of use
  Justifikasi      : T-test cocok untuk membandingkan mean dua kelompok independen dengan data ratio (skor berpikir kritis); Mann-Whitney U untuk data ordinal (Likert scale); kedua kelompok independent dan data pretest menunjukkan distribusi normal
  Alpha            : α = 0.05 (standar akademik untuk signifikansi statistik)
  Effect size min  : Cohen's d > 0.5 (medium effect) untuk perbedaan praktis bermakna; minimum improvement 10% dari baseline untuk relevansi praktis
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Apakah penggunaan Google Meet lebih efektif dibandingkan Zoom dalam pembelajaran daring ditinjau dari kemampuan berpikir kritis, kepuasan pengguna, dan kemudahan penggunaan?
**Tipe eksperimen:** [x] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control (Eksperimen 1) | Pembelajaran daring menggunakan Google Meet | Google Meet | Dataset: 29 mahasiswa kelas IV SD, Materi: Pembelajaran tematik, Durasi: 3 bulan, Metode: Pembelajaran sinkron |
| Treatment (Eksperimen 2) | Pembelajaran daring menggunakan Zoom | Zoom | Dataset: 28 mahasiswa kelas IV SD, Materi: Pembelajaran tematik (sama), Durasi: 3 bulan, Metode: Pembelajaran sinkron (sama) |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✅ | Kedua kelompok menggunakan mahasiswa kelas IV SD dengan karakteristik serupa (usia, tingkat pendidikan sama), jumlah sampel hampir sama (29 vs 28 siswa) |
| Preprocessing setara | ✅ | Kedua kelompok mendapat pretest dan posttest yang sama untuk mengukur kemampuan berpikir kritis, materi pembelajaran identik |
| Tuning effort setara | ✅ | Kedua aplikasi digunakan dengan fitur standar (gratis), tidak ada optimasi khusus pada salah satu platform, durasi penggunaan sama (3 bulan) |
| Environment identik | ✅ | Pembelajaran dilakukan pada kondisi pandemi yang sama, waktu pembelajaran sinkron, koneksi internet dari rumah masing-masing (kondisi real-world) |
| Metrik evaluasi sama | ✅ | Menggunakan metrik yang sama: kemampuan berpikir kritis (pretest-posttest), kepuasan pengguna (kuesioner Likert), kemudahan penggunaan (ease of use questionnaire) |

**Ada yang tidak fair?** [ ] Ya / [x] Tidak
> Desain eksperimen sudah fair karena semua kondisi dikontrol dengan baik. Kedua kelompok mendapat perlakuan yang setara kecuali pada variabel independen (platform yang digunakan).

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | **Selection bias**: Kemungkinan perbedaan karakteristik awal antara kelompok Google Meet dan Zoom | Lakukan pretest untuk memastikan kemampuan awal setara; gunakan random assignment jika memungkinkan; analisis karakteristik demografis kedua kelompok |
| Internal | **Maturation effect**: Peningkatan kemampuan berpikir kritis bisa terjadi karena perkembangan alami siswa selama 3 bulan, bukan karena platform | Gunakan control group atau baseline measurement; bandingkan gain score (posttest - pretest) bukan hanya posttest |
| Internal | **History effect**: Kejadian eksternal selama 3 bulan (misalnya: perubahan kebijakan pembelajaran, kondisi pandemi) yang mempengaruhi hasil | Dokumentasikan kejadian signifikan selama periode penelitian; lakukan pengukuran pada waktu yang sama untuk kedua kelompok |
| External | **Generalisasi terbatas**: Hasil hanya berlaku untuk mahasiswa kelas IV SD, belum tentu untuk jenjang lain atau konteks berbeda | Jelaskan batasan generalisasi dalam laporan; replikasi pada sampel berbeda untuk validasi eksternal |
| External | **Kondisi internet tidak terkontrol**: Kualitas koneksi internet siswa bervariasi yang dapat mempengaruhi pengalaman penggunaan platform | Survey kualitas koneksi internet sebagai variabel kontrol; analisis subgroup berdasarkan kualitas koneksi |
| Construct | **Metrik kemampuan berpikir kritis**: Instrumen tes mungkin tidak sepenuhnya mengukur kemampuan berpikir kritis yang kompleks | Gunakan instrumen tervalidasi (misalnya: soal HOTS); triangulasi dengan metode observasi atau portofolio |
| Construct | **Social desirability bias**: Responden cenderung memberikan jawaban yang dianggap "benar" pada kuesioner kepuasan | Gunakan kuesioner anonim; kombinasikan dengan data objektif (log penggunaan, attendance rate) |
| Conclusion | **Sample size kecil**: N=29 dan N=28 mungkin kurang untuk mendeteksi perbedaan kecil namun bermakna | Hitung power analysis sebelum penelitian; gunakan effect size untuk interpretasi praktis; pertimbangkan replikasi dengan sampel lebih besar |
| Conclusion | **Multiple testing**: Menggunakan banyak metrik (berpikir kritis, kepuasan, kemudahan) meningkatkan risiko false positive | Tentukan primary outcome sebelum analisis; gunakan koreksi Bonferroni atau FDR untuk multiple comparisons |

**Ancaman mana yang paling sulit dimitigasi?** **Kondisi internet tidak terkontrol (External validity)**
**Mengapa?**
> Karena penelitian dilakukan dalam kondisi real-world di masa pandemi dimana siswa belajar dari rumah dengan kualitas internet yang sangat bervariasi. Tidak mungkin mengontrol atau menyeragamkan infrastruktur internet semua siswa. Mitigasi terbaik adalah mengukur dan melaporkan variasi ini sebagai variabel kontrol, serta melakukan analisis sensitivitas untuk melihat apakah hasil tetap konsisten across different internet quality levels. Ancaman ini sebenarnya mencerminkan kondisi nyata penggunaan platform pembelajaran daring, sehingga hasil penelitian lebih ekologis valid meskipun internal validity sedikit berkurang.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. **Apakah perbandingan fair dan kondisi eksperimen identik?** Pertanyaan ini penting untuk memastikan bahwa semua metode diuji pada dataset yang sama, preprocessing yang setara, tuning effort yang sebanding, dan environment yang identik. Misalnya, jika metode baru menggunakan 30 fitur tambahan + Bayesian optimization sementara baseline hanya menggunakan parameter default, maka perbandingan tidak fair dan klaim "mengalahkan" menjadi misleading.

2. **Apa metrik yang digunakan dan apakah metrik tersebut relevan dengan problem domain?** Perlu dipastikan bahwa metrik evaluasi yang dipilih benar-benar mengukur aspek yang penting dalam konteks penelitian. Misalnya, jika metode "mengalahkan" baseline hanya pada accuracy tetapi gagal pada precision/recall (yang lebih penting untuk imbalanced dataset), atau hanya unggul pada satu metrik sementara kalah di metrik lain yang sama pentingnya. Juga perlu dicek apakah ada cherry-picking metrik setelah melihat hasil (p-hacking).

3. **Apakah perbedaan tersebut signifikan secara statistik DAN praktis?** Klaim "mengalahkan" harus didukung dengan uji statistik (p-value < 0.05) untuk memastikan perbedaan bukan karena kebetulan, DAN effect size yang cukup besar (Cohen's d > 0.5) untuk menunjukkan perbedaan bermakna secara praktis. Misalnya, peningkatan accuracy dari 95.2% ke 95.4% mungkin signifikan secara statistik dengan sampel besar, tetapi tidak bermakna secara praktis (hanya 0.2% improvement). Juga perlu dicek apakah ada confidence interval dan apakah hasil konsisten across multiple runs atau hanya satu lucky run.
