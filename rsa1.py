def encrypt(text, s):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


text = "anil"
s = 4
print("Text", text)
print("Shift:", str(s))
print("Cipher:" + encrypt(text, s))
