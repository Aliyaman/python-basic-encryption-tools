def adjust_key_length(text, key):
    # Boşlukları kaldır
    text = text.replace(" ", "")
    
    text_length = len(text)
    key_length = len(key)

    # Eğer key text'ten uzunsa, text uzunluğuna kadar kısalt
    if key_length > text_length:
        return key[:text_length]

     # Eğer key text'ten kısaysa, text uzunluğuna ulaşana kadar tekrarla
    repetitions = text_length // key_length
    remainder = text_length % key_length
    
    adjusted_key = key * repetitions + key[:remainder]
    return adjusted_key

# Test edelim
text = "anen"  # boşluklu bir text
key = "baben"
adjusted_key = adjust_key_length(text, key)
print(f"Text: {text}")
print(f"Original key: {key}")
print(f"Adjusted key: {adjusted_key}")
