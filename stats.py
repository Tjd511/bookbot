def get_book_text(f_path):
    with open(f_path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(f_path):
    counter = 0
    words = get_book_text(f_path).split()
    for word in words:
        counter += 1
    return counter

def get_characters(f_path):
    char_count = {}

    for char in get_book_text(f_path):
        l_char = char.lower()
        if l_char in char_count:
            char_count[l_char] += 1
        else:
            char_count[l_char] = 1
    return char_count

def sort_on(f_path):
    num_list = {}
    sort_list = []
    items = list(get_characters(f_path).items())
    for item in items:
        if item[0].isalpha():
            num_list = {"char": item[0], "num": item[1]}
            sort_list.append(num_list)
    sort_list.sort(reverse=True, key=lambda num_list: num_list["num"])
    return sort_list
