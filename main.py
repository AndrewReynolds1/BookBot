def getbooktext(path):
    with open(path) as f:
        return f.read()

def getwordCount(content):
    words = content.split()
    return len(words)

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def main():

    # Define the bookpath
    bookpath = "books/frankenstein.txt"
    
    # Get the text from the file
    text = getbooktext(bookpath)

    # Get the word count
    word_count = getwordCount(text)
    print(f"{word_count} words found in the document \n")

    # Get Character Count
    countOfCharacters = get_chars_dict(text)

    chars_sorted_list = chars_dict_to_sorted_list(countOfCharacters)

    # Sort Dictionary
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

if __name__ == "__main__":
    main()