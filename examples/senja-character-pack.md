# Google Flow Character Pack: `@Senja` (Senja)

- **Source Reference Image**: `reference_photo.jpg`
- **Target Visual Style**: `3D Pixar-quality animated character`
- **Google Flow Tag**: `@Senja`

---

## 1. Visual DNA & 3 Immutable Traits

| Komponen Identitas | Spesifikasi Terkunci (Locked Spec) |
| :--- | :--- |
| **Nama & Tag** | **Senja** (`@Senja`) |
| **Usia & Karakteristik** | young woman around 24 years old |
| **Wajah & Skin Tone** | soft heart-shaped face, warm light-tan skin tone, subtle freckles across nose bridge |
| **Mata & Alis** | large expressive dark brown almond eyes, neat natural arched eyebrows |
| **Rambut** | shoulder-length wavy chestnut-black hair with wispy curtain bangs |
| **Pakaian Utama (Default Wardrobe)** | mustard-yellow oversized corduroy jacket over a striped navy-and-white crew-neck tee, dark blue rolled-up denim jeans, and white canvas high-top sneakers |
| **Aksesori Khas** | round tortoiseshell eyeglasses and a small silver crescent moon pendant necklace |
| **Proporsi Tubuh** | slender medium build, 165cm height, relaxed posture |

### 3 Immutable Traits (Wajib Dipertahankan di Semua Shot)
1. **round tortoiseshell eyeglasses**
2. **shoulder-length wavy chestnut-black hair with curtain bangs**
3. **mustard-yellow oversized corduroy jacket**

---

## 2. Locked Identity Block (Tempel di Awal Setiap Prompt)

```text
Senja, young woman around 24 years old, soft heart-shaped face, warm light-tan skin tone, subtle freckles across nose bridge, large expressive dark brown almond eyes, neat natural arched eyebrows, shoulder-length wavy chestnut-black hair with wispy curtain bangs, wearing mustard-yellow oversized corduroy jacket over a striped navy-and-white crew-neck tee, dark blue rolled-up denim jeans, and white canvas high-top sneakers, with round tortoiseshell eyeglasses and a small silver crescent moon pendant necklace, slender medium build, 165cm height, relaxed posture; strictly preserve the exact same face, hairstyle, wardrobe, body proportions, and signature traits (round tortoiseshell eyeglasses, shoulder-length wavy chestnut-black hair with curtain bangs, mustard-yellow oversized corduroy jacket) in every scene.
```

---

## 3. Prompt Pembuatan Visual Base & Character Sheet (Ingredients)

### A. Style Transformation / Master Visual Base Prompt
Gunakan prompt ini bersama gambar referensi asli untuk menghasilkan **Visual Base** utama:
```text
Use the uploaded photo as the ONLY identity reference. Preserve the person's exact facial bone structure, eye shape, skin tone, hairstyle, body proportions, and distinctive features (round tortoiseshell eyeglasses, shoulder-length wavy chestnut-black hair with curtain bangs, mustard-yellow oversized corduroy jacket) with 100% accuracy. Transform this exact person into a 3D Pixar-quality animated character: Senja, young woman around 24 years old, soft heart-shaped face, warm light-tan skin tone, subtle freckles across nose bridge, large expressive dark brown almond eyes, neat natural arched eyebrows, shoulder-length wavy chestnut-black hair with wispy curtain bangs, wearing mustard-yellow oversized corduroy jacket over a striped navy-and-white crew-neck tee, dark blue rolled-up denim jeans, and white canvas high-top sneakers, with round tortoiseshell eyeglasses and a small silver crescent moon pendant necklace, slender medium build, 165cm height, relaxed posture; strictly preserve the exact same face, hairstyle, wardrobe, body proportions, and signature traits (round tortoiseshell eyeglasses, shoulder-length wavy chestnut-black hair with curtain bangs, mustard-yellow oversized corduroy jacket) in every scene. Chest-up portrait facing the camera with a calm natural expression, neutral studio gray background (#D8D8D8), even 5600K soft studio lighting, sharp focus on eyes.
```

### B. 4-Panel Multi-Angle Turnaround Sheet Prompt
Gunakan hasil **Visual Base** di atas sebagai gambar referensi untuk membuat *Turnaround Sheet*:
```text
Using the attached character portrait as the strict reference, create a 4-panel character turnaround reference sheet on a clean neutral studio gray background (#D8D8D8). Panel 1: Full-body front view standing in a relaxed neutral pose. Panel 2: Full-body 3/4 angled view. Panel 3: Full-body 90-degree side profile view. Panel 4: Close-up facial portrait with a subtle warm expression. Character specification: Senja, young woman around 24 years old, soft heart-shaped face, warm light-tan skin tone, subtle freckles across nose bridge, large expressive dark brown almond eyes, neat natural arched eyebrows, shoulder-length wavy chestnut-black hair with wispy curtain bangs, wearing mustard-yellow oversized corduroy jacket over a striped navy-and-white crew-neck tee, dark blue rolled-up denim jeans, and white canvas high-top sneakers, with round tortoiseshell eyeglasses and a small silver crescent moon pendant necklace, slender medium build, 165cm height, relaxed posture; strictly preserve the exact same face, hairstyle, wardrobe, body proportions, and signature traits (round tortoiseshell eyeglasses, shoulder-length wavy chestnut-black hair with curtain bangs, mustard-yellow oversized corduroy jacket) in every scene. Flat, even studio lighting with zero harsh shadows, head-to-toe visibility.
```

---

## 4. Konfigurasi Tab `Characters` di Google Flow

Salin konfigurasi berikut saat membuat karakter baru di **Google Flow (`Characters` -> `New Character`)**:

- **Character Name**: `Senja` (Panggil di prompt dengan `@Senja`)
- **Extra Views (Body & Outfit Description)**:
  ```text
  slender medium build, 165cm height, relaxed posture. Wearing mustard-yellow oversized corduroy jacket over a striped navy-and-white crew-neck tee, dark blue rolled-up denim jeans, and white canvas high-top sneakers, paired with round tortoiseshell eyeglasses and a small silver crescent moon pendant necklace. Strictly keep the same outfit colors, fabric textures, and silhouette from every angle.
  ```
- **Voice Profile (Warm Young Female Alto)**:
  ```text
  Warm and clear alto voice, conversational medium-fast pace, expressive and curious tone with a gentle smile in the voice.
  ```
- **Character Info (Persona Memory untuk Google Flow Agent)**:
  ```text
  Senja is an inquisitive indie illustrator and urban sketcher. She is observant, warm-hearted, and slightly clumsy when excited. Mannerisms: frequently pushes her round tortoiseshell glasses up her nose and tilts her head slightly when listening. Speaks in vivid, enthusiastic sentences.
  ```

---

## 5. Prompt Storyboard & 3-Shot Continuity Benchmark (Veo / Google Flow)

### Scene 1 - Studio Intro (Close-Up & Lip-Sync)
```text
@Senja Senja, young woman around 24 years old, soft heart-shaped face, warm light-tan skin tone, subtle freckles across nose bridge, large expressive dark brown almond eyes, neat natural arched eyebrows, shoulder-length wavy chestnut-black hair with wispy curtain bangs, wearing mustard-yellow oversized corduroy jacket over a striped navy-and-white crew-neck tee, dark blue rolled-up denim jeans, and white canvas high-top sneakers, with round tortoiseshell eyeglasses and a small silver crescent moon pendant necklace, slender medium build, 165cm height, relaxed posture; strictly preserve the exact same face, hairstyle, wardrobe, body proportions, and signature traits (round tortoiseshell eyeglasses, shoulder-length wavy chestnut-black hair with curtain bangs, mustard-yellow oversized corduroy jacket) in every scene. Scene: Medium close-up shot at eye level, 85mm lens, shallow depth of field in a cozy sunlit art studio filled with sketchbooks and indoor plants, warm morning window light. @Senja adjusts her round tortoiseshell glasses gently, looks directly into the camera, and smiles warmly and naturally speaks the following dialogue with realistic facial expressions and accurate lip synchronization: "Halo semuanya! Hari ini kita bakal keliling kota buat cari inspirasi sketsa baru."
```

### Scene 2 - Street Exploration (Full-Body Shot)
```text
@Senja Senja, young woman around 24 years old, soft heart-shaped face, warm light-tan skin tone, subtle freckles across nose bridge, large expressive dark brown almond eyes, neat natural arched eyebrows, shoulder-length wavy chestnut-black hair with wispy curtain bangs, wearing mustard-yellow oversized corduroy jacket over a striped navy-and-white crew-neck tee, dark blue rolled-up denim jeans, and white canvas high-top sneakers, with round tortoiseshell eyeglasses and a small silver crescent moon pendant necklace, slender medium build, 165cm height, relaxed posture; strictly preserve the exact same face, hairstyle, wardrobe, body proportions, and signature traits (round tortoiseshell eyeglasses, shoulder-length wavy chestnut-black hair with curtain bangs, mustard-yellow oversized corduroy jacket) in every scene. Scene: Full-body wide shot, 35mm cinematic lens in a charming old-town cobblestone street lined with vintage cafes in golden hour light. @Senja stands near a wooden cafe signboard holding a leather sketchbook and pencil, looking around curiously. Maintain consistent facial geometry, hair silhouette, and wardrobe throughout the motion.
```

### Scene 3 - Walking Sequence (Tracking Motion Shot)
```text
@Senja Senja, young woman around 24 years old, soft heart-shaped face, warm light-tan skin tone, subtle freckles across nose bridge, large expressive dark brown almond eyes, neat natural arched eyebrows, shoulder-length wavy chestnut-black hair with wispy curtain bangs, wearing mustard-yellow oversized corduroy jacket over a striped navy-and-white crew-neck tee, dark blue rolled-up denim jeans, and white canvas high-top sneakers, with round tortoiseshell eyeglasses and a small silver crescent moon pendant necklace, slender medium build, 165cm height, relaxed posture; strictly preserve the exact same face, hairstyle, wardrobe, body proportions, and signature traits (round tortoiseshell eyeglasses, shoulder-length wavy chestnut-black hair with curtain bangs, mustard-yellow oversized corduroy jacket) in every scene. Scene: Smooth medium front-tracking gimbal shot in a tree-lined park pathway with dappled afternoon sunlight. @Senja walks forward at a relaxed pace with her sketchbook tucked under her left arm, hair swaying naturally. Maintain consistent facial geometry, hair silhouette, and wardrobe throughout the motion.
```

---

## 6. Checklist Continuity Control Sebelum Render Video
- [ ] **Face Check**: Struktur wajah, mata, dan alis pada *starting frame* identik dengan *Master Visual Base*.
- [ ] **Immutable Traits Check**: Ketiga ciri mutlak terlihat jelas dan tidak berubah warna/bentuk.
- [ ] **Wardrobe Lock**: Tidak ada pencampuran pakaian dari *prompt* sebelumnya.
- [ ] **Single Variable Change**: Hanya mengubah lokasi/aksi secara bertahap dari *approved reference* terdekat.
