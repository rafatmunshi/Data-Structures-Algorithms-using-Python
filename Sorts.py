def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = (low - 1)

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pivotindex = partition(arr, low, high)
        quickSort(arr, low, pivotindex - 1)
        quickSort(arr, pivotindex + 1, high)


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    left = [0] * n1
    right = [0] * n2

    for i in range(0, n1):
        left[i] = arr[l + i]

    for j in range(0, n2):
        right[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def countSort(arr):
    output = [0 for i in range(0, len(arr))]
    count = [0 for i in range(10)]
    for i in range(0, len(arr)):
        count[arr[i]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(len(arr)):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    return output

def bucketSort(arr):
    arr2=[]
    slots= 10
    for i in range(slots):
        arr2.append([])
    for j in arr:
        index= int(slots*j)
        arr2[index].append(j)
    for i in range(slots):
        arr2[i]= bubbleSort(arr2[i])
    k=0
    for i in range(slots):
        for j in range(len(arr2[i])):
            arr[k] = arr2[i][j]
            k+=1
    return arr

#arr = [9, 3, 7, 2, 6, 4, 8, 0, 1, 5, 3, 4, 6, 3, 2, 7, 8]

#arr = countSort(arr)

# arr= [0.235, 0.569, 0.279, 0.953, 0.174, 0.3739]
arr= bucketSort(arr)
# print(arr)
for i in range(len(arr)):
    print('%d' % arr[i], end=' ')
