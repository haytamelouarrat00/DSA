import random
import time


def generate_random_list(size):
    """Generates a random list of integers of a given size"""
    return [random.randint(0, 100) for _ in range(size)]


def selection_sort(l):
    """Sorts a list using the selection sort algorithm"""
    for i in range(len(l)):
        min_index = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    return l


def bubble_sort(l):
    """Sorts a list using the bubble sort algorithm"""
    for i in range(len(l)):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


def insertion_sort(l):
    """Sorts a list using the insertion sort algorithm"""
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j - 1] > l[j]:
            l[j], l[j - 1] = l[j - 1], l[j]
            j -= 1
    return l


def merge(left, right):
    """Merges two sorted lists"""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(l):
    """Sorts a list using the merge sort algorithm"""
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return merge(left, right)


def quick_sort(l):
    """Sorts a list using the quick sort algorithm"""
    if len(l) <= 1:
        return l
    pivot = l.pop()
    left, right = [], []
    for item in l:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    return quick_sort(left) + [pivot] + quick_sort(right)


def heapify(l, n, i):
    """Heapifies a list"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and l[i] < l[left]:
        largest = left

    if right < n and l[largest] < l[right]:
        largest = right

    if largest != i:
        l[i], l[largest] = l[largest], l[i]
        heapify(l, n, largest)


def heap_sort(l):
    """Sorts a list using the heap sort algorithm"""
    n = len(l)

    for i in range(n, -1, -1):
        heapify(l, n, i)

    for i in range(n - 1, 0, -1):
        l[i], l[0] = l[0], l[i]
        heapify(l, i, 0)
    return l


def radix_sort(l):
    """Sorts a list using the radix sort algorithm"""
    RADIX = 10
    placement = 1
    max_digit = max(l)

    while placement < max_digit:
        buckets = [list() for _ in range(RADIX)]
        for i in l:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                l[a] = i
                a += 1
        placement *= RADIX
    return l


# simple comparison of run times
def get_run_time(func, size):
    """Returns the run time of a given function"""
    start_time = time.time()
    l = generate_random_list(size)
    func(l)
    end_time = time.time()
    run_time = end_time - start_time
    formatted_run_time = "{:.5f}".format(run_time)
    return formatted_run_time


print("Selection Sort: ", get_run_time(selection_sort, 1000))
print("Bubble Sort: ", get_run_time(bubble_sort, 1000))
print("Insertion Sort: ", get_run_time(insertion_sort, 1000))
print("Merge Sort: ", get_run_time(merge_sort, 1000))
print("Quick Sort: ", get_run_time(quick_sort, 1000))
print("Heap Sort: ", get_run_time(heap_sort, 1000))
print("Radix Sort: ", get_run_time(radix_sort, 1000))
