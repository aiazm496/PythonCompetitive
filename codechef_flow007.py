t = int(input())

while(t):
    x = input()
    y = x.strip("0")  #removing trailing and leading zeroes
    print(y[::-1])
    t-=1
        
