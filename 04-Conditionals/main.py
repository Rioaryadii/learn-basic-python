#Rio Fandia Aryadi
#241011400059
#02TPLE001

#04 - Conditionals

def main():
    score = int(input("Enter your score: "))
    if score >= 90:
        print("You got an A!")
    elif score >= 80:
        print("You got a B!")
    elif score >= 70:
        print("You got a C!")
    elif score >= 60:
        print("You got a D!")
    else:
        print("You got an F!")

if __name__ == "__main__":
    main()