---
name: brand-promo-storyboard
description: Workflow "Still-First, Video-Second" untuk menggabungkan Karakter (@Nama), Produk Brand, dan Environment ke dalam Storyboard Iklan di Google Flow & Veo tanpa merusak wajah atau label produk.
---

# Workflow: Storyboard Promosi Brand (`@Karakter` + Produk + Environment)

Jangan langsung men-generate video (*Text-to-Video*) dari nol untuk iklan produk karena wajah karakter, bentuk kemasan, dan teks/label brand berisiko tinggi berubah atau meleleh. Gunakan pendekatan **Still-First, Video-Second** di Google Flow.

---

## Persiapan 3 Bahan Utama (*Ingredients*)

1. **Aset Karakter (`@Karakter`)**: Sudah tersimpan di tab `Characters` (dengan `Potret`, `Buat badan` / *3-Panel Turnaround 16:9*, dan `Voice`).
2. **Foto Produk Brand**: 1 foto produk tajam dengan latar polos/bersih agar bentuk dan label terbaca jelas.
3. **Environment (Lokasi)**: 1 foto referensi lokasi atau deskripsi suasana yang konsisten sama di seluruh *shot* (misal: *minimalist sunlit cafe*, *cozy bedroom*, *lakeside wooden deck*).

> **Mode Referensi Terbaik**: Gunakan **`Ingredients` Mode** (gabungkan foto karakter + foto produk + foto environment) atau panggil `@Karakter` sambil melampirkan foto produk sebagai *Ingredient*.

---

## Struktur Storyboard Iklan 4-Shot (~15–20 Detik)

Buat **4 gambar diam (*Approved Still Frames*)** dulu menggunakan **Nano Banana Pro**, cek konsistensi wajah dan label produk di setiap gambar, baru ubah menjadi video di **Veo**.

### Shot 1 — Hook (Pembuka Perhatian, 3–4 detik)
- **Fokus**: Wajah & ekspresi karakter di *environment* (tanpa memegang produk dulu agar wajah terkunci kuat).
- **Prompt Still Image**:
  ```text
  @[NamaKarakter] [Locked Identity Block]. Medium close-up shot at eye level in [deskripsi environment], soft natural morning light, 85mm f/2.8 lens, looking warmly at the camera with a calm gentle smile.
  ```
- **Prompt Video (Image-to-Video Veo)**:
  ```text
  @[NamaKarakter] blinks naturally, smiles softly, and speaks in a calm, gentle, unhurried voice: "[Kalimat Hook 1 kalimat]". Subtle natural breeze in her hair, static eye-level camera.
  ```

### Shot 2 — Product Reveal / Intro (4–5 detik)
- **Fokus**: Karakter memegang produk dengan posisi stabil menghadap kamera.
- **Prompt Still Image** *(lampirkan foto produk di Ingredients)*:
  ```text
  @[NamaKarakter] [Locked Identity Block]. Medium shot in [deskripsi environment]. @[NamaKarakter] holds the attached product cleanly in her hands toward the camera so the packaging and label are sharp and clearly visible. Soft natural lighting, shallow depth of field.
  ```
- **Prompt Video (Image-to-Video Veo)**:
  ```text
  @[NamaKarakter] holds the product steady without rotating it, smiling gently while speaking in a soft, reassuring voice: "[Kalimat pengenalan manfaat produk]". Keep product label completely intact, minimal hand movement.
  ```

### Shot 3 — Lifestyle / Pemakaian Produk (4–5 detik)
- **Fokus**: Suasana nyata saat karakter menikmati/menggunakan produk di *environment* yang sama.
- **Prompt Still Image**:
  ```text
  @[NamaKarakter] [Locked Identity Block]. Medium-wide lifestyle shot seated comfortably in [deskripsi environment], naturally using/enjoying the attached product on a wooden table. Warm natural sunlight, 35mm cinematic lens.
  ```
- **Prompt Video (Image-to-Video Veo)**:
  ```text
  Slow cinematic push-in camera movement. @[NamaKarakter] looks relaxed and satisfied while interacting gently with the product on the table, natural subtle facial expressions, warm ambient light.
  ```

### Shot 4 — Closing & Call-to-Action / CTA (4–5 detik)
- **Fokus**: Penutup hangat + ajakan (*CTA*).
- **Prompt Still Image**:
  ```text
  @[NamaKarakter] [Locked Identity Block]. Medium close-up shot in [deskripsi environment], the attached product placed neatly in foreground/held casually, @[NamaKarakter] looking warmly into the camera.
  ```
- **Prompt Video (Image-to-Video Veo)**:
  ```text
  @[NamaKarakter] smiles warmly at the camera and speaks in a calm, soft, friendly voice: "[Kalimat CTA singkat]". Subtle head tilt, static camera, natural lighting.
  ```

---

## Aturan Anti-Drift untuk Iklan Produk
1. **Jangan suruh karakter memutar atau melempar produk** di Veo—gerakkan kepala/ekspresi karakter secara halus, biarkan posisi produk relatif stabil agar label brand tidak rusak.
2. **Gunakan 1 *Environment* yang konsisten** di keempat *shot* agar terasa seperti satu kali sesi syuting nyata.
3. **Edit/Perbaiki di tahap gambar (*Still*)**: Jika *blush*, pencahayaan, atau bentuk botol kurang pas, perbaiki lewat kotak edit *"Apa yang ingin Anda ubah?"* sebelum masuk ke Veo.
