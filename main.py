
from stats import get_num_words
from stats import get_characters
from stats import sort_on
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

f_path = sys.argv[1]

def main(f_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {f_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(f_path)} total words" )
    print("--------- Character Count -------")
    for i in sort_on(f_path):
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main(f_path)
