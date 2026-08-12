class Suspect:
    def __init__(self, name, info):
        self.name = name
        self.info = info
        self.suspicion = 0

    def add_suspicion(self, value):
        self.suspicion += value

    def show(self):
        print(f"Nama: {self.name}")
        print(f"info: {self.info}")
        print(f"Tingkat Kecurigaan: {self.suspicion}")


# ============================================================
# DATA TERSANGKA
# ============================================================
suspect1 = Suspect(
    "Reno",
    "Saksi melihat Reno lewat gang belakang TKP sebelum kejadian"
)

suspect2 = Suspect(
    "Dimas",
    "Dimas terlihat keluar dari area sekitar TKP dengan tergesa-gesa"
)

suspect3 = Suspect(
    "Salsa",
    "Salsa terlihat melewati taman dekat lokasi kejadian"
)
suspects = [suspect1, suspect2, suspect3]


# ============================================================
# DATA BUKTI
# ============================================================
evidence_list = [
    ("Topi milik Reno ditemukan di halaman rumah korban", "Reno", 10),
    ("Rekaman CCTV menunjukkan Dimas mengelinlingi rumah korban sebelum kejadian", "Dimas", 25),
    ("botol minum Salsa ditemukan di jalan depan rumah korban", "Salsa", 5),
    ("Teman Dimas mengaku bersama Dimas saat kejadian", "Dimas", -15),
    ("Pisau berdarah ditemukan di semak sungai dekat rumah korban. Setelah di cek, terdapat sidik jari dimas di gagang pisau", "Dimas", 50)
]

evidence_count = {
    "Reno": 0,
    "Dimas": 0,
    "Salsa": 0
}
history_stack = []

evidence_index = 0
visited_places = set()

# ============================================================
# MENU PROGRAM
# ============================================================

while True:
    print("\n==========================")
    print("     GAME DETEKTIF")
    print("==========================")
    print("1. Kronologi")
    print("2. Investigasi")
    print("3. Cari Bukti")
    print("4. Ranking Tersangka")
    print("5. Riwayat Bukti")
    print("6. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("\n===================================")
        print("     KRONOLOGI")
        print("===================================\n")
        print(
        "Korban ditemukan meninggal dunia di dalam rumahnya "
        "pada dini hari oleh salah satu tetangganya yang datang "
        "karena pintu rumah korban terbuka sejak malam sebelumnya. "
        "Ruang tengah rumah terlihat berantakan dan terdapat "
        "beberapa jejak sepatu di lantai dekat jendela belakang. "
        "Menurut keterangan warga sekitar, beberapa orang asing "
        "sempat terlihat berada di sekitar rumah korban beberapa "
        "jam sebelum kejadian."
        )
        
    # ========================================================
    # INVESTIGASI
    # ========================================================
    elif pilihan == "2":
        print("\n=== INVESTIGASI SAKSI ===")
        print("Saksi melihat beberapa orang di sekitar TKP saat sekitar waktu kejadian:\n")

        for suspect in suspects:
            suspect.show()
            print()

# ========================================================
# CARI BUKTI
# ========================================================
    elif pilihan == "3":
        if evidence_index < len(evidence_list):
            evidence_name, suspect_name, suspicion_change = evidence_list[evidence_index]
            print("\nMencari bukti di sekitar TKP...")
            visited_places.add("TKP")
            print(f"Bukti ditemukan: {evidence_name}")
            history_stack.append(evidence_name)
        # Menambah / mengurangi kecurigaan
            for suspect in suspects:
                if suspect.name == suspect_name:
                    suspect.add_suspicion(suspicion_change)

                # Jika poin bertambah
                    if suspicion_change > 0:
                        print(
                            f"Tingkat kecurigaan {suspect.name} "
                            f"bertambah +{suspicion_change}"
                        )

                # Jika poin berkurang
                    elif suspicion_change < 0:
                        print(
                            f"Tingkat kecurigaan {suspect.name} "
                            f"berkurang {suspicion_change}"
                    )
            evidence_index += 1
        else:
            print("Semua bukti sudah ditemukan.")


    # ========================================================
    # RANKING TERSANGKA
    # ========================================================
    elif pilihan == "4":
        for i in range(len(suspects)):
            for j in range(len(suspects) - i - 1):
                if suspects[j].suspicion < suspects[j + 1].suspicion:
                    suspects[j], suspects[j + 1] = suspects[j + 1], suspects[j]

        print("\n=== RANKING TERSANGKA ===\n")
        for suspect in suspects:
            suspect.show()
            print()

    elif pilihan == "5":
        print("\n=== RIWAYAT INVESTIGASI ===")
        for history in reversed(history_stack):
            print("-", history)
    # ========================================================
    # KELUAR
    # ========================================================
    elif pilihan == "6":
        print("game selesai")
        break


    else:
        print("Pilihan tidak valid")