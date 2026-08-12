class Minuman:
    def __init__(self, nama, rasa, rating):
        self.nama = nama
        self.rasa = rasa
        self.rating = rating

    def deskripsi_minuman(self):
        print(f"Minuman favoritku: {self.nama}, rasa: {self.rasa}, rating: {self.rating}")

    def ubah_nama(self,new_nama):
        self.nama = new_nama

    def ubah_rating(self,new_rating):
        if 0 <= new_rating <=10:
         self.rating = new_rating
        else:
         print("rating harus diantara 0 sampai 10") 


minum1 = Minuman ("susu","manis",8)

minum1.deskripsi_minuman()
minum1.ubah_nama("Latte")
minum1.ubah_rating(9)
minum1.deskripsi_minuman()