def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    pivot = arr[len(arr) // 2]  # Choose a pivot element
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    # Recursively sort the sublists
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
my_list = [12, 4, 5, 6, 7, 3, 1, 15, 8, 10]
print("Original list:", my_list)
sorted_list = quick_sort(my_list)
print("Sorted list:", sorted_list)
