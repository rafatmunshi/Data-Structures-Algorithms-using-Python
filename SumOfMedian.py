# arr1, arr2- sorted
# get medians of arr1 and arr2
# m1==m2, return m1+m2
# m1<m2-
# arr1- n/2 - n-1
# arr2- 0 - n/2
# m1>m2-
# arr1- 0 - n/2
# arr2- n/2 - n-1
# sum of medians= max(arr1[0], arr2[0])+min(arr1[1], arr2[1])
# assume len(arr1)==len(arr2)
def sumofmedians(arr1, arr2):
    n = len(arr1)
    if n == 0:
        return 0
    elif n == 1:
        return (arr1[0] + arr2[0])
    elif n == 2:
        return max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])
    else:
        m1 = median(arr1)
        m2 = median(arr2)
        if m1 > m2:
            if n % 2 == 0:
                return sumofmedians(arr1[:int(n / 2) + 1], arr2[int(n / 2) - 1:])
            else:
                return sumofmedians(arr1[:int(n / 2) + 1], arr2[int(n / 2):])
        else:
            if n % 2 == 0:
                return sumofmedians(arr1[int(n / 2) - 1:], arr2[:int(n / 2) + 1])
            else:
                return sumofmedians(arr1[int(n / 2):], arr2[:int(n / 2) + 1])


def median(arr):
    n = len(arr)
    if n % 2 == 0:
        return (arr[int(n / 2)] + arr[int(n / 2) - 1]) / 2
    else:
        return arr[int(n / 2)]


arr1 = [1, 4, 7, 10]
arr2 = [2, 3, 5, 6]
# 1 2 3 4 5 6 7 10- 9
print(int(sumofmedians(arr1, arr2)))
