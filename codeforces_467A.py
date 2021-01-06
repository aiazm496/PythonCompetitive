t= int(input())

cnt_rooms = 0
while(t):
    inp_list = [int(i) for i in input().split()]
    no_ppl = inp_list[0]
    capacity = inp_list[1]
    if(capacity-no_ppl>=2):
        cnt_rooms+=1
    t-=1
print(cnt_rooms)