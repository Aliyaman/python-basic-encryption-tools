from string import ascii_letters
from vigenere.keyAdjust import adjust_key_length

possible_options = ["e","d"]
text_index = []
key_index = []

def get_index(text,which):
    text = text.lower()
    if which == "text":
        for i in text:
            text_index.append(ascii_letters.index(i))
    elif which == "key":
        for i in text:
            key_index.append(ascii_letters.index(i))
    

def vigenere(text,key,option):
    if option == "e":
        adjusted_key = adjust_key_length(text,key)    
        get_index(text,"text")
        get_index(adjusted_key,"key")
        encrypt_index = [x+y for x,y in zip(text_index,key_index)]
        key_index.clear()
        for i in encrypt_index:
            if i > 26:
                i -= 26
                key_index.append(ascii_letters[i].lower())
            elif i<26:
                i+=26
                key_index.append(ascii_letters[i].lower())
        print(f"Text encypted with key {key} is",end=":")
        print("".join(key_index))

    elif option == "d":
        adjusted_key = adjust_key_length(text,key)    
        get_index(text,"text")
        get_index(adjusted_key,"key")
        encrypt_index = [x-y for x,y in zip(text_index,key_index)]
        key_index.clear()
        for i in encrypt_index:
            if i > 26:
                i -= 26
                key_index.append(ascii_letters[i].lower())
            elif i<26:
                i+=26
                key_index.append(ascii_letters[i].lower())
        print(f"Text decrypted with key {key} is",end=":")
        print("".join(key_index))
    else:
        raise ValueError(f"option value can only be (e)ncrypt or (d)ecrypt.\nBut you choose {option}")