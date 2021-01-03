data =  [int(i) for i in input().split()]
participants = data[0]
min_score_place = data[1]
pass_part = 0

score_list = [int(i) for i in input().split()]
for scores in score_list:
    if scores> 0 and scores >= score_list[min_score_place-1]:
        pass_part+=1

print(pass_part)