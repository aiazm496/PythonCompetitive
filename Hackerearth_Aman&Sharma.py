t = int(input())
toffee_received = 0

while(t):
    inp_list = [int(i) for i in input().split()]
    distance_to_cover = inp_list[0] * 2 * 22/7
    distance_can_cover = inp_list[1] * 100

    if(distance_can_cover>=distance_to_cover):
        toffee_received+=1
    
    t-=1    

print(toffee_received)
