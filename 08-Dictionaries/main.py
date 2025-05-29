#Rio Fandia Aryadi
#241011400059
#02TPLE001

#08 - Dictionaries in Python

def main():
    students = {
        "Name": "Rio",
        "NIM": "241011400059",
        "Class": "02TPLE001",
        "Age": 20,
        "Hobby": "Reading",
        "Major": "Computer Science"
    }
    print("Student Information:")
    for key, value in students.items():
        print(f"{key}: {value}")
    
if __name__ == "__main__":
    main()