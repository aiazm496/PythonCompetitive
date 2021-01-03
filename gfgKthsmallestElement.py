def kthSmallest(arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    arr.sort()
    result = arr[k-1]
    return result


test = int(input())


while(test):
    size = int(input())
    array = [int(i) for i in input().split()]
    to_find_index = int(input())
    answer = kthSmallest(array,0,size-1,to_find_index)
    print(answer)
    
    test-=1