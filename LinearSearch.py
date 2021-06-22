def linearsearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


arr = [3, 6, 98, 23, 45, 8, 24, 9]
print(linearsearch(arr, 96))
