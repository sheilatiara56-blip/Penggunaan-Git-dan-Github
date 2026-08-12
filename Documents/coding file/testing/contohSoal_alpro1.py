#soal 1
Film = [["Avengers: Endgame", 50000],
["Spider-Man: No Way Home", 45000],
["Doctor Strange in the Multiverse of Madness", 40000],
["Black Panther", 35000],
["Captain Marvel", 60000]
]

print("== Daftar Film ==")
for i in range(len(Film)):
    print(i +  1,Film[i][0],Film[i][1])

#soal 2

tontonan = []

while True:
    pilihan = int(input("Masukkan nomor film yang ingin ditonton (atau '0' untuk lanjut): "))
    if pilihan >= 1 and pilihan <= len(Film):
        jumlah = int(input("Masukkan jumlah tiket yang ingin dibeli:"))
        judul_film = Film[pilihan - 1][0]
        harga_tiket = Film[pilihan - 1][1]
      
        tontonan.append((judul_film, jumlah, harga_tiket))
        total_harga = harga_tiket * jumlah
        print(f"Anda memilih {judul_film} dengan jumlah {jumlah} tiket. Harga per tiket: {harga_tiket}")
    
    elif pilihan == 0:
        print("Lanjutkan.")
        break
        
    else:
        print("Pilihan tidak valid.")

print("\n Daftar Pesanan:")
total = 0
for item in tontonan:
    judul_film, jumlah, harga_tiket = item
    subtotal = jumlah * harga_tiket
    total += subtotal
    print(f"{judul_film} - Jumlah: {jumlah} - Harga per tiket: {harga_tiket} - Subtotal: {subtotal}")

print("Total:", total)

#soal 3

diskon = 0
if total >= 150000:
    diskon = 0.20 * total
elif total >= 100000:
    diskon = 0.10 * total
else:
    diskon = 0
total_bayar = total - diskon
print(f"Diskon:Rp {diskon:.0f}")
print(f"Total Bayar:Rp {total_bayar:.0f}")