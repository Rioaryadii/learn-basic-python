#Rio Fandia Aryadi
#241011400059
#02TPLE001

#15 - Set Operation Practice 2

def main():
    ekskul_paskibra = {"Alya", "Budi", "Cici", "Doni", "Eka"}
    ekskul_pramuka = {"Budi", "Cici", "Doni", "Fajar", "Gina"}

    print("=== Daftar Anggota Ekstrakurikuler ===")
    print("Anggota Paskibra:", ekskul_paskibra)
    print("Anggota Pramuka:", ekskul_pramuka)

    print("Siswa yang mengikuti keduanya:", ekskul_paskibra & ekskul_pramuka)
    print("Siswa yang hanya mengikuti Paskibra:", ekskul_paskibra - ekskul_pramuka)
    print("Siswa yang hanya mengikuti Pramuka:", ekskul_pramuka - ekskul_paskibra)

if __name__ == "__main__":
    main()