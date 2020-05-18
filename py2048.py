import random

def start_game():
    return [[0 for i in range(4)] for i in range(4)]
def reverse(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j])
    return new_mat
def transp(mat):
    new_mat=[[0 for i in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            new_mat[i][j]=mat[j][i]
    return new_mat
def merge(mat):
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                mat[i][j]+=mat[i][j]
                mat[i][j+1]=0
    return mat
        
def compress(mat):
    new_mat=[[0 for i in range(4)] for i in range(4)]
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos]=mat[i][j]
                pos+=1
    return new_mat
def moveLeft(arr):
    st1=compress(arr)
    st2=merge(st1)
    st3=compress(st2)
    return st3
    
def moveRight(arr):
    st0=reverse(arr)
    st1=compress(st0)
    st2=merge(st1)
    st3=compress(st2)
    st4=reverse(st3)
   
    return st4
    
def moveUp(arr):
    st0=transp(arr)
    st1=compress(st0)
    st2=merge(st1)
    st3=compress(st2)
    st4=transp(st3)
        
    return st4
    
def moveDown(arr):
    st0=transp(arr)
    st=reverse(st0)
    st1=compress(st)
    st2=merge(st1)
    st3=compress(st2)
    st3=reverse(st3)
    st4=transp(st3)
    return st4
input=list(map(int,input().split()))
arr=start_game()
arr[1][3]=2                       #initial array setup, choosen random numbers at random places.
arr[2][2]=2
arr[3][0]=4
arr[3][1]=8
arr[2][1]=4
for i in input:
    if i==1:                         #move Up
        arr=moveUp(arr)
    elif i==2:                       #move Down
        arr=moveDown(arr)
    elif i==3:                       #move left
        arr=moveLeft(arr)
    elif i==4:                       #move right
        arr=moveRight(arr)
print(arr)