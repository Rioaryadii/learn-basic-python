#Rio Fandia Aryadi
#241011400059
#02TPLE001

#Day10 - Sets

def main():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    print("Set 1:", set1)
    print("Set 2:", set2)

    print("Union:", set1.union(set2))
    print("Intersection:", set1.intersection(set2))
    print("Difference:", set1.difference(set2))
    print("Symmetric Difference:", set1.symmetric_difference(set2))

if __name__ == "__main__":
    main()