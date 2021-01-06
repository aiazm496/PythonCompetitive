inp_list = [int(i) for i in input().split()]

n = inp_list[0]
h = inp_list[1]
width = 0

heights = [int(i) for i in input().split()]

for height in heights:
    if height <= h:
        width+=1
    else:
        width+=2

print(width)

