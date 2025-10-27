from stats import get_num_words, get_num_characters, get_sorted_list


def get_book_text(path):
    with open(path) as f:
        return f.read()

def format_report(path, num_words, sorted_list):
    print("======== BOOKBOT ========")
    print(f"Analyzing book found at {path}...")
    print("------- Word Count ------")
    print(f"Found {num_words} total words")
    print("---- Character Count ----")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")


    print("========== END ==========")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars_dict = get_num_characters(text)
    sorted_dict_list = get_sorted_list(num_chars_dict)
    # print(f"Found {num_words} total words")
    # for char in num_chars_dict:
    #     print(f"{char}: {num_chars_dict[char]}")
    # print(sorted_dict_list)
    format_report(book_path, num_words, sorted_dict_list)

main()