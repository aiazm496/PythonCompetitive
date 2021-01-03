no = int(input())


x = 0

while(no):
    logic = input()
    st_logic = logic.strip("X")
    if(st_logic=="++"):
        x+=1
    else:
        x-=1
    no-=1
print(x)