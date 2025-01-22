def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)
    print(f"Word count: {word_count}")
    
    lower_string = file_contents.lower()
    char_count = {}
    for x in lower_string:
        char_count[x] = char_count.get(x, 0) + 1
    print(char_count)

main()