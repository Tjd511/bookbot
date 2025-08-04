
from stats import get_num_words
from stats import get_characters
from stats import sort_on
#from stats import sorted_list

def main(f_path):
      print("============ BOOKBOT ============")
      print("Analyzing book found at books/frankenstein.txt...")
      print("----------- Word Count ----------")
      print(f"Found {get_num_words(f_path)} total words" )
      print("--------- Character Count -------")
      for i in sort_on(f_path):
          print(f"{i['char']}: {i['num']}")
      print("============= END ===============")

main("books/frankenstein.txt")
