inp_list = [int(i) for i in input().split()]
limak_wt = inp_list[0]
bob_wt = inp_list[1]
yr_need = 0

while(limak_wt<=bob_wt):
    limak_wt*=3
    bob_wt*=2
    yr_need+=1

print(yr_need)