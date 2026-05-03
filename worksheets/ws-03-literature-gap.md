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

Topik      : Sistem Informasi Layanan Haji — E-Government & Enterprise Architecture
Database   : ResearchGate, Google Scholar, Institutional Repository, DOI/Jurnal Online
Query      : ("Sistem Informasi Haji" OR "Hajj Information System") AND ("Zachman" OR "framework" OR "architecture") AND ("Kementerian" OR "Layanan Publik" OR "KBIH")
Tahun      : 2011-2026 (15 tahun evolusi teknologi haji IS)
Hasil awal : 5+ paper → Screening by relevance & quality → 5 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| SISKOHAT Effectiveness | 2015 | Qualitative Descriptive | Jawa Tengah; 17 BPS BPIH integrated; waiting list 19-20 tahun | Sangat efektif: integrasi 17 BPS, fitur lengkap (registrasi, visa, payment, manifest, monitoring), mengatasi waiting list masif | Hanya Jawa Tengah; tanpa metrik kuantitatif; tanpa kepuasan jamaah terukur |
| Zachman Hajj Architecture | 2026 | Zachman Framework + EA Design | Kementerian Haji Sukabumi; E-Gov; akses 24/7 requirement | Pemetaan arsitektur lengkap (planning, requirements, design, technical); ERD + service strategy; design untuk transparansi & accessibility | Masih design phase; scope lokal Sukabumi; tanpa empirical validation |
| Web Haji System KBIH | 2011 | Web-Based Development | KBIH Ar Rohman Mabrur Kudus; manual → online registration | Aplikasi web registrasi & informasi haji; akses 24/7; prosedur & aturan haji online | Single KBIH; tahun 2011 (lama); tanpa testing data; scope terbatas |
| McCall Quality SIHAT | 2022 | McCall Quality Model + Survey | SIHAT Arraudhah Wisata Imani; 30 responden | Overall quality 41% (sufficient); Correctness 58%, Reliability 30%, Efficiency 19% | Reliability & efficiency rendah; sample kecil; satu penyedia; tanpa rekomendasi improvement |
| Waterfall Registration | 2024 | Waterfall + CodeIgniter + MySQL | KBIH Ibnu Aqil Bogor; manual → online registration | Design sistem registrasi online, informasi jadwal/biaya, automated reporting | Design phase only; single KBIH; tanpa security/privacy analysis |

Pola yang ditemukan:
  Metode dominan     : Web-based system design (3/5 paper); Enterprise Architecture Zachman (terbaru 2026); Quality assessment McCall (2022)
  Dataset umum       : Hajj service domain; case studies lokal (Jawa Tengah, Sukabumi, Kudus, Bogor); organisasi publik lokal (Kemenag, KBIH)
  Limitasi berulang  : (1) 80% design-only; (2) Metrik operasional tidak konkret; (3) Local scope, no replication model; (4) Limited validation; (5) Quality concerns (SIHAT 41%, efficiency 19%)

GAP IDENTIFICATION

Gap 1: [Jenis: Implementation + Context]
  Deskripsi    : Zachman Framework ada di level design (Bahar 2026), tapi belum ada dokumentasi implementasi nyata dengan operational metrics terukur di local government Sukabumi
  Bukti        : Query sistematis 2015-2026: Bahar (2026) design-only; Fahrudin (2011) & Mustaqim (2024) design-only. Hanya SISKOHAT (2015) operational tapi tanpa framework formal & tanpa metrik operasional (response time, uptime %, transparency score)
  Signifikansi : Indonesia 34 provinsi + 300+ kabupaten. Metodologi proven di Sukabumi dapat direplika nasional. Tanpa dokumentasi implementasi dengan operational metrics, adopsi lambat karena ROI tidak terbukti

Gap 2: [Jenis: Method + Performance]
  Deskripsi    : Metrik operasional untuk "transparansi" & "akses 24/7" belum teroperasional. Paper menyebutkan goals ini tapi tanpa KPI konkret (response time, uptime, satisfaction score, transparency index dengan target numerik)
  Bukti        : Bahar 2026 menyebutkan "transparansi diharapkan meningkat" tanpa target %; McCall 2022 hanya score 41% overall tanpa transparency-specific; Munawaroh 2015 tidak ada metric
  Signifikansi : Tanpa metrik operasional yang jelas & terukur, implementasi EA sulit dievaluasi, sulit direplikasi, & sulit dibuktikan ROI-nya kepada stakeholder publik

Gap 3: [Jenis: Data]
  Deskripsi    : Sangat sedikit data baseline kondisi SEBELUM digitalisasi. Mayoritas paper fokus pada solusi tanpa mengukur current state (waiting time, satisfaction, process cost, transparency baseline)
  Bukti        : Paper 2024, 2026 tidak ada baseline data; Paper 2015 menyebutkan waiting list 19-20 tahun tapi tidak detail metrik lain; Paper 2011, 2022 tidak dokumentasikan baseline
  Signifikansi : Tanpa baseline terukur, improvement claims tidak dapat divalidasi. Crucial untuk ROI analysis & justifikasi budget investasi IS. Penting untuk menunjukkan "before-after" benefit

Baseline Selection:
| Baseline | Relevansi | Representatif | SOTA? | Source |
|----------|-----------|---------------|--------|--------|
| SISKOHAT 2015 (Qualitative + 17 BPS BPIH Integrated) | Implementasi nyata hajj IS; proven effectiveness; skala besar (17 BPS nasional) | Mewakili integrated govt system baseline — apa yang bisa dicapai: fitur lengkap (registrasi, visa, payment, manifest, monitoring) di production | Bukan SOTA framework-wise (kualitatif 2015), tapi PROVEN EFFECTIVE in large-scale hajj operation Indonesia | Munawaroh et al. 2015 |
| Zachman Framework 2026 (EA Design + Systematic Mapping) | Framework sistematis enterprise architecture; fokus transparansi & accessibility (24/7); terbaru & relevan untuk public e-services | Mewakili modern EA approach — best practice systematic architecture design (planning → requirements → design → technical model) | SOTA untuk EA framework (Zachman masih industry standard 2024-2026 untuk e-government) | Bahar & Saepudin 2026 |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan database akademik.

> **Panduan pencarian:**
> - Database: IEEE Xplore, ACM DL, Google Scholar, atau ResearchGate
> - Tulis query Boolean yang digunakan: contoh `("object detection" OR "image classification") AND ("edge computing") NOT ("medical")`. Dokumentasikan query secara eksplisit.
> - Akses gratis: buka Google Scholar → cari judul paper → klik [PDF] jika tersedia, atau akses lewat campus VPN

**Topik riset:** Desain Arsitektur Sistem Informasi Layanan Haji menggunakan Enterprise Architecture (Zachman Framework) untuk Transparansi & Akses Informasi 24/7
**Query pencarian:** ("Sistem Informasi Haji" OR "Hajj Information System") AND ("Zachman" OR "framework" OR "architecture" OR "web") AND ("Kementerian" OR "Layanan Publik" OR "KBIH")
**Database:** ResearchGate, Google Scholar, Institutional Repository Universitas, DOI/Jurnal Online

| # | Study | Tahun | Method | Dataset/Context | Result | Limitasi |
|---|-------|-------|--------|-----------------|--------|----------|
| 1 | Munawaroh et al. "Efektivitas SISKOHAT dalam Penyelenggaraan Ibadah Haji" | 2015 | Qualitative Descriptive | Kanwil Kemenag Jawa Tengah; 17 BPS BPIH integrated | SISKOHAT sangat efektif: integrasi 17 BPS BPIH, fitur lengkap (registrasi, visa, payment, manifest, monitoring), mengatasi waiting list 19-20 tahun | Hanya Jawa Tengah; tanpa metrik kuantitatif; tanpa kepuasan jamaah terukur |
| 2 | Bahar & Saepudin "Aplikasi Web Informasi Layanan Haji... Zachman Framework" | 2026 | Zachman Enterprise Architecture Framework + System Design | Kementerian Haji & Umrah Sukabumi; E-Government; akses 24/7 | Pemetaan arsitektur Zachman lengkap (planning, business requirements, system design, technical model); design untuk transparansi & accessibility online | Masih design phase (belum implementasi); scope lokal Sukabumi; tanpa empirical validation |
| 3 | Fahrudin et al. "Pembangunan Sistem Informasi Layanan Haji Berbasis Web... KBIH" | 2011 | Web-Based System Development + System Design | KBIH Ar Rohman Mabrur Kudus; manual process → online registration | Aplikasi web untuk registrasi & informasi haji; mudah diakses 24/7; prosedur & aturan haji tersedia online | Single KBIH only; tahun 2011 (teknologi lama); tanpa system testing data |
| 4 | Farisi et al. "Analisis Kualitas Sistem Informasi Haji Terpadu (SIHAT)... McCall Model" | 2022 | McCall Software Quality Model + Survey Questionnaire | SIHAT PT. Arraudhah Wisata Imani; 30 responden; Quality measurement | Overall quality 41% (sufficient); Correctness 58%, Reliability 30%, Efficiency 19% | Reliability & efficiency sangat rendah (30%, 19%); sample kecil (30 responden); satu penyedia haji saja |
| 5 | Mustaqim & Prayitno "Perancangan Sistem Informasi Pendaftaran Haji & Umrah... Waterfall" | 2024 | Waterfall Software Development; CodeIgniter + MySQL; Interview & Observation | KBIH Ibnu Aqil Agus Salim Bogor; manual registration → online system; reporting automation | Design sistem registrasi online, informasi jadwal/biaya, automated reporting; expected to improve efficiency | Design phase only (bukan implementasi); single KBIH; tanpa security/privacy analysis |

**Pola yang terlihat — Metode dominan:** Web-based system (3/5 paper) + Enterprise Architecture Zachman (2026, terbaru) + Quality Assessment McCall (2022). SISKOHAT (2015) baseline proven operational nasional.
**Limitasi yang berulang:** (1) 80% masih design-only; (2) Metrik operasional transparansi/efficiency tidak konkret; (3) Local scope, no replication model; (4) Limited validation (UAT, long-term monitoring); (5) Quality concerns (SIHAT 41% overall, efficiency 19%)

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [X] Ya / [ ] Tidak | McCall study (2022) menunjukkan SIHAT hanya 41% quality; Efficiency 19% sangat rendah. SISKOHAT (2015) proven effective tapi tanpa metrik operasional. **Gap: implementasi EA Zachman belum memiliki proven performance metrics (response time, uptime, transparency index) di production** |
| Method Gap | [X] Ya / [ ] Tidak | Zachman Framework ada (Paper 2, 2026), tapi **belum ada metodologi operasional yang mengintegrasikan: (1) Architecture design, (2) Quality metrics, (3) User satisfaction, (4) Implementation roadmap** dalam satu framework terstruktur untuk hajj service |
| Data Gap | [X] Ya / [ ] Tidak | **Sangat sedikit data baseline kondisi SEBELUM digitalisasi**. Paper fokus pada solusi tapi tidak dokumentasikan: waiting time baseline, current satisfaction, current process cost, current transparency level. Krusial untuk measuring improvement |
| Context Gap | [X] Ya / [ ] Tidak | Implementasi EA (Zachman) ada di negara maju, ada di hajj service Indonesia (SISKOHAT), tapi **belum ada adaptasi systematik untuk Kementerian Haji lokal dengan resource constraints Sukabumi** dengan operasional metrics jelas |

**Gap utama yang dipilih:** Kombinasi Method Gap + Context Gap + Performance Gap
- **Fokus:** Metodologi operasional untuk implementasi Zachman Framework di Kementerian Haji Sukabumi yang menghasilkan sistem dengan performance metrics terukur (response time <5s, uptime >99%, transparency score 80+, user satisfaction >4/5)

**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> SISKOHAT (2015) buktikan hajj IS dapat berfungsi nasional & effective; Zachman Framework (2026) mapping tersedia untuk Sukabumi; McCall (2022) tunjukkan quality gaps. **GAP INI PENTING KARENA:** (1) Indonesia punya 34 provinsi + 300+ kabupaten — metodologi proven di Sukabumi bisa direplika ke seluruh Kemenag lokal; (2) Layanan haji prioritas nasional (jutaan jamaah/tahun) — improvement transparansi & akses berdampak ekonomi & kepuasan sosial; (3) SIHAT hanya 41% quality (efficiency 19%) — perbaikan metodologi berbasis Zachman dapat meningkatkan kualitas sistematis; (4) Belum ada dokumentasi cara meng-operasionalkan Zachman Framework dengan KPI konkret (response time, transparency index, satisfaction score) di public sector lokal dengan budget terbatas. Tanpa ini, Kepala Daerah/Menag lokal enggan adopt karena ROI tidak terbukti.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | **SISKOHAT 2015 (Qualitative Descriptive + Integrated 17 BPS BPIH)** | Implementasi nyata hajj IS di Kemenag; proven effectiveness mengatasi waiting list 19-20 tahun; skala besar (17 BPS terintegrasi) | **Representatif untuk integrated govt system baseline** — menunjukkan apa yang bisa dicapai: fitur lengkap (registrasi, visa, payment, manifest, health monitoring, flight monitoring) | Bukan SOTA framework-wise (method kualitatif, 2015), tapi **PROVEN EFFECTIVE in large-scale hajj operation** di Indonesia | Munawaroh et al. 2015 |
| 2 | **Zachman Framework 2026 (EA Design + Systematic Mapping + Service Strategy)** | Framework sistematis enterprise architecture; fokus transparansi & accessibility (24/7); terbaru & relevan untuk public e-services | **Representatif untuk modern EA approach** — mewakili best practice systematic architecture design (planning → business requirements → system design → technical model) | **SOTA untuk EA framework** (Zachman masih industry standard 2024-2026 untuk e-government) | Bahar & Saepudin 2026 |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [X] Tidak
> Justifikasi: **Bukan straw man — kedua baseline complementary & rigorous:** (1) SISKOHAT 2015 = proof-of-concept bahwa hajj IS work di Indonesia skala besar, tapi tanpa framework sistematis & tanpa metrik operasional konkret; (2) Zachman 2026 = methodology sistematis untuk design architecture tapi belum terbukti implementable dengan metrik operasional yang jelas. **Penelitian ini akan:** Implementasi Zachman Framework (baseline 2) dengan metodologi operasional (KPI konkret) yang validated pada case SISKOHAT (baseline 1). Hasilnya: proven-in-practice Zachman methodology untuk hajj IS di local government context. Ini adalah **evolution of baselines**, bukan pengecilan artificial untuk membuat method sendiri terlihat baik.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**

**"Belum ada yang meneliti ini" (klaim tanpa bukti):** Pernyataan vague tanpa dokumentasi pencarian. Contoh: "Belum ada yang menerapkan Zachman di Indonesia" — tanpa query Boolean, database mana yang dicari, atau paper apa yang sudah direview. Ini **tidak sah akademis** karena tidak dapat diverifikasi.

**Research gap yang valid:** Pernyataan spesifik didukung bukti literatur sistematis. Contoh: "Dari query Boolean ('Zachman' OR 'EA') AND ('e-government') AND ('Indonesia') di Google Scholar, IEEE, Scopus (2015-2025), ditemukan 0 paper tentang implementasi Zachman di local government Sukabumi dengan operational metrics. Sebaliknya, di level nasional ada SISKOHAT (2015) dan di level design ada Bahar 2026. Gap: **metodologi operasional untuk implementasi EA dengan KPI konkret di local government belum terdokumentasi**."

**Cara membuktikan gap benar-benar ada:**
1. **Pencarian sistematis terdokumentasi:** Query Boolean spesifik, database yang digunakan, rentang tahun, jumlah hasil & hasil filter
2. **Backward & Forward snowballing:** Lacak referensi paper kunci; cari paper yang mengutip paper kunci (Google Scholar "Cited by")
3. **Analisis pola literatur:** Tabel concept-centric yang membandingkan metode, dataset, konteks di setiap paper. Pola yang berulang menunjukkan limitasi umum
4. **Kontrastif (bukan negatif):** Jangan hanya bilang "belum ada," tetapi "ada di konteks X, tetapi tidak di konteks Y yang relevan dengan riset ini"
5. **Signifikansi & Impact:** Jelaskan **mengapa** gap ini penting — dampaknya bagi teori, praktik, atau masyarakat. Contoh: "Indonesia 34 provinsi × 300+ kabupaten — metodologi proven di Sukabumi bisa direplika nasional"

**Contoh dari WS-03 Anda:**
- **Klaim tanpa bukti:** "Belum ada yang meneliti Zachman untuk haji di Indonesia"
- **Gap yang valid:** "Ada SISKOHAT (2015) proven effective tapi tanpa framework formal; ada Zachman mapping (2026) tapi design-only; ada McCall quality assessment (2022) tapi 41% score. **Gap: metodologi operasional yang mengintegrasikan systematic design (Zachman) + quality metrics (KPI operasional) + proven implementation dalam 1 framework untuk local government hajj service belum ada**. Ini penting karena Indonesia punya 300+ kabupaten dengan kebutuhan serupa — perlu metodologi yang replicable & measurable untuk adopt EA di public sector lokal."
