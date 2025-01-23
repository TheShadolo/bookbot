def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document.")
    print()
    
    lower_string = file_contents.lower()
    char_count = {}
    for x in lower_string:
        if x.isalpha():
            char_count[x] = char_count.get(x, 0) + 1
        sorted_char_count = {key: value for key, value in 
                             sorted(char_count.items(), 
                                    key=lambda item: item[1], 
                                    reverse=True)}
    for x in sorted_char_count:
        print(f"The '{x}' character was found {sorted_char_count[x]} times.")


main()