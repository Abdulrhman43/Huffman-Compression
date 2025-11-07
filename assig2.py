import heapq, json
from over import overr

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1 
    
    heap = []
    for ch, f in freq.items():
        heapq.heappush(heap, Node(ch, f))
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_codes(node, current="", codes={}):
    if node is None:
        return
    if node.char is not None:
        if current == "":
         codes[node.char] = "0"
         return codes
        else:
         codes[node.char] = current
        return
    generate_codes(node.left, current + "0", codes)
    generate_codes(node.right, current + "1", codes)
    return codes

def huffman_compress(text):
    root = build_huffman_tree(text)
    codes = generate_codes(root)
    encoded_text = ''.join(codes[ch] for ch in text)
    return encoded_text, codes
#####################################################################

def bits_to_bytes(bits):
    
    while len(bits) % 8 != 0:
        bits += "0"
        overr.over+=1
        
    byte_arr = bytearray()
    for i in range(0, len(bits), 8):
        byte_chunk = bits[i:i+8]
        byte_arr.append(int(byte_chunk, 2))

    return bytes(byte_arr)

def save_compressed_file(filename, codes, bitstream):
    byte_data = bits_to_bytes(bitstream)
    with open(filename, "wb") as f:
        codes_json = json.dumps(codes)
        f.write(codes_json.encode('utf-8'))
       
        f.write(b"\n---DATA---\n")
        f.write(byte_data)
####################################################
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read().strip()

bitstream, codes = huffman_compress(text)
save_compressed_file("output.bin", codes, bitstream)
print("✅ Compression done! Output saved in output.bin")


