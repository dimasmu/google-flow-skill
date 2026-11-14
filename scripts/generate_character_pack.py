#!/usr/bin/env python3
"""
Google Flow Character Pack Generator
------------------------------------
Menghasilkan dokumen lengkap "Google Flow Character Pack" (Locked Identity Block,
Style Transformation Prompts, 4-Panel Turnaround Ingredients Prompt, Setup Tab Characters,
dan Multi-Shot Storyboard Veo Prompts) dari file spesifikasi JSON.

Cara Pakai:
  python3 scripts/generate_character_pack.py --input templates/example-character.json --output output/senja-character-pack.md
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List


def build_locked_identity_block(spec: Dict[str, Any]) -> str:
    name = spec.get("name", "Character")
    age_gender = spec.get("age_and_gender", "")
    face_skin = spec.get("face_and_skin", "")
    eyes_brows = spec.get("eyes_and_brows", "")
    hair = spec.get("hair", "")
    wardrobe = spec.get("wardrobe", "")
    accessories = spec.get("accessories", "")
    proportions = spec.get("body_proportions", "")
    traits: List[str] = spec.get("immutable_traits", [])

    traits_str = ", ".join(traits) if traits else "exact face, hair, and outfit"
    parts = [
        f"{name}",
        age_gender,
        face_skin,
        eyes_brows,
        hair,
        f"wearing {wardrobe}" if wardrobe else "",
        f"with {accessories}" if accessories else "",
        proportions,
    ]
    clean_parts = [p.strip() for p in parts if p and p.strip()]
    base_desc = ", ".join(clean_parts)
    return (
        f"{base_desc}; strictly preserve the exact same face, hairstyle, wardrobe, "
        f"body proportions, and signature traits ({traits_str}) in every scene."
    )


def generate_markdown_pack(spec: Dict[str, Any]) -> str:
    name = spec.get("name", "Character")
    tag = spec.get("tag") or f"@{name.replace(' ', '')}"
    source_image = spec.get("source_image", "uploaded_reference_image.png")
    target_style = spec.get("target_style", "Cinematic Photorealism")
    traits = spec.get("immutable_traits", [])
    voice = spec.get("voice_profile", {})
    agent_info = spec.get("character_info_agent", "")
    scenes = spec.get("sample_scenes", [])

    locked_block = build_locked_identity_block(spec)
    traits_inline = ", ".join(traits) if traits else "signature facial features and outfit"

    md: List[str] = []
    md.append(f"# Google Flow Character Pack: `{tag}` ({name})")
    md.append("")
    md.append(f"- **Source Reference Image**: `{source_image}`")
    md.append(f"- **Target Visual Style**: `{target_style}`")
    md.append(f"- **Google Flow Tag**: `{tag}`")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 1. Visual DNA & 3 Immutable Traits")
    md.append("")
    md.append("| Komponen Identitas | Spesifikasi Terkunci (Locked Spec) |")
    md.append("| :--- | :--- |")
    md.append(f"| **Nama & Tag** | **{name}** (`{tag}`) |")
    md.append(f"| **Usia & Karakteristik** | {spec.get('age_and_gender', '-')} |")
    md.append(f"| **Wajah & Skin Tone** | {spec.get('face_and_skin', '-')} |")
    md.append(f"| **Mata & Alis** | {spec.get('eyes_and_brows', '-')} |")
    md.append(f"| **Rambut** | {spec.get('hair', '-')} |")
    md.append(f"| **Pakaian Utama (Default Wardrobe)** | {spec.get('wardrobe', '-')} |")
    md.append(f"| **Aksesori Khas** | {spec.get('accessories', '-')} |")
    md.append(f"| **Proporsi Tubuh** | {spec.get('body_proportions', '-')} |")
    md.append("")
    md.append("### 3 Immutable Traits (Wajib Dipertahankan di Semua Shot)")
    for idx, trait in enumerate(traits, start=1):
        md.append(f"{idx}. **{trait}**")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 2. Locked Identity Block (Tempel di Awal Setiap Prompt)")
    md.append("")
    md.append("```text")
    md.append(locked_block)
    md.append("```")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 3. Prompt Pembuatan Visual Base & Character Sheet (Ingredients)")
    md.append("")
    md.append("### A. Style Transformation / Master Visual Base Prompt")
    md.append("Gunakan prompt ini bersama gambar referensi asli untuk menghasilkan **Visual Base** utama:")
    md.append("```text")
    md.append(
        f"Use the uploaded photo as the ONLY identity reference. Preserve the person's exact facial bone structure, "
        f"eye shape, skin tone, hairstyle, body proportions, and distinctive features ({traits_inline}) with 100% accuracy. "
        f"Transform this exact person into a {target_style}: {locked_block} "
        f"Chest-up portrait facing the camera with a calm natural expression, neutral studio gray background (#D8D8D8), "
        f"even 5600K soft studio lighting, sharp focus on eyes."
    )
    md.append("```")
    md.append("")
    md.append("### B. 4-Panel Multi-Angle Turnaround Sheet Prompt")
    md.append("Gunakan hasil **Visual Base** di atas sebagai gambar referensi untuk membuat *Turnaround Sheet*:")
    md.append("```text")
    md.append(
        f"Using the attached character portrait as the strict reference, create a 4-panel character turnaround reference sheet "
        f"on a clean neutral studio gray background (#D8D8D8). "
        f"Panel 1: Full-body front view standing in a relaxed neutral pose. "
        f"Panel 2: Full-body 3/4 angled view. "
        f"Panel 3: Full-body 90-degree side profile view. "
        f"Panel 4: Close-up facial portrait with a subtle warm expression. "
        f"Character specification: {locked_block} "
        f"Flat, even studio lighting with zero harsh shadows, head-to-toe visibility."
    )
    md.append("```")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 4. Konfigurasi Tab `Characters` di Google Flow")
    md.append("")
    md.append("Salin konfigurasi berikut saat membuat karakter baru di **Google Flow (`Characters` -> `New Character`)**:")
    md.append("")
    md.append(f"- **Character Name**: `{name}` (Panggil di prompt dengan `{tag}`)")
    md.append("- **Extra Views (Body & Outfit Description)**:")
    md.append("  ```text")
    md.append(
        f"  {spec.get('body_proportions', '')}. Wearing {spec.get('wardrobe', '')}, "
        f"paired with {spec.get('accessories', '')}. Strictly keep the same outfit colors, fabric textures, and silhouette from every angle."
    )
    md.append("  ```")
    md.append(f"- **Voice Profile ({voice.get('base_type', 'Custom Voice')})**:")
    md.append("  ```text")
    md.append(f"  {voice.get('custom_voice_prompt', 'Natural, clear conversational voice matching the character persona.')}")
    md.append("  ```")
    md.append("- **Character Info (Persona Memory untuk Google Flow Agent)**:")
    md.append("  ```text")
    md.append(f"  {agent_info}")
    md.append("  ```")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 5. Prompt Storyboard & 3-Shot Continuity Benchmark (Veo / Google Flow)")
    md.append("")

    if scenes:
        for idx, scene in enumerate(scenes, start=1):
            title = scene.get("title", f"Shot {idx}")
            camera = scene.get("camera", "Medium shot, 50mm lens")
            setting = scene.get("setting", "clean modern environment, natural lighting")
            action = scene.get("action", "stands naturally looking ahead")
            dialogue = scene.get("dialogue", "").strip()

            md.append(f"### {title}")
            md.append("```text")
            if dialogue:
                md.append(
                    f"{tag} {locked_block} Scene: {camera} in a {setting}. "
                    f"{tag} {action} and naturally speaks the following dialogue with realistic facial expressions "
                    f"and accurate lip synchronization: \"{dialogue}\""
                )
            else:
                md.append(
                    f"{tag} {locked_block} Scene: {camera} in a {setting}. "
                    f"{tag} {action}. Maintain consistent facial geometry, hair silhouette, and wardrobe throughout the motion."
                )
            md.append("```")
            md.append("")

    md.append("---")
    md.append("")
    md.append("## 6. Checklist Continuity Control Sebelum Render Video")
    md.append("- [ ] **Face Check**: Struktur wajah, mata, dan alis pada *starting frame* identik dengan *Master Visual Base*.")
    md.append("- [ ] **Immutable Traits Check**: Ketiga ciri mutlak terlihat jelas dan tidak berubah warna/bentuk.")
    md.append("- [ ] **Wardrobe Lock**: Tidak ada pencampuran pakaian dari *prompt* sebelumnya.")
    md.append("- [ ] **Single Variable Change**: Hanya mengubah lokasi/aksi secara bertahap dari *approved reference* terdekat.")
    md.append("")

    return "\n".join(md)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a Google Flow Character Pack markdown file from a JSON character specification."
    )
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="Path ke file JSON spesifikasi karakter (lihat templates/example-character.json)",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=False,
        help="Path file output Markdown (.md). Jika dikosongkan, hasil dicetak ke terminal (stdout).",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: File input '{input_path}' tidak ditemukan.", file=sys.stderr)
        return 1

    with input_path.open("r", encoding="utf-8") as f:
        spec = json.load(f)

    markdown_output = generate_markdown_pack(spec)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown_output, encoding="utf-8")
        print(f"Berhasil membuat Google Flow Character Pack di: {output_path}")
    else:
        print(markdown_output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
