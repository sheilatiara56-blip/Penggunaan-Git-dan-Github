import time

def input_pilihan():
    while True:
        pilihan = input("Pilih kertas/batu/gunting:").lower().strip()
        if pilihan in ["kertas", "batu", "gunting"]: # buat hemat waktu, daripada nulis panjang-panjang
            return pilihan
        print("Pilihan tidak valid. Silakan coba lagi.")

def tentukan_pemenang(p1, p2):
    if p1 == p2:
        return "seri"
    elif (p1 == "kertas" and p2 == "batu") or \
         (p1 == "batu" and p2 == "gunting") or \
         (p1 == "gunting" and p2 == "kertas"):
        return "pemain 1"
    else:
        return "pemain 2"

def satu_ronde(no):
    p1 = input_pilihan()
    p2 = input_pilihan()
    hasil = tentukan_pemenang(p1, p2)
    return [no, p1, p2, hasil]

def main_game():
    print("=== Permainan Kertas, Batu, Gunting ===")
    hasil_semua = []

    jumlah_ronde = int(input("masukkan jumlah ronde: "))
    for i in range (jumlah_ronde):
        print(f"\nRonde ke-{i+1}")
        hasil_semua.append(satu_ronde(i+1))

    return hasil_semua

def tampilkan_data(data):
    if not data:
        print("Data kosong!, Belum ada Pertandingan")
        return 
        
        print("\nNo\t\t\P1\t\t\tP2\t\t\t\Hasil")
        print("-"*50)
    
    for baris in data:
        no, p1, p2, hasil = baris
        print(f"{no}\t\t{p1}\t\t{p2}\t\t{hasil}")


def main():
    hasil = main_game()
    tampilkan_data(hasil)
    print("\nHasil semua ronde:", hasil)

main()
    