inp_list = [int(i) for i in input().split()]
k = inp_list[0]
n = inp_list[1]
w = inp_list[2]

total_amt  = int(k*w*(w+1)/2)
if(total_amt<=n):
    print("0")

else:
    amt_to_borrow = total_amt - n
    print(amt_to_borrow)