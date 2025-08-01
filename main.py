def get_book_text(f_path):
    with open(f_path) as f:
        file_contents = f.read()
        return file_contents

from stats import get_num_words

def main(f_path):
      print(f"{get_num_words(f_path)} words found in the document" )

main("books/frankenstein.txt")
