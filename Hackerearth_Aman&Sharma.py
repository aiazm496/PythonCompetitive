t = int(input())
toffee_received = 0
while(t):
    inp = list(map(int,input().split()))
    radius = inp[0]
    horlicks = inp[1]
    distance_to_cover = 2* 22/7 * radius
    distance_can_cover = horlicks*100.0
    if(distance_can_cover>=distance_to_cover):
        toffee_received+=1
    t-=1
    
print(toffee_received)