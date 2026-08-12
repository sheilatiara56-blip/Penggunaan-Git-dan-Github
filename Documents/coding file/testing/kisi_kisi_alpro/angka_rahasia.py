angka_rahasia = 9

def tebak_angka():
    data = []
    ronde = 1

    while True:
        tebak = int(input("Masukkan angka tebakan kamu: "))

        if tebak < angka_rahasia:
            hasil = "Terlalu rendah"
        elif tebak > angka_rahasia:
            hasil = "Terlalu tinggi"
        else:
            hasil = "Tebakan benar!"

        data.append([ronde, tebak, hasil])
        ronde += 1

        if hasil == "Tebakan benar!":
            break

    return data


def tampilkan_tabel(data):
    print("\nRonde\tTebakan\t\tHasil")
    print("-" * 30)

    for baris in data:
        print(f"{baris[0]}\t{baris[1]}\t{baris[2]}")


def bubble_sort_ascending(data):  # kecil → besar
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][1] > data[j+1][1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


def main():
    hasil = tebak_angka()

    print("\nData asli:")
    tampilkan_tabel(hasil)

    #sorting
    data_copy = hasil.copy()
    hasil_sort = bubble_sort_ascending(data_copy)

    print("\nSetelah diurutkan (kecil → besar):")
    tampilkan_tabel(hasil_sort)


main()