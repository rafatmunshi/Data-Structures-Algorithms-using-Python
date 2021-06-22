def binarysearch(arr, low, high, key):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binarysearch(arr, mid + 1, high, key)
        else:
            return binarysearch(arr, low, mid - 1, key)
    else:
        return -1


arr = [1, 4, 5, 8, 10, 23, 45, 67, 89, 100]
print(binarysearch(arr, 0, len(arr) - 1, 98))
