# Google Flow Character Creator Skill & Workflow (`google-flow-character`)

Repository ini berisi paket lengkap **AI Agent Skill (`SKILL.md`)**, **End-to-End Workflow**, **Referensi Prompt Transformasi Gaya Visual**, **Template Character Bible**, serta **Generator Script** untuk membuat karakter AI yang konsisten dari gambar referensi di ekosistem **Google Flow** (*Nano Banana Pro*, *Gemini Omni Flash*, *Veo*, *Ingredients*, *Whisk*, dan *@Character Tags*).

---

## Struktur Repository

- **[SKILL.md](SKILL.md)** — Instruksi utama skill `google-flow-character` untuk AI Agent (juga tersedia di [.agents/skills/google-flow-character/SKILL.md](.agents/skills/google-flow-character/SKILL.md)).
- **[workflows/create-character-from-image.md](workflows/create-character-from-image.md)** — Workflow lengkap langkah demi langkah dari 1 gambar referensi hingga produksi video multi-scene di Google Flow (juga disinkronkan ke [.agents/workflows/create-character-from-image.md](.agents/workflows/create-character-from-image.md)).
- **[references/style-transformations.md](references/style-transformations.md)** — Library prompt *Identity Preservation Lock* untuk mengubah foto referensi menjadi:
  - *3D Pixar / Disney Animation* (+ *Pixar Mirror validation prompt*)
  - *Cinematic Photorealism (Studio Master Portrait)*
  - *Modern Anime / 2D Cel-Shaded*
  - *Stylized 3D Painterly (Arcane style)*
  - *Claymation / Stop-Motion*
  - *4-Panel Multi-Angle Turnaround Sheet*
- **[references/google-flow-setup-guide.md](references/google-flow-setup-guide.md)** — Panduan teknis fitur native Google Flow:
  - Setup tab `Characters` (`Visual Base`, `Extra Views`, `Voice Profile`, dan `Character Info` untuk *Google Flow Agent*)
  - Perbandingan 3 mode referensi: `@Tags` (`@NamaKarakter`, `@me`), `Ingredients`, dan `Whisk`
  - 5 *Flow Creative Tools* (`Character Poster`, `Character Arc`, `Pixel Machine`, `Lucid Glass`, `Pocket Studio`)
  - Troubleshooting *identity drift* saat render video Veo
- **[templates/character-spec-template.md](templates/character-spec-template.md)** — Template *Character Bible* & *Google Flow Pack* siap pakai.
- **[templates/example-character.json](templates/example-character.json)** — Contoh spesifikasi JSON karakter (`@Senja`).
- **[scripts/generate_character_pack.py](scripts/generate_character_pack.py)** — Script Python CLI untuk men-generate dokumen *Google Flow Character Pack* otomatis dari file JSON.
- **[examples/senja-character-pack.md](examples/senja-character-pack.md)** — Contoh hasil *output* lengkap untuk karakter `@Senja`.

---

## Cara Menggunakan Skill Ini

### 1. Lewat Chat AI Agent (Otomatis dari Gambar)
Cukup lampirkan gambar referensi atau sebutkan path file gambar di chat, lalu ketik:
> *"Buatkan karakter Google Flow dari gambar ini dengan gaya [3D Pixar / Cinematic Realism / Anime] beserta workflow dan prompt videonya."*

Agent akan otomatis menjalankan skill `google-flow-character` untuk:
1. Mengekstrak **Visual DNA** & **3 Immutable Traits** dari gambarmu.
2. Menyusun **Locked Identity Block** yang mengunci struktur wajah, rambut, dan pakaian.
3. Membuatkan prompt **Style Transformation** & **4-Panel Turnaround Sheet (Ingredients)**.
4. Menyiapkan teks konfigurasi untuk tab **Characters** di Google Flow (`@Tag`, *Extra Views*, *Custom Voice*, dan *Character Info* untuk Flow Agent).
5. Menyusun prompt **3-Shot Continuity Benchmark** & storyboard video **Veo** lengkap dengan dialog *lip-sync*.

### 2. Lewat CLI Script (`generate_character_pack.py`)
Kamu juga bisa mengisi file JSON spesifikasi karakter dan men-generate dokumen paket karakter secara otomatis:

```bash
python3 scripts/generate_character_pack.py \
  --input templates/example-character.json \
  --output examples/senja-character-pack.md
```