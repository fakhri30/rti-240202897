# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

  Contoh config YAML dengan feature toggles:
  ```yaml
  model:
    type: cnn          # IV: ganti "rf" untuk kondisi baseline
  features:
    use_temporal: true  # toggle komponen temporal
    use_normalization: true  # toggle preprocessing
  experiment:
    seed: 42
    runs: 5
  ```
  Dengan pendekatan ini, berbeda kondisi eksperimen = berbeda satu baris config, **tanpa mengubah kode**.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question: Apakah arsitektur sistem terintegrasi (Zachman+GIS+Payment) meningkatkan waktu akses <2 detik, transparansi >80%, efisiensi <1 hari, kepuasan >4/5 dibanding sistem fragmented manual?

Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
| Tipe Arsitektur | IV | Architecture Mode Config (Integrated vs Fragmented/Manual) | Toggle config: arch_mode: "integrated" vs "manual" |
| Response Time | DV | API Server + DB Query Logger | Automated timestamp logging (request - response time) |
| Transparency Score | DV | Status Update Tracker + Push Notification Module | Count: % status updates <1 hour from event log |
| Process Duration | DV | Workflow Engine + Database Timestamp Tracker | Calculate: (completion_timestamp - registration_timestamp) in days |
| User Satisfaction | DV | Post-Interaction Survey Module | Collect via web form: 5-item Likert questionnaire |
| Network Infrastructure | CV | Server Uptime Monitor + Bandwidth Meter | Config: Min bandwidth 10Mbps, uptime >99% |
| User Training | CV | Training Hours Tracker | Config: minimum 40 hours formal training logged |
| Dataset Jemaah | CV | Historical Data Import Module | Config: Load 2000 jemaah/year dari Kemenag Sukabumi |
| Operational Hours | CV | System Clock / Scheduler | Config: Testing weekday 9AM-5PM (work hours) |

4 Prinsip Desain:
  [x] Traceability — Setiap komponen bisa ditelusuri ke variabel
  [x] Variabel Isolation — IV bisa diubah via config tanpa mengubah CV
  [x] Measurement Integration — Pengukuran DV built-in di sistem
  [x] Reproducibility — Setup bisa direkonstruksi dari config YAML

Experimental Setup:
  Input data     : 2000 historical jemaah records dari Kemenag Sukabumi
  Parameter      : arch_mode={integrated|manual}, seed=42, runs=3
  Output format  : CSV logs (response_time_ms, transparency_score, process_duration_days, satisfaction_likert)
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Apakah arsitektur sistem terintegrasi (Zachman+GIS+Payment) meningkatkan akses, transparansi, efisiensi, kepuasan dibanding sistem fragmented manual?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| Tipe Arsitektur | IV | Architecture Mode Config | Ganti config: arch_mode="integrated" atau "fragmented" |
| Response Time | DV | API Gateway + Request-Response Logger | Otomatis capture timestamp; hitung delta_time in milliseconds |
| Transparency Score | DV | Status Update Tracker + Event Stream Module | Count: % permohonan dengan update <1 jam dari database events |
| Process Duration | DV | Workflow State Machine + Timestamp Tracker | Calculate: (completion_date - registration_date) in days |
| User Satisfaction | DV | Survey Form UI Module + Response Collector | Web form post-task; 5-item Likert; submit ke database |
| Network Infrastructure | CV | Uptime Monitor Config | Set threshold: min_bandwidth=10Mbps, uptime=99.5% |
| User Training | CV | Training Log Module | Verify: semua petugas >=40 hours training completed |
| Dataset Jemaah | CV | Historical Data Repository | Config: load_dataset="kemenag_sukabumi_2000" |
| Operational Hours | CV | Scheduler + Clock | Config: testing_window="weekday 9AM-5PM" |

**Apakah semua variabel bisa di-map?** [x] Ya / [ ] Tidak
> Semua variabel berhasil di-map ke komponen fisik atau konfigurasi. IV adalah toggle, DV adalah modules dengan automated logging, CV adalah external parameters.

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | ✅ Terpenuhi | Setiap modul (API Logger, Survey Form, Workflow Tracker) punya label variabel DV yang jelas; IV arch_mode yang explicit |
| Modularity | ✅ Terpenuhi | 6 modul terpisah: APIGateway, Logger, StatusTracker, WorkflowEngine, SurveyForm, DataRepository; dapat diubah independent |
| Controllability | ✅ Terpenuhi | Semua CV (infrastructure, training, dataset, hours) dieksternalisasi ke config YAML; tidak hardcoded di source code |
| Measurability | ✅ Terpenuhi | Semua DV metrics automated collection built-in: response time logger, status update tracker, workflow duration tracker, survey form |

**Prinsip mana yang paling sulit dipenuhi?** **Controllability** (Paling Challenging)
**Strategi untuk mengatasinya:**
> Gunakan dependency injection + config-driven initialization. Infrastruktur seperti bandwidth dijaga dengan monitoring alerts. Training ditrack via audit log. Dataset dipilih awal eksperimen & di-freeze. Operasional hours dijaga via automated scheduler yang prevent testing di luar 9AM-5PM window.

---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki 3 komponen utama, rencanakan ablation study.

Sistem informasi haji terpadu memiliki 3 komponen utama:
- **A = Zachman Enterprise Architecture** (backend modular design)
- **B = GIS + Google Maps API** (travel location mapping)
- **C = Payment Gateway Integration** (payment verification automation)

| Kondisi | Zachman EA | GIS Mapping | Payment Gateway | Hasil yang Diharapkan |
|---------|-----------|-----------|-------------|----------------------|
| Full (A+B+C) | ✅ Modular microservices | ✅ Real-time map + 5 travel locations | ✅ Automated payment verification | Baseline: response_time <2s, transparency 80-100%, process <1d, satisfaction 4-5 |
| – A (Monolithic) | ❌ Monolithic DB query | ✅ Real-time map | ✅ Automated payment | Degradation: response_time >2-5s (modular penalty), transparency 60-70% (no service isolation) |
| – B (No GIS) | ✅ Modular microservices | ❌ Manual location list only | ✅ Automated payment | Minor degradation: response_time same, transparency 75-80% (no geolocation feature), satisfaction -0.5 |
| – C (Manual Payment) | ✅ Modular microservices | ✅ Real-time map | ❌ Manual verification only | Major degradation: response_time same, process_duration >1-2 days (manual bottleneck), satisfaction 3-3.5 (user frustration with payment wait) |

Recommended untuk time-constrained: 4 kondisi dasar (Full, –A, –B, –C) ≈ 4-8 minggu testing. Jika waktu memungkinkan, tambahkan kombinasi ganda: (–A,–B), (–A,–C) untuk 6-7 kondisi total.

**Komponen mana yang diprediksi paling berkontribusi?** **C (Payment Gateway Integration)**
**Mengapa?**
> Payment adalah bottleneck critical di sistem fragmentasi saat ini (>7 hari proses). Integrasi Payment Gateway otomatis = immediate impact pada process_duration metric (KPI utama). Zachman EA (A) penting untuk scalability & maintainability tapi improvement response_time mungkin kurang dramatis (delta dari <2s ke <1s). GIS (B) adalah nice-to-have untuk UX discovery.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> **Risiko Sistem Monolitik untuk Riset:**
> 1. **Variable Isolation Failure:** Jika payment + mapping + authentication semua hardcoded dalam 1 database schema, tidak bisa di-"off" satu komponen tanpa merusak yang lain. Ablation study jadi impossible atau menghasilkan confounded results.
> 2. **Replicability Crisis:** Ketika hasil publikasi, peneliti lain tidak bisa replika hanya dengan ganti config; mereka harus fork codebase dan recompile. Penelitian menjadi non-reproducible.
> 3. **Hidden Confounders:** Tidak jelas mana kontribusi Zachman EA (backend), mana GIS, mana Payment. Klaim "sistem terintegrasi lebih baik" menjadi ambiguous — mana yang benar-benar membuat perbedaan?
> 4. **Measurement Contamination:** Jika logging di-embed dalam bisnis logic (bukan separate logging module), kesalahan di payment logic bisa corrupt response_time data.
> 5. **Time Waste:** Refactoring monolitik ke modular mid-project buang waktu dan biaya.
>
> **Mengapa Modular Architecture Penting untuk Riset:**
> - **Traceability:** RQ → Variable → Component → Metric adalah garis lurus, auditable
> - **Ablation Study:** Komponen bisa di-toggle on/off via config, bukan code change
> - **Pre-registration:** Setup tercatat di config + source code, membuat eksperimen reproducible
> - **Isolation:** Jika DV metrics rusak, terdeteksi cepat di logging module tertentu, tidak spread di seluruh sistem
> - **Scalability:** Kalau hasil publikasi, community bisa extend/replika dengan mengedit config YAML, bukan fork entire repository
>
> **Kesimpulan:** Design sistem untuk penelitian ≠ design untuk user. Research priority: **modularity & traceability**, bukan "fitur lengkap". Engineering priority: **scalability & performance**. Dua mindset berbeda yang perlu balanced dalam DSR (Design Science Research).
