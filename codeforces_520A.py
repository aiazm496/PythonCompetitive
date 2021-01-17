t  = int(input())
s = input().lower()

distinct_s = set(s)

#print(distinct_s)
if(len(distinct_s)==26):
    print("YES")
else:
    print("NO")