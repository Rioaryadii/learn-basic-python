# Rio Fandia Aryadi
# 241011400059
# 02TPLE001

# 17 - Positional, Keyword Args & Kwargs

def biodata(nama, nim, kelas):
    """Function to display student biodata."""
    return f"Nama: {nama}, NIM: {nim}, Kelas: {kelas}"

def total(*args):
    """Function to calculate the total of given numbers."""
    return sum(args)

def display_info(**kwargs):
    """Function to display information using keyword arguments."""
    info = []
    for key, value in kwargs.items():
        info.append(f"{key}: {value}")
    return ", ".join(info)

def main():
    # Biodata
    nama = "Rio Fandia Aryadi"
    nim = "241011400059"
    kelas = "02TPLE001"
    biodata_info = biodata(nama, nim, kelas)
    print(biodata_info)

    # Total of numbers
    numbers = [10, 20, 30, 40]
    total_result = total(*numbers)
    print(f"Total of {numbers} is: {total_result}")

    # Displaying information using keyword arguments
    info = display_info(nama=nama, nim=nim, kelas=kelas)
    print(f"Student Info: {info}")

if __name__ == "__main__":
    main()