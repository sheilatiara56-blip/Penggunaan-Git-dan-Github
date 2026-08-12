def registrasi_produk(nama, kategori, harga, kode):
    if harga <= 500000:
        print("Harga produk tidak valid")
        return None
    if len(kode) < 6:
        print("Kode produk tidak valid")
        return None

    produk = {
        "nama": nama,
        "kategori": kategori,
        "harga": harga,
        "kode": kode,
        "status": "tersedia"
}
    return produk

inventaris = []

for i in range(2):
    nama = input("Masukkan nama produk: ")
    kategori = input("Masukkan kategori produk: ")
    harga = int(input("Masukkan harga produk: "))
    kode = input("Masukkan kode produk: ")

    produk = registrasi_produk(nama, kategori, harga, kode)
    if produk:
        inventaris.append(produk)
    else:
        print("Gagal menambahkan produk ke inventaris")

for produk in inventaris:
    print(produk)

def filter_data(data, kategori, min_harga, max_harga):
    hasil = []
    for produk in data:
        if produk["harga"] >= min_harga and produk["harga"] <= max_harga and produk["kategori"] == kategori:
         hasil.append(produk)
    return hasil

data_produk = [
    {'nama': 'Keyboard', 'kategori': 'Input', 'harga': 1500000},
    {'nama': 'Mouse', 'kategori': 'Input', 'harga': 800000},
    {'nama': 'Monitor', 'kategori': 'Display', 'harga': 2500000}
]

kategori = input("Masukkan kategori: ")
min_harga = int(input("Masukkan harga minimum: "))
max_harga = int(input("Masukkan harga maksimum: "))

hasil = filter_produk(data_produk, kategori, min_harga, max_harga)

if hasil:
    for item in hasil:
        print(item)
else:
    print("Tidak ada produk yang sesuai")