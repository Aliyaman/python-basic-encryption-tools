from string import ascii_lowercase as letters
letters_reverse = letters[::-1]
encrypted = []
#test
def atbash(text):
    text = text.replace(" ","")
    for i in text:
        if i in letters:
            encrypted.append(letters_reverse[letters.index(i)])
        else:
            print(f"String {i} is passed because its not in ascii letters")
    print(f"Encrypted/decrypted text is {"".join(encrypted)}")
