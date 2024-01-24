def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    chars_dict = get_chars_dict(text)
    sorted_char_list = sort_chars_dict(chars_dict)
    print_sorted_chars(sorted_char_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text_string):
    words = text_string.split()
    return len(words)

def get_chars_dict(text_string):
    new_dict = {}
    for l in text_string:
        lowered = l.lower()
        if lowered in new_dict:
            new_dict[lowered] += 1
        else:
            new_dict[lowered] = 1
    return new_dict

def second_item(tuple):
    return tuple[1]

def sort_chars_dict(dict):
    char_list = []
    for c in dict:
        if c.isalpha():
            char_list.append((c,dict[c]))
    char_list.sort(reverse=True,key=second_item)
    return char_list
    
def print_sorted_chars(list):
    for l in list:
        print(f"The '{l[0]}' character was found {l[1]} times")

main()