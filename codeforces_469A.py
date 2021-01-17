n = int(input())

p1 = [int(i) for i in input().split()]
p1.pop(0)  #removing the first index
p2 = [int(i) for i in input().split()]
p2.pop(0)

p1_set = set(p1)
p2_set = set(p2)
p1_p2_set = p1_set.union(p2_set)

if(len(p1_p2_set)==n):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")