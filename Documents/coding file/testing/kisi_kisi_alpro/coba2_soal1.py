import random

def input_pilihan():
    while True:
        pilihan = input("Pilih kertas/batu/gunting:").lower().strip()
        if pilihan in ["kertas", "batu", "gunting"]: # buat hemat waktu, daripada nulis panjang-panjang
            return pilihan
        print("Pilihan tidak valid. Silakan coba lagi.")

def pilihan_komputer():
    return random.choice(["kertas", "batu", "gunting"])

def tentukan_pemenang(p1, p2):
    if p1 == p2:
        return "seri"
    elif (p1 == "kertas" and p2 == "batu") or \
         (p1 == "batu" and p2 == "gunting") or \
         (p1 == "gunting" and p2 == "kertas"):
        return "pemain 1"
    else:
        return "pemain 2"

def satu_ronde():
    p1 = input_pilihan()
    p2 = pilihan_komputer()
    print(f"Komputer memilih: {p2}")
    hasil = tentukan_pemenang(p1, p2)
    return hasil

def main_game():
    print("=== Permainan Kertas, Batu, Gunting ===")
    hasil_semua = []

    jumlah_ronde = int(input("masukkan jumlah ronde: "))
    for i in range (jumlah_ronde):
        print(f"\nRonde ke-{i+1}")
        hasil_semua.append(satu_ronde())

    return hasil_semua

def main():
    hasil = main_game()
    print("\nHasil semua ronde:", hasil)

main()
    