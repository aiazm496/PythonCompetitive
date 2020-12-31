t = int(input())

while(t):
    x = int(input())
    sum = 0
    while(x>0):
        last_digit = x%10
        sum+=last_digit
        x = int(x/10)
    print(sum)
    t-=1

