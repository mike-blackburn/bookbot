def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_characters(text):
    char_dict = {}
    for char in text:
        normalized_char = f"'{char.lower()}'"
        if normalized_char not in char_dict:
            char_dict[normalized_char] = 1
        else:
            char_dict[normalized_char] += 1
    return char_dict