# Rio Fandia Aryadi
# 241011400059
# 02TPLE001

#16 - Function Arguments & Return

def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"

def add(a, b):
    """Function to add two numbers."""
    return a + b

def biodata(nama, nim, kelas):
    """Function to display student biodata."""
    return f"Nama: {nama}, NIM: {nim}, Kelas: {kelas}"

def main():
    # Greeting
    name = "Rio Fandia Aryadi"
    greeting = greet(name)
    print(greeting)

    # Addition
    num1 = 5
    num2 = 10
    result = add(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")

    # Biodata
    nama = "Rio Fandia Aryadi"
    nim = "241011400059"
    kelas = "02TPLE001"
    biodata_info = biodata(nama, nim, kelas)
    print(biodata_info)

if __name__ == "__main__":
    main()