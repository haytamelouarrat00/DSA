import math


def linear_search(array, target):
    """Linear search algorithm.

    Args:
        array (list): List of elements.
        target (int): Element to be searched.

    Returns:
        int: Index of the element if found, -1 otherwise.
    """
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1


def binary_search(arr, low, high, target):
    if high >= low:
        mid = (high + low) // 2

        # Check if the target is present at mid
        if arr[mid] == target:
            return mid

        # If target is smaller than mid, it's in the left subarray
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)

        # Else, it's in the right subarray
        else:
            return binary_search(arr, mid + 1, high, target)
    else:
        # Element is not present in array
        return -1


def ternary_search(arr, l, r, x):
    if r >= l:
        # Divide the range into three parts
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3

        # Check if the element is present at any mid
        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2

        # If not, then narrow down search to the segment where the element is likely to be
        if x < arr[mid1]:
            return ternary_search(arr, l, mid1 - 1, x)
        elif x > arr[mid2]:
            return ternary_search(arr, mid2 + 1, r, x)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, x)

    # Element is not present in the array
    return -1

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == x:
        return prev
    return -1

