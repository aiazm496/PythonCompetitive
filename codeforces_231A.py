t = int(input())

no_of_problems_can_solve = 0
while(t):
    decison_list = [int(i) for i in input().split()]
    if(decison_list.count(1)>decison_list.count(0)):
        no_of_problems_can_solve+=1
    t-=1

print(no_of_problems_can_solve)