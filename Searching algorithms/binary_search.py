''' A Python program implements binary search '''


def binarySearch(list, target):
    # initialize 
    low = 0
    high = len(list) - 1
    # First we need to sort the list
    list = list.sort()
    # keep subdivide the sequence in half until the target is found
    while low <= high:
        # find the midpoint
        mid = (high+low) // 2
        # Does the midpoint contain the target?
        if list[mid] == target:
            return True
        # or does the target precede the midpoint?
        elif target < list[mid]:
            high  = mid - 1
        else:
            low = mid - 1
    return False

