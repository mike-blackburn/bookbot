from stats import get_num_words, get_num_characters


def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars_dict = get_num_characters(text)
    print(f"Found {num_words} total words")
    for char in num_chars_dict:
        print(f"{char}: {num_chars_dict[char]}")

main()