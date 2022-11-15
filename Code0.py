def encryption_function():
    plain_text = input("insert your text: ")
    key = input("insert your key: ")
    text_binary = ''.join(format(ord(i), '08b') for i in plain_text)
    key_binary = ''.join(format(ord(i)-10, '08b') for i in key)  # convert to binary
    print("text binary: " + text_binary)
    print("key  binary: " + key_binary)
    for i in range(len(text_binary)):  # key on length of text_binary
        if len(key_binary) < len(text_binary):
            key_binary = ''.join(format(ord(i), '08b') for i in key) + key_binary
    cipher_binary = [(ord(a) ^ ord(b)) for a, b in zip(text_binary, key_binary)]  # key XOR text_binary
    ct = ''.join(map(str, cipher_binary))
    print(ct)
    #ct_split = ct.split()
    #x = ''
    #for i in ct_split:
    #    an_integer = int(i, 20)
    #    x = x + chr(an_integer)
    #print("xxx", x, "xxx")

    def BinaryToDecimal(binary):  # convert from binary to decimal
        binary1 = binary
        decimal, i, n = 0, 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary//10
            i += 1
        return (decimal)
    str_data = ' '  # from decimal to text
    for i in range(0, len(ct), 7):
        temp_data = int(ct[i:i + 7])
        decimal_data = BinaryToDecimal(temp_data)
        str_data = str_data + chr(decimal_data)
    print("Your cipher text is:", str_data)
    return str_data
print("THE CIPHER:==="+encryption_function()+"===")

text = str(encryption_function)
#print("the cipher text:", encryption_function())

def decryption_function():
    plain_text = text     #input("input cipher: ")   خليه تلقائيا ياخد النص المشفر أفضل ما انت تاخدو كوبي بيست للاحتياط يلي هو متغير text
    key = input("insert your key: ")
    text_binary = ''.join(format(ord(i), '08b') for i in plain_text)
    key_binary = ''.join(format(ord(i)+10, '08b') for i in key)  # convert to binary
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
    print(reverse_cipher)
    '''cipher_split = cipher_binary.split()
    x = ''
    for i in cipher_split:
        an_integer = int(i, 2)
        x = x + chr(an_integer)
    print("xxx", x, "xxx")'''
    def BinaryToDecimal(binary):
        string = int(binary, 2)
        return string
    #list_cipher = ' '  # convert to literial
    #for i in range(0, len(reverse_cipher)):
    #    list_cipher = list_cipher + reverse_cipher[i]
    str_data = ' '
    for i in range(0, len(reverse_cipher), 7):
        temp_data = reverse_cipher[i:i + 7]
        decimal_data = BinaryToDecimal(temp_data)
        str_data = str_data + chr(decimal_data)
    print("Your original text is:", str_data)
    return str_data
print("THE ORIGINAL:", decryption_function())