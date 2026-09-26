from PIL import Image
import os

INPUT_FILE = "логотип Kashiwa Ole.webp"
OUTPUT_192 = "icon-192.png"
OUTPUT_512 = "icon-512.png"
BG_COLOR = (30, 83, 141, 255)

def create_icon(input_path, output_path, size):
    img = Image.open(input_path)
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    background = Image.new('RGBA', (size, size), BG_COLOR)
    margin = int(size * 0.1)
    logo_size = size - 2 * margin
    img_resized = img.resize((logo_size, logo_size), Image.LANCZOS)
    offset = ((size - logo_size) // 2, (size - logo_size) // 2)
    background.paste(img_resized, offset, img_resized)
    background.save(output_path, 'PNG')
    print(f"OK: {output_path} ({size}x{size})")

if __name__ == "__main__":
    if not os.path.exists(INPUT_FILE):
        print(f"ERROR: File not found: {INPUT_FILE}")
        for f in os.listdir('.'):
            print(f"  - {f}")
        exit(1)
    create_icon(INPUT_FILE, OUTPUT_192, 192)
    create_icon(INPUT_FILE, OUTPUT_512, 512)
    print("Done!")
