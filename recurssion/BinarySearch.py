import math
def Binary_Search(data, target, low, high):
    """ returns true if target is found in indicated portion of a list the search only includes data[low] to data[high]
    """
    if low > high:
        return False
    else:
        mid = math.floor((low + high) / 2)
        if target == data[mid]:
            return True
        elif target < data[mid]:
            print(target)
            return Binary_Search(data, target, low, mid - 1)
        else:
            print(target)
            return Binary_Search(data, target, mid + 1, high)
        

data = [10,20,30]
target = 20
low = data[0]
high = data[len(data) - 1]
Binary_Search(data, target, low, high)