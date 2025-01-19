def adjust_key_length(text, key):
    text = text.replace(" ", "")
    
    text_length = len(text)
    key_length = len(key)

    if key_length > text_length:
        return key[:text_length]

    repetitions = text_length // key_length
    remainder = text_length % key_length
    
    adjusted_key = key * repetitions + key[:remainder]
    return adjusted_key

"""
text = "anen"
key = "baben"
adjusted_key = adjust_key_length(text, key)
print(f"Text: {text}")
print(f"Original key: {key}")
print(f"Adjusted key: {adjusted_key}")
"""