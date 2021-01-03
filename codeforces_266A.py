stones = int(input())

inp_list = input()
stones_out = 0

for i in range(len(inp_list)-1):
    if inp_list[i+1] == inp_list[i]:
        stones_out+=1

print(stones_out)