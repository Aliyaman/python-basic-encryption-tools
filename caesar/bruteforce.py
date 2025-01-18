from string import ascii_letters
harfler = []
enc_msg = []
decrypt = []
mesaj = []

def beautify(beaut):
  k = "".join(beaut)
  mesaj.append(k)

def brute(kelime):
    for letter in kelime:
        enc_msg.append(letter)
    """
    for b in enc_msg:
        if b == "m":
            enc_msg[enc_msg.index(b)] = "b"
    """
    def brutee(crypto):
        for keys in range(1,26):
            for i in crypto:
                k = int(ascii_letters.index(i))
                dec = k - keys
                if dec < 0:
                    dec = dec + 26
                if dec > 26:
                    dec = dec -26
                decrypt.append(ascii_letters[dec].lower())
            beautify(decrypt)
            decrypt.append(i)
            decrypt.clear()

    brutee(enc_msg)
    print(mesaj)
    for a in mesaj:
        sira = mesaj.index(a)+1
        print(f"Text: {a}, key={sira}")
    