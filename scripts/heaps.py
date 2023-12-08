def count_swaps(heap):
    """Count the number of swaps needed to build a max heap from the given heap."""
    swaps = 0

    # Function to heapify a subtree rooted at index i
    def max_heapify(i, n):
        nonlocal swaps
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child is larger than root
        if left < n and heap[left] > heap[largest]:
            largest = left

        # Check if right child is larger than largest so far
        if right < n and heap[right] > heap[largest]:
            largest = right

        # If largest is not root
        if largest != i:
            heap[i], heap[largest] = heap[largest], heap[i]
            swaps += 1
            max_heapify(largest, n)

    # Build a max heap
    n = len(heap)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(i, n)

    return swaps

# Test different values of x
valid_x_values = []
for x in range(1, 10):
    heap = [3, 4, x, 1, 7]
    swaps = count_swaps(heap.copy())
    if swaps <= x:
        valid_x_values.append(x)

print(valid_x_values)
