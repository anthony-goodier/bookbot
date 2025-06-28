import sys
from stats import get_num_words, get_num_characters, sort_uniques


def get_book_text(filepath):
    with open(filepath) as file:
        book_text = file.read()
        return book_text


def main():
    args = sys.argv

    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = args[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    uniques = get_num_characters(book_text)
    sorted = sort_uniques(uniques)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted:
        name = item["name"]
        count = item["count"]
        if name.isalpha():
            print(f"{name}: {count}")

    print("============= END ===============")


main()
