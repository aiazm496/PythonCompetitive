a = [5,2,8,1,3]

def quick_sort(arr,n):
    if(n<=1):
        return arr
    else:
        last_element = arr.pop()  #3
        items_greater = []   #[5,8]
        items_smaller = []   #[2,1]
        for i in arr:
            if(i<last_element):
                items_smaller.append(i)
            else:
                items_greater.append(i)
            
        return quick_sort(items_smaller,len(items_smaller)) + [last_element] + quick_sort(items_greater,len(items_greater))


print(quick_sort(a,len(a)))




