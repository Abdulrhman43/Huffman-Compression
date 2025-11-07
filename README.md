# 🧠 Huffman Compression & Decompression System

📌 **Overview**

A Python-based **Huffman Compression System** that performs **lossless data compression** and **decompression**.  
It reads data from a text file, compresses it into a binary file, and then restores it perfectly to its original form.

This project was developed as part of the **Information Theory and Data Compression** course assignment.

---

## 💻 **Technology Used**

- 🐍 **Programming Language:** Python 3.8+
- 📦 **Libraries Used:** `heapq`, `json`
- 💾 **Input/Output:** Text files (`.txt`) and binary files (`.bin`)

---

## 🎯 **Project Purpose**

To demonstrate the use of **Huffman Coding Algorithm**,  
which assigns shorter binary codes to frequent characters and longer codes to rare ones,  
achieving **efficient data compression** without any data loss.

---

## ⚙️ **Main Functionalities**

### 🧩 Compression Module (`assig2.py`)

- 📊 **Frequency Analysis:** Counts the frequency of each character in the input text.
- 🌳 **Tree Construction:** Builds the Huffman Tree using a min-heap.
- 💡 **Code Generation:** Generates unique binary codes for each character.
- 🧬 **Encoding:** Converts the input text into a compressed binary bitstream.
- 💾 **File Saving:** Saves both:
  - The Huffman code dictionary (in JSON format)
  - The binary compressed data stream (in `.bin` format)
- 🧱 **Padding Handling:** Calculates and stores the number of added bits to complete full bytes.

---

### 🔁 Decompression Module (`assig22.py`)

- 📂 **File Loading:** Reads the `.bin` compressed file.
- 🧩 **Dictionary Extraction:** Extracts and decodes the Huffman dictionary.
- 🔢 **Bitstream Conversion:** Converts bytes back into bit sequences.
- ✂️ **Padding Removal:** Removes extra padding bits added during compression.
- 🔄 **Decoding:** Reconstructs the original text from the binary codes.
- 📝 **File Output:** Writes the decompressed data to `decompressed.txt`.

---

## 🧮 **Key Functions**

| Function Name | Description |
|----------------|-------------|
| `build_huffman_tree(text)` | Builds Huffman tree from character frequencies |
| `generate_codes(node, current, codes)` | Recursively generates Huffman binary codes |
| `huffman_compress(text)` | Compresses text and returns bitstream + codes |
| `bits_to_bytes(bits)` | Converts bitstream to byte format and calculates padding |
| `save_compressed_file(filename, codes, bitstream)` | Saves encoded data and dictionary to binary file |
| `bytesToBits(byte_data)` | Converts bytes back to bit sequence during decompression |
| `load_compressed_file(filename)` | Reads binary file and extracts both codes and data |
| `swapDictionary(codes)` | Reverses Huffman dictionary for decoding |
| `huffman_decompress(filename)` | Fully reconstructs text from binary data |
