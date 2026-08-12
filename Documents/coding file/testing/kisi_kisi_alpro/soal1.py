def input_pilihan():
    while True:
        pilihan = input("Pilih kertas/batu/gunting: ").lower().strip()
        if pilihan in ["kertas", "batu", "gunting"]:
            return pilihan
        print("Pilihan tidak valid. Silakan coba lagi.")

def tentukan_pemenang(p1, p2):
    if p1 == p2:
        return "Seri"
    elif (p1 == "kertas" and p2 == "batu") or \
         (p1 == "batu" and p2 == "gunting") or \
         (p1 == "gunting" and p2 == "kertas"):
        return "Pemain 1"
    else:
        return "Pemain 2"

def satu_ronde(no):   # ✅ tambah parameter
    p1 = input_pilihan()
    p2 = input_pilihan()
    hasil = tentukan_pemenang(p1, p2)
    return [no, p1, p2, hasil]   # ✅ list 2D

def main_game():
    print("=== Permainan Kertas, Batu, Gunting ===")
    hasil_semua = []

    jumlah_ronde = int(input("Masukkan jumlah ronde: "))
    for i in range(jumlah_ronde):
        print(f"\nRonde ke-{i+1}")
        hasil_semua.append(satu_ronde(i+1))  # ✅ kirim nomor ronde

    return hasil_semua

def tampilkan_data(data):
    if not data:
        print("Data kosong!, Belum ada Pertandingan")
        return

    print("\nNo\tP1\t\tP2\t\tHasil")
    print("-"*40)

    for baris in data:
        no, p1, p2, hasil = baris
        print(f"{no}\t{p1}\t\t{p2}\t\t{hasil}")

def main():
    hasil = main_game()
    tampilkan_data(hasil)

main()