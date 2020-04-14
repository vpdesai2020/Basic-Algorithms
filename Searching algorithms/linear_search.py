''' A python program that implements linear search. '''
def linearSearch(list, target):
    for i in range(len(list) -1):
        # if the target is int the ith element, return True
        if list[i] == target:
            return True
    return False # If not found, return false
