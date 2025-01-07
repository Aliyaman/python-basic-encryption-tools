from string import ascii_letters
kelime = "dvyk" #enter your text to decrypt without using space
harfler = []
enc_msg = []
decrypt = []
mesaj = []

def beautify(beaut):
  k = "".join(beaut)
  mesaj.append(k)

for letter in kelime:
  enc_msg.append(letter)

for b in enc_msg:
  if b == "i":
    enc_msg[enc_msg.index(b)] = "t"

def brute(crypto):
  for keys in range(1,26):
    for i in crypto:
      k = int(ascii_letters.index(i))
      dec = k - keys
      if dec < 0:
        dec = dec + 26
      if dec > 25:
        dec = dec -26
      decmsg = decrypt.append(ascii_letters[dec].lower())
    beautify(decrypt)
    decrypt.append(i)
    decrypt.clear()

brute(enc_msg)

for a in mesaj:
  sıra = mesaj.index(a)+1
  print(f"Text: {a}, key={sıra}")
 