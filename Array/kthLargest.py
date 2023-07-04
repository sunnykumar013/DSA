def find_kth_largest(nums, k):
    min_heap = nums[:k]
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            min_heap[0] = nums[i]
            _heapify_down(min_heap, 0, k)
    return min_heap[0]

def _heapify_down(nums, i, size):
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i
    if left < size and nums[left] < nums[smallest]:
        smallest = left
    if right < size and nums[right] < nums[smallest]:
        smallest = right
    if smallest != i:
        nums[i], nums[smallest] = nums[smallest], nums[i]
        _heapify_down(nums, smallest, size)

res = find_kth_largest([10, 63, 87, 67, 34, 98, 1, 21, 23, 34, 45, 566, 687, 87, 83, 87, 21],6)
print(res)