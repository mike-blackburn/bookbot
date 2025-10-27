def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_characters(text):
    char_dict = {}
    for char in text:
        # normalized_char = f"'{char.lower()}'"
        normalized_char = char.lower()
        if normalized_char not in char_dict:
            char_dict[normalized_char] = 1
        else:
            char_dict[normalized_char] += 1
    return char_dict

def sort_on_helper(items):
    return items["num"]
def get_sorted_list(dict_to_sort):
    # print(dict_to_sort)
    sorted_list = []
    for key, value in dict_to_sort.items():
        if key.isalpha():
            sorted_list.append({"char": key, "num": value})


    sorted_list.sort(reverse=True, key=sort_on_helper)
    return sorted_list