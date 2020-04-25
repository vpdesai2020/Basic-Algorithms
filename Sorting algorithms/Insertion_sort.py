''' Write a python program that implements insertionsort.'''
def insertionSort(seq):
    n = len(seq)
    
    for i in range(1, n):
        # save the value 
        value = seq[i]
        # Find the position where value fits in the ordered part of the list
        pos = i
        while pos > 0 and value < seq[pos - 1]:
            # shift the items to the right during the search
            seq[pos] = seq[pos - 1]
            pos -= 1
        seq[pos] = value
        print seq
    return seq
