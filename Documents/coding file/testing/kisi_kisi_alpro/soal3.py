data = [
    ["Andi", 80],
    ["Budi", 95],
    ["Cici", 85],
    ["Dodi", 70]
]

def bubble_sort_descending(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][1] < data[j+1][1]:  # bandingkan nilai (index 1)
                data[j], data[j+1] = data[j+1], data[j]  # tukar posisi
    return data

data_copy = data.copy() # buat salin data asli
hasil = bubble_sort_descending(data_copy)

for i in hasil:
    print(f"{i[0]} - {i[1]}")

# cari nilai tertinggi
nilai_tertinggi = hasil[0][1]

for i in hasil:
    if i[1] == nilai_tertinggi:
        print(f"Nilai tertinggi: {i[0]} - {i[1]}") 

