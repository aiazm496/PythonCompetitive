import array

arr = array.array('i',[1,2,3])  #i is typecode for signed int

#printing array

for i in range(len(arr)):
    print(arr[i],end = " ")

print("\n")

#appending to array  = adding value at the end of array

arr.append(4)

for i in range(len(arr)):
    print(arr[i],end = " ")

print("\n")

#inserting (index,value)
arr.insert(4,5)

for i in range(len(arr)):
    print(arr[i],end = " ")

print("\n")

#pop - remove the element at specific index

arr.pop(4)

for i in range(len(arr)):
    print(arr[i],end = " ")

#remove a specific value's first occurence

arr.remove(4)
print("\n")
for i in range(len(arr)):
    print(arr[i],end = " ")

print("\n")
#index of a value in array

print(arr.index(3))

#reversing array

arr.reverse()

print("\n")
for i in range(len(arr)):
    print(arr[i],end = " ")

print("\n")

print(arr[::-1])


