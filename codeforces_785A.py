t  = int(input())
faces_total = 0
while(t):
    shape =input()
    if(shape =='Tetrahedron'):
        faces_total+=4
    elif(shape =='Cube'):
        faces_total+=6
    elif(shape =='Octahedron'):
        faces_total+=8
    elif(shape =='Dodecahedron'):
        faces_total+=12
    else:
        faces_total+=20
    t-=1

print(faces_total)