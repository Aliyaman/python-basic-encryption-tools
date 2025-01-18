from string import ascii_letters
harfler = []
enc_msg = []
decrypt = []
mesaj = []

def caesar(key,kelime):
  for harf in kelime:
    harfler.append(harf)

  for i in harfler:
    k = int(ascii_letters.index(i))
    enc = k + key
    enc_msg.append(ascii_letters[enc].lower())
  
  encrypted_text = "".join(enc_msg)
  print(f"Plain Text:{kelime}")
  print(f"Encrypted Text:{encrypted_text}, Key:{key}")
  return encrypted_text
