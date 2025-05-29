#Rio Fandia Aryadi
#241011400059
#02TPLE001

#07 - Lists in Python

def main():
    pets = ["cat", "dog", "bird"]
    pets.append("fish")
    pets.remove("dog")

    print("My pets are:")
    for pet in pets:
        print(pet)

if __name__ == "__main__":
    main()