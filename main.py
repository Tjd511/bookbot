
from stats import get_num_words
from stats import get_characters

def main(f_path):
      #print(f"{get_num_words(f_path)} words found in the document" )
      print(get_characters(f_path))

main("books/frankenstein.txt")
