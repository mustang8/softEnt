# 22:00-22:30
import sys

def compress_rle (text):
    if not text: 
        return "no text provided"
    compressed = []
    size = len(text)
    count = 1
    for char in range(1, size):
        if text[char] == text[char - 1]:
            count += 1
        else:
            compressed.append(f"{text[char - 1]}{count if count > 1 else ''}")
            count = 1
    return ''.join(compressed)

def decompress_rle (compressed_text):
    decompressed = []
    size = len(compressed_text)
    for char in range(size):
        if char + 1 < size and compressed_text[char + 1].isdigit():
            count = int(compressed_text[char + 1])
            decompressed.append(compressed_text[char] * count)
        elif compressed_text[char].isdigit():
            continue
        else:
            decompressed.append(compressed_text[char])
    return ''.join(decompressed)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    input_file = sys.argv[1]
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
        text = text.strip()
    compressed_text = compress_rle(text)
    print(compressed_text)
    decompressed_text = decompress_rle(compressed_text)
    print(decompressed_text)
