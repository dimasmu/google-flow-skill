# Google Flow & AI Character Suite (`google-flow-skill`)

Repository ini berisi kumpulan **4 AI Agent Skills & Universal Chatbot System Prompts** serta **End-to-End Workflows** yang dirancang khusus untuk membuat, mencocokkan adegan/pose, mengganti pakaian, dan memproduksi video karakter AI yang **100% konsisten & hyper-realistic** di **Google Flow** (*Nano Banana Pro*, *Gemini Omni Flash*, *Veo*, *Ingredients*, *Whisk*), serta kompatibel penuh untuk dipasang di **ChatGPT (Custom GPT / Projects)**, **Gemini (Gems)**, **Google AI Studio (System Instructions)**, dan **Antigravity**.

---

## Daftar 4 Skill Utama di Repository Ini

### 1. [`base-character-ai-builder`](skills/base-character-ai-builder/SKILL.md) — *Hyper-Realistic & No-AI-Look Base Character Generator*
- **Fungsi Utama**: Membuat *Master Base Character* yang terlihat 100% seperti foto manusia asli hasil kamera profesional tanpa efek plastik/lilin (*No-AI-Look*).
- **Fitur Teknis**:
  - Menyuntikkan 5 lapisan realisme organik: *Micro-Asymmetry* anatomi wajah, tekstur kulit dermatologis (*visible micro-pores, vellus peach fuzz, subsurface scattering*), fisika mata autentik, detail *baby hairs/flyaways*, dan metadata optik kamera nyata (Canon EOS R5 / Phase One 85mm).
  - Menghasilkan **Master Close-Up Portrait (`Potret`)**, **3-Panel `16:9` Turnaround Sheet (`Buat badan`)**, **Locked Identity Block**, dan **Anti-AI Negative Constraints**.

### 2. [`character-matching-builder`](skills/character-matching-builder/SKILL.md) — *AI Character Scene, Pose, Lighting & Mood Matcher*
- **Fungsi Utama**: Meniru pose tubuh, posisi tangan, sudut kamera, *lighting*, *color grading*, *mood*, dan detail tempat dari gambar referensi mana pun (Pinterest/Instagram/katalog) lalu memasangkannya ke karakter AI milikmu **tanpa mengubah wajah karaktermu**.
- **Fitur Teknis**:
  - Membedah gambar referensi dengan **Protokol 7-Dimensi** (*Pose & Micro-Gesture, Camera & Lens Optics, Lighting Direction & Kelvin Temp, LUT/Color Grading, Set Dressing, Wardrobe Handling, & Identity Separation Lock*).
  - Menyediakan prompt untuk **Single-Reference Mode (`@Karakter`)**, **Dual-Reference Mode (`Whisk` / `Ingredients`)**, dan **Veo Image-to-Video Motion**.

### 3. [`outfit-swap-builder`](skills/outfit-swap-builder/SKILL.md) — *Zero-Drift AI Character Wardrobe & Outfit Swapper*
- **Fungsi Utama**: Mengganti pakaian/wardrobe karakter AI (baik lewat teks maupun transfer dari foto baju katalog/referensi) **tanpa mengubah detail wajah, gaya rambut, proporsi tubuh, skin tone, pose, atau pencahayaan**.
- **Fitur Teknis**:
  - Membedah pakaian dengan **6-Layer Garment Engineering** (*Silhouette & Cut, Fabric Physics & Drape, Color/Pattern, Stitching/Hardware, Footwear Harmony, & Hair-Collar Clearance*).
  - Menyediakan 3 mode prompt: **Mode 1 (In-Place Edit via `"Apa yang ingin Anda ubah?"`)**, **Mode 2 (Dual-Image Transfer via `Ingredients`)**, dan **Mode 3 (Master `16:9` Look Sheet untuk konsistensi video multi-shot)**.

### 4. [`google-flow-character`](SKILL.md) — *End-to-End Google Flow Character & Video Production Skill*
- **Fungsi Utama**: Mengintegrasikan seluruh siklus karakter di dalam studio **Google Flow** (`flow.google.com`) mulai dari ekstraksi DNA visual, transformasi gaya visual (3D Pixar, Anime, Realism), setup tab `Characters` (`Potret`, `Buat badan`, `Voice Profile`, `Info karakter`), hingga storyboard video **Veo**.

---

## Cara Memasang di ChatGPT, Gemini (Gems), & Google AI Studio

Ketiga skill generator di folder `skills/` ditulis dengan format **Universal System Instruction** sehingga bisa langsung dipakai di chatbot AI mana pun:

1. **Google AI Studio (`aistudio.google.com`)**:
   - Buka file skill yang diinginkan (misal [`skills/base-character-ai-builder/SKILL.md`](skills/base-character-ai-builder/SKILL.md)).
   - Copy seluruh isinya $\rightarrow$ tempel ke kotak **System Instructions** di bagian atas Google AI Studio.
2. **Google Gemini (`Gems`)**:
   - Buka **Gem Manager** $\rightarrow$ klik **New Gem**.
   - Beri nama (misal: *Base Character AI-Builder* / *Character Matching Builder* / *Outfit Swap Builder*).
   - Paste isi file `SKILL.md` ke kolom **Instructions** $\rightarrow$ klik **Save**.
3. **ChatGPT (`Custom GPT` atau `Project Instructions`)**:
   - Buat Project baru atau Custom GPT baru $\rightarrow$ tempel isi file `SKILL.md` ke bagian **Instructions / System Prompt**.
4. **Antigravity / AI Coding Agent**:
   - Otomatis aktif dari folder `.agents/skills/` atau panggil langsung lewat nama skill-nya.

---

## Struktur File Lainnya di Repository

- **Workflows**:
  - [`workflows/create-character-from-image.md`](workflows/create-character-from-image.md) — Panduan end-to-end pembuatan karakter konsisten di Google Flow.
  - [`workflows/brand-promo-storyboard.md`](workflows/brand-promo-storyboard.md) — Workflow **Still-First, Video-Second** untuk menggabungkan `@Karakter` + Produk Brand + Environment dalam storyboard iklan 4-shot.
- **References**:
  - [`references/style-transformations.md`](references/style-transformations.md) — Prompt *Identity Preservation Lock* untuk berbagai gaya visual (3D Pixar, Anime, Cinematic Realism, Arcane, Claymation).
  - [`references/google-flow-setup-guide.md`](references/google-flow-setup-guide.md) — Panduan teknis UI Google Flow (`Potret`, `Buat badan`, `Info karakter`, `Voice`, `Ingredients`, `Whisk`, & 5 *Flow Tools*).
- **Templates & Generator Script**:
  - [`templates/character-spec-template.md`](templates/character-spec-template.md) & [`templates/example-character.json`](templates/example-character.json)
  - [`scripts/generate_character_pack.py`](scripts/generate_character_pack.py) — Script Python CLI untuk men-generate dokumen *Character Pack* otomatis.