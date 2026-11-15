# Panduan Teknis Fitur Karakter & Ekosistem Google Flow

Dokumen ini merangkum cara kerja sistem **Characters**, **Avatars**, **Reference Modes (`@Tags`, `Ingredients`, `Whisk`)**, serta **Google Flow Agent** di dalam studio kreatif **Google Flow** (`flow.google.com`).

---

## 1. Memahami Arsitektur Karakter di Google Flow

Di Google Flow, sebuah **Character** bukan sekadar satu gambar referensi, melainkan **entitas bundel (*reusable actor bundle*)** yang menyimpan 4 lapisan memori:
1. **Visual Base (Primary Face & Identity Lock)**: Gambar utama yang mengunci struktur wajah dan estetika visual.
2. **Extra Views (360° Body & Outfit Reference)**: Referensi sudut pandang kedua dan deskripsi tekstual pakaian/proporsi tubuh.
3. **Audio Profile (Voice)**: Suara karakter (*Preset Voice* atau *Custom Voice* berbasis deskripsi akustik) untuk fitur dialog dan *lip-sync* di Veo.
4. **Character Info (Agent Memory)**: Deskripsi kepribadian, sifat, dan gestur yang langsung diumpankan ke **Google Flow Agent** saat menulis naskah atau membuat *storyboard*.

---

## 2. Cara Setup Karakter di Tab `Characters`

### A. Membuat `Visual Base` (Tab `Potret`)
Buka menu sebelah kiri -> klik **`Characters`** -> klik **`New Character`**.
Ada 3 cara membangun tampilan dasar:
- **Upload / Approved Image**: Unggah gambar referensi (atau hasil transformasi gaya) yang sudah memiliki pencahayaan netral dan wajah tajam.
- **From Scratch (Nano Banana Pro / Nano Banana 2)**: Generate langsung di dalam Flow menggunakan *Locked Identity Block Prompt*.
- **Templates**: Memilih template preset lalu memodifikasi prompt-nya.

> **Tips Pembersih Screenshot Video & Edit Cepat:**
> Jika foto awal berasal dari *screenshot* video (agak buram atau ada *subtitle*), masukkan ke tab **`Potret`** lalu minta hapus *subtitle* & *blur*. Jika hasil *Potret* sudah bagus tapi butuh penyesuaian kecil (misal *blush* terlalu merah atau warna kulit kurang natural), gunakan kotak edit **`"Apa yang ingin Anda ubah?"`** di bawah gambar tanpa perlu mengulang dari nol.

### B. Menambahkan `Buat badan` / `Extra Views` (Wajib untuk Konsistensi Full-Body)
Di bawah gambar `Potret`, klik tombol **`Buat badan`** (`Extra Views`):
1. Jika hanya butuh adegan menghadap kamera (*talking head*), 1 gambar badan tampak depan sudah cukup.
2. **Rekomendasi Terbaik (`3-Panel 16:9 Turnaround Sheet`)**: Atur format ke **`16:9` (Landscape)** untuk men-generate 1 gambar berisi **3 sudut sekaligus** (*3/4 front*, *90° side profile*, dan *back view*) di latar abu-abu studio netral (`#D8D8D8`) dari kepala hingga sepatu (*head-to-toe*). Ini mencegah AI mengarang potongan rambut belakang atau alas kaki saat kamera bergerak.
3. Masukkan deskripsi tubuh & pakaian lengkap dengan format:
   > `[Postur & siluet tubuh] + [Atasan: jenis, warna spesifik, detail tali/kerah] + [Bawahan: jenis, warna, potongan] + [Sepatu/Alas Kaki]`

### C. Mengatur `Voice Profile` (Suara & Lip-Sync)
1. **Preset Voices**: Audisi suara bawaan (misalnya preset seperti **`autonoe`** untuk karakter wanita bernada lembut) dan tempelkan ke karakter.
2. **Custom Voices**:
   - Pilih satu *base voice*.
   - Beri nama suara tersebut.
   - Tulis deskripsi karakter vokal (*voice prompt*) yang mencakup **Pitch/Register**, **Pace (Tempo)**, **Texture (Tekstur suara)**, dan **Emotion/Vibe**:
     - *Contoh Wanita Kalem & Lembut*: `"Soft, calm, and gentle young female alto voice. Smooth, airy, and warm vocal texture with a relaxed, unhurried conversational pace, soothing intonation."`
     - *Contoh Pria Tenang*: `"Warm mid-baritone voice, measured and relaxed pace, clean studio vocal texture with a reassuring, thoughtful tone."`

### D. Mengisi `Info karakter (opsional)` (Untuk Google Flow Agent)
Kolom **Info karakter** sangat krusial jika kamu menggunakan **Google Flow Agent** untuk *brainstorming* skrip atau menyusun banyak *clip*:
- Tuliskan dalam 3-4 kalimat:
  1. **Peran & Kepribadian Utama**: (misal: *"Detektif swasta yang skeptis namun berempati tinggi."*)
  2. **Bahasa Tubuh / Mannerisms**: (misal: *"Sering membetulkan letak kacamatanya saat berpikir dan jarang tersenyum lebar."*)
  3. **Gaya Bicara**: (misal: *"Bicara singkat, to-the-point, menggunakan kalimat pendek."*)

---

## 3. Menggunakan Personal Avatar (`@me`)

Jika kamu ingin menggunakan wajah dan suara aslimu sendiri:
1. Buka **Account Settings** di desktop -> klik **`Create avatar`**.
2. Scan QR code dengan aplikasi **Gemini** di ponsel.
3. Rekam video selfie pendek (mengikuti panduan sudut wajah) dan bacakan deretan angka untuk merekam profil suaramu.
4. Panggil di prompt cukup dengan mengetik **`@me`**.
> **Catatan Privasi**: Avatar `@me` dikunci khusus untuk akun pribadimu dan tidak bisa dibagikan ke publik atau lewat *Flow Tools*.

---

## 4. Tiga Mode Referensi di Google Flow (`@Tags` vs `Ingredients` vs `Whisk`)

Saat men-generate gambar atau video di Google Flow (atau menggunakan *Flow Automator*), terdapat 3 metode pemanggilan referensi:

### 1. Mode `@Tags` (`@NamaKarakter`)
- **Cara Kerja**: Ketik simbol `@` diikuti nama karakter (contoh: `@Lana sedang berjalan di pasar malam bersama @Bima`).
- **Kelebihan**: Sangat fleksibel. Meskipun wajah karakter terkunci, kamu tetap bisa menyuruh AI mengganti pakaian mereka di prompt (misal: `@Lana mengenakan jas hujan kuning`), menempatkan mereka di lokasi baru, atau melakukan aksi baru.
- **Kapan Dipakai**: Saat membuat *multi-character scene* atau ketika setiap prompt membutuhkan kombinasi aktor yang berbeda.

### 2. Mode `Ingredients`
- **Cara Kerja**: Memilih sekumpulan gambar referensi (misal: 1 foto wajah *close-up*, 1 foto *full-body* dengan pakaian yang sama, dan 1 foto latar ruangan) yang diterapkan secara seragam ke seluruh prompt.
- **Aturan Emas Ingredients**:
  - Gunakan **1 portrait jelas** + **1 full-body image** dengan pakaian yang sama.
  - Jangan memasukkan terlalu banyak gambar referensi dengan pencahayaan yang saling bertabrakan karena model akan mencampur (*blend*) ciri-ciri tersebut secara tidak stabil.
  - Gunakan set *Ingredients* yang sama untuk kelompok *shot* yang berdekatan (*adjacent shot groups*).

### 3. Mode `Whisk`
- **Cara Kerja**: Mengorganisir gambar referensi ke dalam 3 slot kategori terpisah:
  - **Subject**: Gambar referensi karaktermu.
  - **Scene**: Gambar referensi lokasi/interior/eksterior.
  - **Style**: Gambar referensi estetika visual, palet warna, atau *grading* sinematik.
- **Kapan Dipakai**: Saat ingin menjaga karakter tetap sama tetapi bereksperimen dengan atmosfer lokasi dan *color grading* yang sangat spesifik dari gambar referensi lain.

---

## 5. Lima Fitur Kreatif Tambahan (Google Flow Tools)

Manfaatkan *Flow Tools* terbaru untuk memperkaya karaktermu:
1. **Character Poster**: Membuat poster visual bergaya konsisten untuk memperkenalkan karakter utama.
2. **Character Arc**: Melacak dan menjaga konsistensi perkembangan karakter lintas waktu/dekade (misal: karakter bertambah tua atau berganti era cerita tanpa kehilangan struktur wajah dasar).
3. **Pixel Machine**: Menerapkan estetika digital retro pada karakter/adegan.
4. **Lucid Glass**: Mensimulasikan efek pembiasan cahaya (*light refractions*) dan optik sinematik di sekitar karakter.
5. **Pocket Studio**: Mengubah rekaman video HP menjadi berbagai sudut kamera sinematik (*multi-angle shots*) dari satu *take*.

---

## 6. Mengatasi Masalah Umum (Troubleshooting Drift)

| Masalah yang Muncul | Penyebab Utama | Solusi di Google Flow |
| :--- | :--- | :--- |
| **Wajah berubah saat *wide shot*** | Tidak ada referensi *full-body* atau *Extra Views* belum diisi. | Tambahkan referensi *full-body* di *Extra Views* & generate gambar *still* dulu sebelum diubah ke video Veo. |
| **Karakter memakai pakaian campuran** | Gambar referensi di *Ingredients* memiliki 2 baju berbeda. | Pisahkan setiap *outfit* menjadi *reference sheet* tersendiri (Look A vs Look B). |
| **Gerakan mata/mulut aneh saat bicara** | Prompt menggabungkan gerakan kamera ekstrem + aksi fisik rumit + dialog panjang. | Gunakan *medium close-up* dengan gerakan kamera tenang (*static* atau *slow push-in*) khusus untuk *shot* dialog *lip-sync*. |
| **Wajah perlahan bergeser setelah banyak video** | Konteks sesi terlalu panjang atau menggunakan *frame* terakhir yang sudah mengalami *drift*. | Mulai sesi baru untuk setiap *scene* utama dan selalu gunakan **Approved Master Reference** asli, bukan hasil generasi ke-5. |
