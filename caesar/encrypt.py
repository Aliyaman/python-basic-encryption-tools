from string import ascii_letters
harfler = []
enc_msg = []
decrypt = []
mesaj = []

def caesar(harf,key):
  enc = harf + key
  encmsg = enc_msg.append(ascii_letters[enc].lower())
  

for harf in kelime:
  harfler.append(harf)
  
for i in harfler:
  k = int(ascii_letters.index(i))
  caesar(k,key)

print(f"Original text is: {kelime}")
print(f"Encrypted text is: {"".join(enc_msg)}") 
