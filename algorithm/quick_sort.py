def lomuto(A, p, r):
    i = p - 1
    x = A[r]
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def hoare(A, l, r):
    i, j = l, r
    x = A[l]
    while i <= j:
        while i <= j and A[i] <= x:
            i += 1
        while i <= j and A[j] >= x:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


def quick_sort(A, l, r):
    if l < r:
        # s = hoare(A, l, r)
        s = lomuto(A, l, r)
        quick_sort(A, l, s-1)
        quick_sort(A, s+1, r)


arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(arr, 0, len(arr)-1)
print(arr)
