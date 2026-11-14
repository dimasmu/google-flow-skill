# Panduan & Prompt Transformasi Gaya Visual (Identity-Locked Style Transfer)

Dokumen ini berisi kumpulan template prompt untuk mengubah **gambar referensi asli** (foto wajah manusia, sketsa, atau potret awal) menjadi berbagai gaya visual tanpa kehilangan identitas wajah (*100% Identity Preservation*) sebelum didaftarkan sebagai **Visual Base** atau **Ingredients** di **Google Flow**.

---

## Prinsip Utama: "Identity Preservation Lock"

Saat mengubah gaya visual (misalnya dari foto asli ke 3D Pixar atau Anime), model AI sering kali "mempercantik" atau menyeragamkan wajah sehingga ciri khas asli hilang. Untuk mencegahnya, setiap prompt transformasi wajib menyertakan **3 Komponen Pengunci**:
1. **Instruksi Referensi Tunggal**: *"Use the uploaded photo as the ONLY identity reference."*
2. **Daftar Larangan Perubahan (*Do Not Alter*)**: *"Do not change the face shape, hairstyle, hairline, skin tone, eye shape, eyebrow thickness, nose bridge, glasses, or distinctive facial features."*
3. **Deskripsi eksplisit 3 Immutable Traits**: Menyebutkan kembali 3 ciri paling khas dari foto asli di dalam teks prompt.

---

## 1. Transformasi ke 3D Pixar / Disney Animation Style

Cocok untuk cerita animasi pendek, konten edukasi berkarakter, atau maskot naratif di Google Flow.

### A. Prompt Karakter 3D Tunggal (Siap Jadi Visual Base Google Flow)
```text
Use the uploaded photo as the ONLY identity reference. Preserve the person's identity, facial structure, skin tone, hairstyle, eye shape, eyebrows, body proportions, age, and distinctive features ([sebutkan 3 ciri khas, misal: kacamata bulat hitam, lesung pipi kanan, jaket denim]). Transform this exact person into a high-end Pixar-quality 3D animated character. The animated character must clearly be recognizable as the exact same individual. Wearing [deskripsi pakaian]. Neutral studio gray background, soft three-point studio lighting, subsurface skin scattering, expressive eyes, 8k render quality.
```

### B. Prompt "Pixar Mirror" (Validasi Kemiripan Berdampingan)
Gunakan prompt ini jika ingin mengecek apakah versi 3D sudah benar-benar mirip dengan orang aslinya dalam satu frame:
```text
Use the uploaded photo as the ONLY identity and location reference. Preserve the person's identity and the original scene exactly. Do not change the face, hairstyle, skin tone, body proportions, age, ethnicity, glasses, or distinctive features. Create a photorealistic image of the real person sitting beside a Pixar-quality 3D animated version of themselves wearing the exact same outfit. Both must clearly look like the same individual.
```

---

## 2. Transformasi ke Cinematic Photorealism (Studio Master Portrait)

Cocok ketika foto referensi awal diambil menggunakan kamera HP dengan pencahayaan kurang bagus (misal: *backlight*, agak buram, atau warna lampu kamar kuning pekat) dan kamu butuh **Visual Base** yang bersih dan sinematik untuk Nano Banana Pro / Veo.

```text
Use the uploaded photo as the ONLY facial identity reference. Preserve the exact facial bone structure, eye shape, nose, lips, skin tone, hairstyle, and distinctive traits ([sebutkan 3 ciri khas]) with 100% fidelity. Generate a clean, high-resolution cinematic studio portrait of this exact person from chest up, facing the camera with a calm natural expression. Wearing [deskripsi pakaian]. Neutral soft gray background, balanced 5600K daylight studio lighting, shot on 85mm f/2.8 lens, natural skin texture, zero distortion.
```

---

## 3. Transformasi ke Modern Anime / 2D Cel-Shaded (Makoto Shinkai / Kyoto Animation Style)

Cocok untuk proyek *micro-drama* anime, visual novel, atau MV animasi di Google Flow.

```text
Use the uploaded photo as the ONLY identity reference. Translate this exact person into a high-budget modern Japanese anime character (Makoto Shinkai and Kyoto Animation visual quality) while strictly preserving their recognizable identity: keep the exact hairstyle and hair parting, eye color and shape, eyebrow thickness, skin tone, accessories, and outfit ([sebutkan pakaian & 3 ciri khas]). Clean cel-shaded line art, detailed anime eye highlights, standing against a clean neutral gray reference background, even studio lighting.
```

---

## 4. Transformasi ke Stylized 3D Game / Arcane Painterly Style

Cocok untuk cerita aksi, sci-fi, atau fantasi dengan tekstur *hand-painted* yang kuat.

```text
Use the uploaded image as the strict facial and character reference. Keep the exact facial geometry, hairstyle, skin tone, and signature features ([sebutkan 3 ciri khas]). Render this exact character in a stylized hand-painted 3D art style inspired by Arcane (Fortiche studio), featuring expressive brushwork textures on skin and fabric, sharp chiselled rim lighting, wearing [deskripsi pakaian]. Clean dark neutral background for character sheet clarity.
```

---

## 5. Transformasi ke Claymation / Stop-Motion Vinyl Figure (Aardman / Laika Style)

Cocok untuk video cerita unik, iklan kreatif, atau cerita komedi pendek.

```text
Use the uploaded photo as the ONLY character identity reference. Transform this exact person into a handcrafted stop-motion claymation miniature figure (Laika Studios quality). Preserve their exact hairstyle, facial proportions, skin tone, glasses/accessories, and outfit ([sebutkan pakaian & 3 ciri khas]) so they remain immediately recognizable. Subtle tactile fingerprint textures on polymer clay, miniature studio lighting, clean neutral backdrop.
```

---

## 6. Prompt Turnaround Sheet (Dari 1 Gambar ke Multi-Angle Reference Set)

Setelah kamu mendapatkan **1 Gambar Base** (baik realistis maupun yang sudah ditransformasi gayanya), gunakan prompt ini dengan melampirkan Gambar Base tersebut untuk membuat **Turnaround Sheet** (bahan utama *Ingredients Mode* dan *Extra Views* di Google Flow):

```text
Using the attached image as the strict character reference, create a 4-panel character turnaround reference sheet on a clean neutral studio gray background (#D8D8D8).
Panel 1 (Left): Full-body front view standing in a relaxed neutral A-pose.
Panel 2 (Center-Left): Full-body 3/4 angled view.
Panel 3 (Center-Right): Full-body side profile view (90 degrees).
Panel 4 (Right): Close-up portrait of the face with a warm subtle smile.
Strictly preserve the exact face, hairstyle, skin tone, body proportions, height, and outfit ([tempel Locked Identity Block]) across every panel. Flat, even studio lighting with no dramatic shadows.
```
