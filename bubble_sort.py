''' Write a Python program that implements bubblesort. '''
def bubbleSort(seq):
    not_sorted = True
    n = len(seq)
    while not_sorted:
        # If following statements fail next statement will stop the loop
        not_sorted = False

        for i in range(n - 1):
            if seq[i] < seq[i-1]:
                temp = seq[i]
                seq[i] = seq[i-1]
                seq[i-1] = temp

                not_sorted = True
        print seq
    return seq
