hash_table = [None] * 5

def insert(key):
    index = key % 5
    hash_table[index] = key

insert(7)
insert(12)

print(hash_table)