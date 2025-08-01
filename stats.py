def get_num_words(f_path):
    counter = 0
    words = get_book_text(f_path).split()
    for word in words:
        counter += 1
    return counter
