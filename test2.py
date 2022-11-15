def encryption_function():
    plain_text = input("insert your text: ")
    key = input("insert your key: ")
    text_binary = ''.join(format(ord(i), '08b') for i in plain_text)
    key_binary = ''.join(format(ord(i)+3, '08b') for i in key)  # convert to binary
    print("text binary: " + text_binary)
    print("key  binary: " + key_binary)
    for i in range(len(text_binary)):  # key on length of text_binary
        if len(key_binary) < len(text_binary):
            key_binary = ''.join(format(ord(i), '08b') for i in key) + key_binary
    cipher_binary = [(ord(a) ^ ord(b)) for a, b in zip(text_binary, key_binary)]  # key XOR text_binary
    ct = ''.join(map(str, cipher_binary))
    print("the cipher in binary: "+"==="+ct+"===")
    global ascii_text
    binary_int = int(ct, 2)
    byte_number = binary_int.bit_length() + 7 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()
    print("THE CIPHER TEXT:\n"+"==="+ascii_text+"===")
    return ascii_text
text0 = encryption_function()
print(text0)


def decryption_function():
    byte_array = text0.encode()
    binary_int = int.from_bytes(byte_array, "big")
    text_binary = bin(binary_int)
    print(text_binary)
    key = input("insert your key: ")
    #text_binary = ''.join(format(ord(i), '08b') for i in plain_text)
    key_binary = ''.join(format(ord(i)-3, '08b') for i in key)  # convert to binary
    reverse_text = text_binary[len(text_binary)::-1]
    reverse_key = key_binary[len(key_binary)::-1]
    print("text binary: " + reverse_text)
    print("key binary: " + reverse_key)
    for i in range(len(reverse_text)):  # key on length of text_binary
        if len(reverse_key) < len(reverse_text):
            reverse_key = ''.join(format(ord(i), '08b') for i in key) + reverse_key
    ct = [(ord(a) ^ ord(b))for a, b in zip(reverse_text, reverse_key)]  # key XOR text_binary
    cipher_binary = ''.join(map(str, ct))
    reverse_cipher = cipher_binary[len(cipher_binary)::-1]
    text = reverse_cipher
    print("test= ", text)
 #cipher_split = cipher_binary.split()
    x = ''
    for i in text:
        an_integer = int(i, 2)
        x = x + chr(an_integer)
    print("xxx", x, "xxx")
decryption_function()