arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = 23

def subArraySum(arr, s):
    n = len(arr)
    i = 1
    curr_sum = arr[0]
    start = 0
    while i <= n:
        while curr_sum > s and start < i-1:
            curr_sum = curr_sum - arr[start]
            start += 1
        if curr_sum == s:
            print("%d %d" % (start, i - 1))
            return
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1
    print("-1")
    return


subArraySum(arr, s)
