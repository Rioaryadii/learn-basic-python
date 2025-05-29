#Rio Fandia Aryadi
#241011400059
#02TPLE001

# 11 - Strings in Python

def main():
    name = input("Enter your name: ")

    print("\n===Name Analysis===")
    print("All uppercase:", name.upper())
    print("Character count (excluding spaces):", len(name.replace(" ", "")))

    words = name.split()
    initials = "".join([word[0].upper() for word in words])
    print("Initials:", initials)

    print("\n===Palindrome Check===")
    word = input("Enter a word or phrase: ")
    cleaned = word.replace(" ", "").lower()
    is_palindrome = cleaned == cleaned[::-1]
    print("Is it a palindrome?", is_palindrome)

if __name__ == "__main__":
    main()