def get_book_text(f_path):
    with open(f_path) as f:
        file_contents = f.read()
        return file_contents


def word_count(f_path):
    counter = 0
    words = get_book_text(f_path).split()
    for word in words:
        counter += 1
    return counter


def main(f_path):
      print(f"{word_count(f_path)} words found in the document" )

main("books/frankenstein.txt")
