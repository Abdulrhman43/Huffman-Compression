import json 
import assig2
from over import overr
# this function changes from bytes to bits 
def bytesToBits(byte_data):
    x=overr.over
    bits = ""  
    for byte in byte_data:
        binary = format(byte, '08b')  # change every byte to 8 bits
        bits += binary 
    if x != 0 :
         bits=bits[:-x] 

   
    return bits
# this function loads the compressed file and separates the dictionary part from the byte part
def load_compressed_file(filename):
    f = open(filename, "rb")
    content = f.read()
    f.close()
    separator = b"\n---DATA---\n"
    #separator begining
    sepStart = content.index(separator)
    #the part before the separator is the dictionary part
    dictionryPart = content[:sepStart].decode('utf-8')
    #the part after the separator is the byte part
    byte_part = content[sepStart + len(separator):]
    #load the dictionary part as a json object
    codes = json.loads(dictionryPart)
    #convert the byte part to bits
    bits = bytesToBits(byte_part)

    return codes, bits
# this function swaps the keys and values of the dictionary into a new dictionary
def swapDictionary(codes):
    new_dict = {}                 
    for k, v in codes.items():
        new_dict[v] = k           
    return new_dict  

def huffman_decompress(filename):
    codes, bits = load_compressed_file(filename)
    # create the reverse dictionary
    reverse_codes = swapDictionary(codes)
    current = ""
    decoded_text = ""
    # iterate through the bits to decode the text
    for bit in bits:
        current += bit
        if current in reverse_codes:
            decoded_text += reverse_codes[current]
            current = ""
    return decoded_text

text = huffman_decompress("output.bin")
f = open("decompressed.txt", "w", encoding="utf-8")
f.write(text)
f.close()
print("Decompression done! Output saved in decompressed.txt")