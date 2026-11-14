---
name: google-flow-character
description: Buat karakter AI yang konsisten dari gambar referensi untuk Google Flow (Veo, Nano Banana Pro, Omni Flash, Ingredients, Whisk, & @Character tags), lengkap dengan ekstraksi DNA visual, transformasi gaya visual, prompt character sheet multi-angle, setup profil karakter & suara, serta workflow storyboard video.
---

# Google Flow Character Creator Skill (`google-flow-character`)

Skill ini digunakan ketika pengguna ingin **membuat karakter yang konsisten berdasarkan gambar referensi** untuk digunakan di dalam ekosistem **Google Flow** (menggunakan model seperti *Nano Banana Pro / Nano Banana 2*, *Gemini Omni Flash*, dan *Veo*).

Ketika pengguna memberikan gambar (atau path ke file gambar) dan meminta pembuatan karakter atau workflow Google Flow, ikuti alur kerja terstruktur di bawah ini.

---

## Alur Eksekusi Agent (Step-by-Step)

### Tahap 1: Analisis Gambar & Ekstraksi "Visual DNA" (Identity Lock)
1. **Lihat Gambar Referensi**:
   - Jika pengguna memberikan path file lokal, gunakan tool `view_file` pada gambar tersebut.
   - Jika pengguna melampirkan gambar langsung di chat, amati setiap detail visualnya secara mendalam.
2. **Ekstrak Parameter Identitas secara Presisi**:
   Susun dalam urutan tetap (*Locked Identity Order*) agar model AI di Google Flow tidak mengalami *identity drift*:
   - **Nama Karakter & Tag**: (misal: `@Arka`, `@Lana`)
   - **Rentang Usia & Gender/Kesan Umum**: (misal: *pria sekitar 26 tahun, atletis ramping*)
   - **Struktur Wajah & Kulit**: Bentuk wajah (oval, persegi, hati), warna kulit (*skin tone* spesifik), rahang, tulang pipi.
   - **Mata & Alis**: Bentuk mata, warna iris, ketebalan alis, tatapan khas.
   - **Rambut**: Gaya potongan, panjang, tekstur (lurus, bergelombang, ikal), warna, belahan rambut/poni.
   - **Pakaian Utama (Default Wardrobe)**: Atasan, bawahan, alas kaki, bahan kain, warna spesifik, dan potongan pakaian.
   - **Aksesori & Ciri Khas**: Kacamata, anting, kalung, tahi lalat, bekas luka, tato.
   - **3 Immutable Traits (3 Ciri Mutlak yang Tidak Boleh Berubah)**: Pilih 3 penanda visual paling ikonik dari gambar yang wajib dipertahankan di setiap *shot*.

---

### Tahap 2: Transformasi Gaya Visual (Opsional / Sesuai Permintaan)
Jika gambar referensi berupa foto manusia asli dan pengguna menginginkan gaya visual tertentu (atau sebaliknya), buatkan **Style Transformation Prompt** yang mengunci identitas wajah asli (*Identity Preservation Lock*) sebelum dimasukkan ke Google Flow:
- **Cinematic Photorealism**: Mempertahankan realisme foto asli dengan pencahayaan studio/sinematik netral.
- **3D Pixar / Stylized Animation**: Mengubah foto asli menjadi karakter 3D sekelas film animasi Pixar/Disney dengan proporsi wajah, gaya rambut, dan pakaian yang tetap dikenali 100%.
- **Anime / 2D Cel-Shaded**: Transformasi ke gaya anime modern berkualitas tinggi dengan siluet rambut dan fitur mata yang setia pada referensi.
- **Stylized 3D Game / Toy / Retro (Pixel Machine / Lucid Glass)**: Adaptasi ke estetika fitur kreatif Google Flow.

> Lihat [references/style-transformations.md](references/style-transformations.md) untuk template prompt lengkap setiap gaya visual.
> Jika pengguna meminta kamu langsung membuatkan gambar karakter baru atau *character sheet*-nya sekarang, gunakan tool `generate_image` dengan memasukkan path gambar referensi ke parameter `ImagePaths`.

---

### Tahap 3: Pembuatan Character Sheet & Reference Ingredients
Google Flow membutuhkan referensi visual yang bersih (terutama **1 Close-Up Portrait** dan **1 Full-Body / Multi-Angle Turnaround**) dengan pencahayaan netral agar karakter konsisten di semua *angle*.
Buatkan untuk pengguna:
1. **Locked Identity Block Prompt**: Blok teks pendek dan padat yang wajib ditempel di awal setiap prompt generasi.
2. **Base Portrait Prompt (Close-Up / Medium Shot)**: Untuk mengunci wajah di tab *Characters* Google Flow.
3. **Extra Views / 360° Turnaround Sheet Prompt**: Prompt untuk menghasilkan tampak depan (*front view*), samping (*side profile*), tiga perempat (*3/4 view*), dan belakang (*back view*) dengan pakaian yang sama di latar belakang abu-abu netral (*neutral studio gray background*).

---

### Tahap 4: Konfigurasi Fitur Native Google Flow (`Characters` Tab)
Pandu pengguna (dan sediakan teks siap *copy-paste*) untuk mendaftarkan karakter di menu **Characters -> New Character** pada Google Flow:
1. **Visual Base**: Gunakan gambar hasil Tahap 2/3 atau unggah gambar referensi yang sudah disetujui (*approved reference*).
2. **Extra Views (Body & Outfit Description)**: Teks deskripsi tubuh dan pakaian untuk fitur *second reference image / extra views* di Google Flow.
3. **Voice Profile (Audio Profile)**:
   - Rekomendasi *Preset Voice* atau deskripsi **Custom Voice** (misal: *"suara bariton hangat, tempo bicara tenang dan artikulatif, sedikit serak di akhir kalimat"*).
4. **Character Info (Untuk Google Flow Agent)**:
   - Deskripsi kepribadian dasar (*baseline personality*), *quirks*, bahasa tubuh (*mannerisms*), dan gaya bicara agar **Google Flow Agent** memahami cara karakter berakting saat menulis skrip atau membuat *scene*.

> Lihat [references/google-flow-setup-guide.md](references/google-flow-setup-guide.md) untuk detail mode `@Tags`, `Ingredients`, dan `Whisk`.

---

### Tahap 5: Scene & Video Generation Workflow (Veo / Image-to-Video)
Berikan workflow produksi gambar-ke-video di Google Flow agar wajah dan proporsi tidak berubah (*anti-drift workflow*):
1. **3-Shot Continuity Benchmark Prompts**:
   - **Shot 1 (Face Close-Up & Lip-Sync/Expression)**: Menguji ketajaman wajah dan ekspresi mikro.
   - **Shot 2 (Full-Body Environment Shot)**: Menguji proporsi tubuh dan konsistensi pakaian di lokasi baru.
   - **Shot 3 (Dynamic Action & Camera Movement)**: Menguji pergerakan kamera (misal: *medium tracking shot*) tanpa merusak struktur wajah.
2. **Format Prompt `@Character` di Google Flow**:
   Gunakan formula:
   `@[NamaKarakter] + [Locked Identity Block singkat] + [Aksi Sederhana & Jelas] + [Setting & Pencahayaan] + [Kamera & Lensa] + [Dialog/Audio jika ada]`

---

## Struktur Output yang Harus Diberikan ke Pengguna

Setiap kali skill ini dijalankan untuk sebuah gambar, sajikan hasil dalam format **Google Flow Character Pack** yang rapi:
1. **Ringkasan Visual DNA & 3 Immutable Traits**
2. **Prompt Transformasi Gaya & Turnaround Sheet (Ingredients)** *(Siap Copy-Paste)*
3. **Setup Kartu Karakter Google Flow** (`@Tag`, *Extra Views*, *Custom Voice*, *Character Info*)
4. **Prompt Storyboard & Video Generation (`@Character`)**
5. **Checklist Continuity Control** sebelum *render* video di Veo.

## File Referensi & Alat Bantu di Skill Ini
- [workflows/create-character-from-image.md](workflows/create-character-from-image.md) — Dokumen workflow lengkap dari gambar referensi hingga video akhir di Google Flow.
- [references/style-transformations.md](references/style-transformations.md) — Kumpulan prompt pengunci identitas (*Identity Lock*) untuk berbagai gaya visual.
- [references/google-flow-setup-guide.md](references/google-flow-setup-guide.md) — Panduan teknis fitur `Characters`, `@Tags`, `Ingredients`, `Whisk`, dan `Flow Agent`.
- [templates/character-spec-template.md](templates/character-spec-template.md) — Template lembar kerja spesifikasi karakter (*Character Bible*).
- [scripts/generate_character_pack.py](scripts/generate_character_pack.py) — Script Python CLI untuk men-generate dokumen *Character Pack* dan prompt Google Flow otomatis dari file JSON spesifikasi karakter.
