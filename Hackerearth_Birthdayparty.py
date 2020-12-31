t = int(input())

while(t):
    inp = list(map(int,input().split()))
    no_of_friends = inp[0]
    no_of_chocolates = inp[1]

    if(no_of_chocolates%no_of_friends==0):
        print("Yes")
    else:
        print("No")
    t-=1