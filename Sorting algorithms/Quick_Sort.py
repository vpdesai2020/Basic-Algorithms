''' Write a python program that implements quicksort with in-place partitioning.'''
#!/bin/python
''' Quick Sort 1 - Partition '''
def partition(ar):    
    p = 0
    for j in range(1, len(ar)):
        if ar[j] < ar[p]:
            ar = ar[0:p] + [ar[j]] + ar[p:j] + ar[j+1:]
            p += 1
    print ' '.join([`num` for num in ar])

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
