def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
    # this is the number of loops we do
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

test_arr = [2, 5, 5, 3, 8, 1]
different_arr = [2, 5, 5, 3, 8, 1, 2, 5, 5, 3, 8, 1]


# O(n^2) when you have a nested loop, and both loops
# are dependent on the size of n, the size of the input
sorted_test_arr = bubble_sort(test_arr)
print(sorted_test_arr)