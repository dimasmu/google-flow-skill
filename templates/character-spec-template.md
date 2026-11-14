# Character Bible & Google Flow Pack: `@[NamaKarakter]`

> **Gambar Referensi Sumber**: `[Path atau nama file gambar referensi]`
> **Target Gaya Visual**: `[Cinematic Photorealism / 3D Pixar / Modern Anime / Stylized 3D]`
> **Model Target di Google Flow**: `Nano Banana Pro` (Stills & Ingredients) + `Veo` (Image-to-Video & Lip-Sync) + `Gemini Omni Flash` (Flow Agent)

---

## 1. Visual DNA (Ekstraksi dari Gambar Referensi)

| Atribut | Deskripsi Terkunci (Locked Specification) |
| :--- | :--- |
| **Nama & Tag Flow** | `@[NamaKarakter]` |
| **Usia & Kesan Umum** | `[Misal: Wanita sekitar 25 tahun, postur ramping proporsional]` |
| **Bentuk Wajah & Skin Tone** | `[Misal: Wajah oval halus, kulit kuning langsat hangat (warm light-olive skin)]` |
| **Mata & Alis** | `[Misal: Mata almond cokelat tua ekspresif, alis melengkung natural rapi]` |
| **Rambut** | `[Misal: Rambut hitam sebahu model bob berlapis (layered bob), poni tipis menyamping ke kanan]` |
| **Pakaian Utama (Look A)** | `[Misal: Kardigan rajut warna terracotta di atas kemeja kerah putih dan celana jeans biru gelap high-waist]` |
| **Alas Kaki** | `[Misal: Sepatu loafers kulit cokelat tua]` |
| **Aksesori Khas** | `[Misal: Anting hoop perak kecil di kedua telinga, jam tangan tali kulit cokelat di tangan kiri]` |

### 3 Immutable Traits (Wajib Ada di Setiap Shot)
1. **`[Ciri Mutlak 1]`**: `[Misal: Potongan rambut bob sebahu dengan poni menyamping ke kanan]`
2. **`[Ciri Mutlak 2]`**: `[Misal: Anting hoop perak kecil]`
3. **`[Ciri Mutlak 3]`**: `[Misal: Kardigan rajut warna terracotta]`

---

## 2. Locked Identity Block (Copy-Paste ke Awal Setiap Prompt)

```text
[NamaKarakter], [usia & gender], [bentuk wajah & skin tone], [mata & alis], [gaya & warna rambut], wearing [pakaian utama & aksesori], [proporsi tubuh]; strictly preserve the exact same face, hairstyle, wardrobe, and body proportions in every scene.
```

---

## 3. Prompt Pembuatan Aset Referensi (Ingredients & Character Sheet)

### A. Prompt Transformasi Gaya / Master Portrait (Visual Base)
```text
Use the uploaded photo as the ONLY identity reference. Preserve the person's facial bone structure, eye shape, skin tone, hairstyle, and signature features ([3 Immutable Traits]) with 100% accuracy. Create a [Target Gaya Visual] chest-up portrait of [Locked Identity Block]. Neutral soft gray studio background, even 5600K studio lighting, sharp focus on eyes, natural expression.
```

### B. Prompt 4-Panel Turnaround Sheet (Untuk Ingredients Mode)
```text
Using the attached portrait as the strict character reference, generate a 4-panel character turnaround sheet on a solid neutral gray background: (1) full-body front view, (2) full-body 3/4 view, (3) full-body side profile view, and (4) close-up facial portrait. Character spec: [Locked Identity Block]. Keep the exact same face, hair, outfit, and proportions across all panels. Flat studio lighting.
```

---

## 4. Konfigurasi Tab `Characters` di Google Flow

- **Character Name**: `[NamaKarakter]` (Dipanggil via `@[NamaKarakter]`)
- **Extra Views (Body & Outfit Prompt)**:
  ```text
  [Deskripsi lengkap postur tubuh dari ujung kepala hingga kaki, warna & tekstur atasan, bawahan, sepatu, dan aksesori untuk fitur Extra Views Google Flow]
  ```
- **Voice Profile (Custom Voice Prompt)**:
  ```text
  [Register suara: alto/soprano/baritone/tenor], [tempo bicara], [tekstur vokal], [emosi dasar & aksen/intonasi]
  ```
- **Character Info (Persona untuk Google Flow Agent)**:
  ```text
  [NamaKarakter] adalah [peran/latar belakang singkat]. Kepribadiannya [3 sifat utama]. Kebiasaan gestur/mannerisms: [kebiasaan gerak wajah/tangan saat bicara atau diam]. Gaya bicara: [cara menyusun kalimat].
  ```

---

## 5. Prompt 3-Shot Continuity Benchmark & Storyboard Video (Veo)

### Shot 1 — Close-Up & Dialog Lip-Sync
```text
@[NamaKarakter] [Locked Identity Block]. Medium close-up shot at eye level in soft natural window lighting. @[NamaKarakter] looks warmly into the camera and speaks naturally with accurate lip synchronization and subtle facial expressions: "[Kalimat dialog uji coba]"
```

### Shot 2 — Full-Body Environment Shot
```text
@[NamaKarakter] [Locked Identity Block]. Full-body wide shot standing in [deskripsi lokasi], [aksi tenang sederhana]. Cinematic 35mm lens, balanced natural lighting, clear view of face and full outfit.
```

### Shot 3 — Dynamic Camera Movement (Tracking Shot)
```text
@[NamaKarakter] [Locked Identity Block]. Medium tracking shot following @[NamaKarakter] walking calmly through [deskripsi lokasi]. Smooth gimbal camera motion, consistent facial structure and hair movement, soft afternoon light.
```
