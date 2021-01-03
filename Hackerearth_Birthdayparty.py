t = int(input())

while(t):
    inp_list = [int(i) for i in input().split()]
    no_of_friends = inp_list[0]
    no_of_chocolates  = inp_list[1]

    if(no_of_chocolates%no_of_friends==0):
        print("Yes")
    else:
        print("No")
    t-=1

    