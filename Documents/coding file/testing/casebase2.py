from collections import deque
import random

# ============================================================
# CLASS SUSPECT
# ============================================================
class Suspect:
    def __init__(self, name, info):
        self.name = name
        self.info = info
        self.suspicion = 0

    def add_suspicion(self, value):
        self.suspicion += value

    def show(self):
        print(f"Nama: {self.name}")
        print(f"Info: {self.info}")
        print(f"Tingkat Kecurigaan: {self.suspicion}")


# ============================================================
# TREE NODE
# ============================================================
class DecisionNode:
    def __init__(self, decision):
        self.decision = decision
        self.children = []

    def add_child(self, child):
        self.children.append(child)


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
# GRAPH LOKASI
# ============================================================
graph = {
    "Rumah Korban": ["Gang", "Taman"],
    "Gang": ["Rumah Korban", "Sungai"],
    "Taman": ["Rumah Korban"],
    "Sungai": ["Gang"]
}

current_place = "Rumah Korban"
visited_places = set()


# ============================================================
# TREE INVESTIGASI
# ============================================================
root = DecisionNode("Mulai Investigasi")

# Cabang utama
periksa_tkp = DecisionNode("Periksa TKP")
interogasi = DecisionNode("Interogasi Saksi")
periksa_sungai = DecisionNode("Periksa Sungai")

root.add_child(periksa_tkp)
root.add_child(interogasi)
root.add_child(periksa_sungai)

# Cabang TKP
jejak = DecisionNode("Cari Jejak Sepatu")
jendela = DecisionNode("Periksa Jendela")

periksa_tkp.add_child(jejak)
periksa_tkp.add_child(jendela)

# Cabang Sungai
pisau = DecisionNode("Cari Pisau Berdarah")
semak = DecisionNode("Periksa Semak")

periksa_sungai.add_child(pisau)
periksa_sungai.add_child(semak)


# ============================================================
# DATA BUKTI
# ============================================================
evidence_list = [
    (
        "Topi milik Reno ditemukan di halaman rumah korban",
        "Reno",
        10
    ),

    (
        "Rekaman CCTV menunjukkan Dimas mengelilingi rumah korban",
        "Dimas",
        25
    ),

    (
        "Botol minum Salsa ditemukan di depan rumah korban",
        "Salsa",
        5
    ),

    (
        "Teman Dimas mengaku bersama Dimas saat kejadian",
        "Dimas",
        -15
    ),

    (
        "Pisau berdarah ditemukan dengan sidik jari Dimas",
        "Dimas",
        50
    )
]


# ============================================================
# HASH TABLE / DICTIONARY
# ============================================================
evidence_table = {
    "Topi": "Topi milik Reno ditemukan di TKP",
    "Pisau": "Pisau memiliki sidik jari Dimas",
    "Botol": "Botol minum Salsa ditemukan di depan rumah"
}


# ============================================================
# DICTIONARY PENYIMPAN BUKTI
# ============================================================
suspect_evidence = {
    "Reno": [],
    "Dimas": [],
    "Salsa": []
}


# ============================================================
# STACK RIWAYAT
# ============================================================
history_stack = []


# ============================================================
# QUEUE SAKSI
# ============================================================
witness_queue = deque()

witness_queue.append("Pak RT")
witness_queue.append("Satpam")
witness_queue.append("Penjual Warung")


# ============================================================
# SINGLE LINKED LIST
# ============================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def show(self):
        current = self.head

        while current:
            print("->", current.data)
            current = current.next


travel_history = SingleLinkedList()


# ============================================================
# DOUBLE LINKED LIST
# ============================================================
class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = DoubleNode(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def show_forward(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next


case_notes = DoubleLinkedList()


# ============================================================
# CIRCULAR LINKED LIST
# ============================================================
class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = CircularNode(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head

        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def show(self):
        if not self.head:
            return

        current = self.head

        while True:
            print(current.data)
            current = current.next

            if current == self.head:
                break


shift_police = CircularLinkedList()
shift_police.add("Polisi A")
shift_police.add("Polisi B")
shift_police.add("Polisi C")


# ============================================================
# REKURSIF TREE
# ============================================================
def show_tree(node, level=0):
    print("   " * level + "- " + node.decision)

    for child in node.children:
        show_tree(child, level + 1)


# ============================================================
# PINDAH LOKASI
# ============================================================
def move_place():
    global current_place

    print(f"\nLokasi sekarang: {current_place}")

    connected = graph[current_place]

    print("Lokasi yang bisa dikunjungi:")

    for i, place in enumerate(connected):
        print(f"{i+1}. {place}")

    pilih = int(input("Pilih lokasi: ")) - 1

    current_place = connected[pilih]

    visited_places.add(current_place)
    travel_history.add(current_place)

    print(f"Berpindah ke {current_place}")


# ============================================================
# INVESTIGASI TREE
# ============================================================
def investigasi(node):
    print(f"\nInvestigasi: {node.decision}")

    history_stack.append(node.decision)
    case_notes.add(node.decision)

    if len(node.children) == 0:
        print("Tidak ada investigasi lanjutan")
        return

    for i, child in enumerate(node.children):
        print(f"{i+1}. {child.decision}")

    pilih = int(input("Pilih investigasi: ")) - 1

    investigasi(node.children[pilih])


# ============================================================
# CARI BUKTI
# ============================================================
def search_evidence():

    chance = random.randint(1, 100)

    if chance <= 35:
        print("\nTidak ada bukti ditemukan")
        history_stack.append("Pencarian gagal")
        return

    evidence = random.choice(evidence_list)

    evidence_name, suspect_name, suspicion_change, trust = evidence

    print("\n=== BUKTI DITEMUKAN ===")
    print(evidence_name)

    print(f"Tingkat kepercayaan bukti: {trust}%")

    # STATUS BUKTI
    if trust >= 80:
        print("Status: Sangat terpercaya")

    elif trust >= 60:
        print("Status: Cukup terpercaya")

    elif trust >= 40:
        print("Status: Meragukan")

    else:
        print("Status: Sangat meragukan")

    history_stack.append(evidence_name)

    suspect_evidence[suspect_name].append(evidence_name)

    # PENGARUH KECURIGAAN
    final_suspicion = int(
        suspicion_change * (trust / 100)
    )

    for suspect in suspects:

        if suspect.name == suspect_name:

            suspect.add_suspicion(final_suspicion)

            print(
                f"Kecurigaan {suspect.name} "
                f"bertambah {final_suspicion}"
            )


# ============================================================
# RANKING
# ============================================================
def ranking():
    for i in range(len(suspects)):
        for j in range(len(suspects) - i - 1):
            if suspects[j].suspicion < suspects[j + 1].suspicion:
                suspects[j], suspects[j + 1] = suspects[j + 1], suspects[j]

    print("\n=== RANKING TERSANGKA ===")

    for suspect in suspects:
        suspect.show()
        print()


# ============================================================
# RIWAYAT STACK
# ============================================================
def show_history():
    print("\n=== RIWAYAT INVESTIGASI ===")

    for history in reversed(history_stack):
        print("-", history)


# ============================================================
# PANGGIL SAKSI
# ============================================================
def call_witness():
    if len(witness_queue) == 0:
        print("Tidak ada saksi lagi")
        return

    current = witness_queue.popleft()

    print(f"\nMemanggil saksi: {current}")


# ============================================================
# HASH TABLE SEARCH
# ============================================================
def search_hash():
    key = input("Masukkan nama bukti: ")

    result = evidence_table.get(key)

    if result:
        print(result)
    else:
        print("Bukti tidak ditemukan")


# ============================================================
# SAVE FILE
# ============================================================
def save_result():
    with open("hasil_investigasi.txt", "w") as file:
        file.write("HASIL INVESTIGASI\n\n")

        for suspect in suspects:
            file.write(
                f"{suspect.name}: {suspect.suspicion}\n"
            )

    print("Data berhasil disimpan")


# ============================================================
# MENU UTAMA
# ============================================================
while True:
    print("\n============================")
    print("     GAME DETEKTIF")
    print("============================")
    print("1. Kronologi")
    print("2. Lihat Tersangka")
    print("3. Pindah Lokasi")
    print("4. Investigasi")
    print("5. Cari Bukti")
    print("6. Ranking Tersangka")
    print("7. Riwayat Investigasi")
    print("8. Panggil Saksi")
    print("9. Data Bukti")
    print("10. Lihat Tree")
    print("11. Riwayat Perjalanan")
    print("12. Save File")
    print("13. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("\nKorban ditemukan meninggal di rumahnya.")
        print("Rumah korban berantakan dan ditemukan jejak sepatu.")

    elif pilihan == "2":
        print("\n=== DATA TERSANGKA ===")

        for suspect in suspects:
            suspect.show()
            print()

    elif pilihan == "3":
        move_place()

    elif pilihan == "4":
        investigasi(root)

    elif pilihan == "5":
        search_evidence()

    elif pilihan == "6":
        ranking()

    elif pilihan == "7":
        show_history()

    elif pilihan == "8":
        call_witness()

    elif pilihan == "9":
        search_hash()

    elif pilihan == "10":
        print("\n=== TREE INVESTIGASI ===")
        show_tree(root)

    elif pilihan == "11":
        print("\n=== RIWAYAT PERJALANAN ===")
        travel_history.show()

    elif pilihan == "12":
        save_result()

    elif pilihan == "13":
        print("Game selesai")
        break

    else:
        print("Pilihan tidak valid")
