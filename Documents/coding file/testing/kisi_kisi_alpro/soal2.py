def tampilkan_data(data):
    if not data:
        print("Data kosong!")
        return

    print("Nama\tNilai")
    print("-" * 20)

    for baris in data:
        print(f"{baris[0]}\t{baris[1]}")

def main():
    data = []

    n = int(input("Jumlah data: "))

    for i in range(n):
        nama = input("Nama: ")
        nilai = int(input("Nilai: "))
        data.append([nama, nilai])

    tampilkan_data(data)

main()