t  = int(input())

while(t):
    a_b = [int(i) for i in input().split()]
    a = a_b[0]
    b = a_b[1]
    if(a%b==0):
        print(0)
    else:
        r = a%b
        to_add = b-r
        print(b-r)
    t-=1