 # pdf bubblesort
A = [5, 12, 3, 4, 7, 1, 0, 6, 19, 8, 13, 4, 2, 10, 16,-2,10.5]
n = len(A)
for i in range(n - 1):
    for j in range(n - 1, i, -1):
        if A[j] < A[j - 1]:
            A[j], A[j - 1] = A[j - 1], A[j] # Swap a bubble
    print(A)