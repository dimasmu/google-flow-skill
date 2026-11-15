# Affiliate UGC Workflow: Satto Hair Tonic Serum Herbal 160ML (`@nadia`)

Dokumentasi workflow produksi video affiliate **natural (non-AI look)** di **Google Flow** menggunakan strategi **Hybrid (AI Talking Head + Real B-Roll)** dan metode **Still-First, Video-Second** (`9:16` Vertical).

- **Produk**: Satto Hair Tonic Serum Herbal 160ML – Penumbuh Rambut, Atasi Rambut Rontok & Kuatkan Akar
- **Link Referensi**: https://shopee.co.id/product/667103265/15552301083
- **Karakter**: `@nadia` (wanita muda Indonesia, rambut hitam sebahu kering rapi, *black spaghetti-strap camisole*, celana *sage-beige*)
- **Kemasan Produk**: Botol silinder cokelat gelap (*amber*), tutup ulir hitam, label gelombang oranye-putih-hitam, *badge* hijau tosca `SATTO`, teks `HAIR TONIC SERUM HERBAL 160 ml`.

---

## 1. Persiapan Aset (*Ingredients*)

1. **Referensi Produk Terbaik**: Foto produk bersih tanpa stiker promo (botol & dus terlihat tajam).
2. **B-Roll Asli (Anti-AI)**: Video *POV* tangan memutar botol asli (memperlihatkan label depan, belakang, dan nomor BPOM) untuk disisipkan di tengah video agar AI tidak perlu merender rotasi teks kecil.
3. **Setup Voice Profile (`Custom Voice`) di Tab `Characters`**:
   ```text
   Natural, casual Indonesian young adult voice, conversational and relaxed pace, warm everyday tone like talking to a close friend on a smartphone video, slight natural breath pauses, no commercial announcer intonation.
   ```

---

## 2. Prompt Still Frames (`Image` Mode — Rasio `9:16`)

> **Catatan Anti-Filter & Konsistensi**:
> - Gunakan lokasi **`bright minimalist living room`** dan **`wooden desk`** (hindari kata `bedroom`/`bed` dan `massage` agar tidak terkena *false-positive* filter kebijakan).
> - Hindari menyebut nama merek di teks prompt cukup gunakan foto produk sebagai lampiran (`+` / `Add`).
> - Lampirkan **gambar Shot 1/Shot 2 terpilih** sebagai referensi pertama agar wajah, pakaian, dan ruangan tetap 100% sama.

### Shot 1 — Hook (Tanpa Produk)
*(Gunakan `@nadia` atau lampirkan gambar referensi utama `@nadia` di ruang tamu)*
```text
Keep the exact same woman, black tank top, sage-beige pants, dry shoulder-length black hair, and bright minimalist living room from the reference image. 9:16 vertical, eye-level smartphone camera, natural morning window light. She sits at a wooden desk looking at the camera with a relatable thoughtful expression while gently running a wooden comb through her dry hair. Authentic everyday smartphone video style.
```

### Shot 2 — Product Reveal (Pegang Botol Stabil)
*(Lampirkan **Gambar Shot 1 terpilih** + **Foto Botol Satto** lewat tombol `+`)*
```text
Keep the exact same woman, fresh face, dry shoulder-length black layered hair, black spaghetti-strap camisole top, and exact same bright living room background from the first reference image. 9:16 vertical, shot on smartphone camera, eye-level medium shot. She holds the dark amber bottle with black cap from the second reference image steadily in one hand at chest level facing directly toward the camera, so the orange-white wave label and badge are sharp and readable. Warm friendly smile, natural daylight.
```

### Shot 4 — Pemakaian (Menyisir Rambut di Meja Kayu)
*(Shot 3 diisi B-Roll asli. Untuk Shot 4, lampirkan **Gambar Shot 1 terpilih** + **Foto Botol Satto** lewat `+`)*
```text
Keep the exact same woman, black tank top, sage-beige pants, dry shoulder-length black hair, and bright minimalist living room from the first reference image. 9:16 vertical, candid smartphone shot, soft daylight. She sits at the wooden desk with the amber bottle from the second reference image resting neatly on the table, while she gently combs her dry shoulder-length black hair with a wooden comb, looking refreshed with a soft natural smile.
```

### Shot 5 — Closing & CTA
*(Lampirkan **Gambar Shot 1/Shot 2 terpilih** + **Foto Botol Satto** lewat `+`)*
```text
Keep the exact same woman, fresh face, dry shoulder-length black hair, black spaghetti-strap camisole top, and exact same bright living room from the first reference image. 9:16 vertical, eye-level medium close-up, smartphone camera. Holding the dark amber bottle from the second reference image casually near shoulder level facing the camera, giving a warm bright natural smile. Soft morning window light, sharp product label, authentic UGC review style.
```

### Opsional: Memakai Background Referensi dari Website (Pexels / Unsplash / Pixabay / Pinterest)
*(Lampirkan **3 bahan**: `@nadia` + **Foto Ruangan Kosong `9:16`** + **Foto Botol Satto**)*
```text
Place @nadia naturally inside the exact room from the background reference image, matching the room's natural lighting, color tone, and soft shadows. She is sitting or standing comfortably and holding the bottle from the product reference image steadily toward the camera. 9:16 vertical, candid smartphone camera look.
```

---

## 3. Prompt Video Veo (`Video` -> `Frames`, Veo 3.1, `9:16`)

Gunakan masing-masing gambar hasil tahap 2 sebagai **Start Frame** (*frame awal*).

### Klip 1 — Hook
```text
Static smartphone camera with very slight natural handheld micro-shake. @nadia looks at the camera with a relatable expression while gently holding the wooden comb near her hair, and speaks casually in Indonesian: "Jujur paling males tiap habis keramas tuh lihat rambut rontok numpuk di lantai." Natural blinking and subtle head movement.
```

### Klip 2 — Product Reveal
```text
Static smartphone camera. @nadia holds the Satto bottle steady without rotating it, nodding slightly while speaking in a relaxed Indonesian everyday tone: "Makanya sekarang aku rutin pakai Hair Tonic Serum Herbal dari Satto yang 160 mili ini." Keep product bottle and label completely intact, minimal hand movement.
```

### Klip 3 — Pemakaian
```text
Subtle handheld smartphone camera. @nadia gently combs her hair with the wooden comb while looking comfortable and relaxed, speaking casually in Indonesian: "Pakainya tinggal habis keramas, teksturnya cair, ringan, dan nggak bikin rambut lepek sama sekali." Leave the Satto box and bottle untouched on the wooden table.
```

### Klip 4 — Closing & CTA
```text
Static smartphone camera. @nadia smiles warmly and naturally at the camera, speaking casually in Indonesian: "Kandungannya ada ginseng, aloe vera, sama vitamin E buat kuatin akar. Yang rambutnya lagi rontok, langsung cek keranjang ya!" Subtle natural head tilt.
```

---

## 4. Susunan Timeline Hybrid di CapCut (~18–22 Detik)

| Urutan | Sumber Klip | Keterangan |
| :--- | :--- | :--- |
| **1. Hook** | Klip 1 Veo | Keluhan rambut rontok setelah keramas. |
| **2. Reveal** | Klip 2 Veo | Memperkenalkan Satto Hair Tonic 160ml. |
| **3. B-Roll Asli** | Video Testimoni Asli (*Mute*) | Tangan asli memutar botol & memperlihatkan label belakang/BPOM (3–4 detik). |
| **4. Pemakaian** | Klip 3 Veo | Menyisir rambut rapi di meja kayu, botol & dus terlihat jelas. |
| **5. Closing & CTA** | Klip 4 Veo | Ringkasan kandungan (ginseng, aloe vera, vitamin E) + ajakan cek keranjang. |

**Tips Finishing**:
* Potong jeda hening (0.2–0.4 detik) di awal/akhir setiap klip Veo agar ritme bicara terasa cepat dan alami.
* Samakan *warmth/contrast* antara klip AI dan B-Roll asli agar transisi tidak jomplang.
* Tambahkan *auto-caption* dan musik *lo-fi* pelan (volume 5–8%).
