#Rio Fandia Aryadi
#241011400059
#02TPLE001

#09 - Tuples in Python

def main():
    coordinates = (9.5, 10.9)
    print("Coordinates:", coordinates)

    print("X:", coordinates[0])
    print("Y:", coordinates[1])

    #Tuple unpacking
    x, y = coordinates
    print(f"Unpacked -> X: {x}, Y: {y}")

if __name__ == "__main__":
    main()
    