# Rio Fandia Aryadi
# 241011400059
# 02TPLE001

# 19 - Lambda Function

def main():
    add = lambda a, b: a + b
    print("sum 3 + 5 =", add(3, 5))

    numbers = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x ** 2, numbers))
    print("Squares of numbers:", squares)

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print("Even numbers:", even_numbers)

    data = [
        {"name": "Rio", "age": 20},
        {"name": "Budi", "age": 22},
        {"name": "Cici", "age": 19}
    ]
    sorted_data = sorted(data, key=lambda x: x["age"])
    print("Sorted data by age:", sorted_data)

if __name__ == "__main__":
    main()