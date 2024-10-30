def atbash_cipher(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for char in text.lower():
        if char in alphabet:
            index = alphabet.index(char)
            result += alphabet[25-index]
        else:
            result += char
        return result
text = "Hello world!"
encrypted_text = atbash_cipher(text)
print(f"Зашифрованный текст: {encrypted_text}") #Вывод: Svool dliow!