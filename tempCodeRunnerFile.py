inp_lis = [int(i) for i in input().split()]

n = inp_lis[0]
t = inp_lis[1]

q = input()
nq = []


while(t):
    for i in range(len(q)-1):
        if(q[i]=='B' and q[i+1] == 'G'):
            nq[i] = ('G')
            nq[i+1] = ('B')
        else:
            nq[i] = (q[i])
            nq[i+1] = (q[i+1])
    t-=1

