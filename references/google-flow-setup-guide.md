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

### A. Membuat `Visual Base`
Buka menu sebelah kiri -> klik **`Characters`** -> klik **`New Character`**.
Ada 3 cara membangun tampilan dasar:
- **Upload / Approved Image**: Unggah gambar referensi (atau hasil transformasi gaya dari Tahap 2) yang sudah memiliki pencahayaan netral dan wajah tajam.
- **From Scratch (Nano Banana Pro / Nano Banana 2)**: Generate langsung di dalam Flow menggunakan *Locked Identity Block Prompt*.
- **Templates**: Memilih template preset (*"the fantastical"*, dll.) lalu memodifikasi prompt-nya.

### B. Menambahkan `Extra Views` (Wajib untuk Konsistensi Full-Body)
Setelah gambar awal dikunci:
1. Klik opsi untuk men-generate gambar referensi kedua (*Add Extra Views*).
2. Saat Flow meminta deskripsi tubuh dan pakaian (*body and outfit description*), gunakan format spesifik berikut:
   > `[Tinggi/Postur Tubuh] + [Atasan: jenis, warna spesifik, kerah/detail] + [Bawahan: jenis, warna, potongan] + [Sepatu/Alas Kaki] + [Aksesori yang menempel di badan]`
3. Ini memberi model AI pemahaman 360 derajat sehingga ketika kamera mengambil *wide shot* atau *back shot*, pakaian dan proporsi tubuh karakter tidak berubah-ubah.

### C. Mengatur `Voice Profile` (Suara & Lip-Sync)
1. **Preset Voices**: Audisi daftar suara bawaan dan tempelkan ke karakter.
2. **Custom Voices**:
   - Pilih satu *base voice*.
   - Beri nama suara tersebut.
   - Tulis deskripsi karakter vokal (*voice prompt*) yang mencakup **Pitch/Register**, **Pace (Tempo)**, **Texture (Tekstur suara)**, dan **Emotion/Vibe**:
     - *Contoh Karakter Pria Tenang*: `"Warm mid-baritone voice, measured and relaxed pace, clean studio vocal texture with a reassuring, thoughtful tone."`
     - *Contoh Karakter Wanita Enerjik*: `"Bright alto voice, fast-paced and expressive delivery, slightly raspy edge when excited, warm and approachable."`

### D. Mengisi `Character Info` (Untuk Google Flow Agent)
Kolom **Character info** sangat krusial jika kamu menggunakan **Google Flow Agent** untuk *brainstorming* skrip atau menyusun banyak *clip*:
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
