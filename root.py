key0 = input("insert your key: ")
def encryption_function():
    plain_text = input("insert your text: ")
    key = key0
    text_binary = ''.join(format(ord(i), '08b') for i in plain_text)
    key_binary = ''.join(format(ord(i), '08b') for i in key)
    #print(text_binary,"\n", key_binary)
    for i in range(len(text_binary)):
        if len(key_binary) < len(text_binary):
            key_binary=''.join(format(ord(i), '08b')for i in key) + key_binary
    cipher_binary=[(ord(a) ^ ord(b)) for a, b in zip( text_binary, key_binary)]  # key XOR text_binary
    ct=''.join(map(str, cipher_binary))
    print("the cipher in binary: "+"==="+ct+"===")
    x = ''
    for i in ct:
        an_integer = int(i, 2)
        x = x + chr(an_integer)
    #print("xxx", x, "xxx")
    return x
print(x)
cipher1=encryption_function()
def decryption():
    plain=cipher1
    key=key0
    text_binary = ''.join(format(ord(i), '08b') for i in plain)
    key_binary = ''.join(format(ord(i), '08b') for i in key)
    print(text_binary, "\n", key_binary)
    for i in range(len(text_binary)):
        if len(key_binary) < len(text_binary):
            key_binary = ''.join(format(ord(i), '08b') for i in key) + key_binary
    cipher_binary = [(ord(a) ^ ord(b)) for a, b in zip(
        text_binary, key_binary)]  # key XOR text_binary
    pt = ''.join(map(str, cipher_binary))
    print(pt)
    #print("the original in binary: "+"==="+pt+"===")
decryption()