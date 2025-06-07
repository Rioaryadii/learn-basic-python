#Rio Fandia Aryadi
#241011400059
#02TPLE001

#14 - Set Operation Practice

def main():
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}

    print("Set A:", set_a)
    print("Set B:", set_b)

    # Union
    union_set = set_a | set_b
    print("Union:", union_set)

    # Intersection
    intersection_set = set_a & set_b
    print("Intersection:", intersection_set)

    # Difference
    difference_set = set_a - set_b
    print("Difference (A - B):", difference_set)

    # Symmetric Difference
    symmetric_difference_set = set_a ^ set_b
    print("Symmetric Difference:", symmetric_difference_set)

    # Checking membership
    print("Is 3 in Set A?", 3 in set_a)
    print("Is 6 in Set B?", 6 in set_b)

if __name__ == "__main__":
    main()