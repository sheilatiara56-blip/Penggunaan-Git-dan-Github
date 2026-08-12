def bubble_sort_ascending(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

data = [2,5,0,7,1,1,3,5,8,9,]

print("Data sebelum disort:",data)
sorted_data = bubble_sort_ascending(data)
print("Data setelah disort:",sorted_data)