def main():
    num_words = 0
    chars = dict()
    with open("./books/frankenstein.txt") as f:
        for line in f.readlines():
            words = line.split()
            for word in words:
                num_words += 1
                for letter in word:
                    chars[letter.lower()] = chars.get(letter.lower(), 0) + 1
    print_report(chars, num_words)

def print_report(chars, num_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for k, v in chars.items():
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]
main()