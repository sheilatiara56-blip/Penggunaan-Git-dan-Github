def TowerOfHanoi(n, fromRod, toRod, auxRod):
    if n == 0:
        return
    TowerOfHanoi(n-1, fromRod, auxRod, toRod)
    print("Disk", n, " moved from ", fromRod, " to ", toRod)
    TowerOfHanoi(n-1, auxRod, toRod, fromRod)

if __name__ == "__main__":
    n = 3
    
    # A, C, B are the name of rods
    TowerOfHanoi(n, 'A', 'C', 'B')