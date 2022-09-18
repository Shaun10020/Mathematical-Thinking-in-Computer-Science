import numpy as np
import itertools as it

def can_be_extend(array,index,size):
    row=int(index/size)
    col=int(index%size)
    top_right=((row-1)*size)+col+1
    top_left=((row-1)*size)+col-1
    btm_right=((row+1)*size)+col+1
    btm_left=((row+1)*size)+col-1
    if array[index]=='/':
        if row!=0 and col!=size-1:
            if array[top_right]=='/':
                return False
        if row!=size-1 and col!='0':
            if array[btm_left]=='/':
                return False
    if array[index]=='|':
        if row!=0 and col!='0':
            if array[top_left]=='/':
                return False
        if row!=size-1 and col!=size-1:
            if array[btm_right]=='/':
                return False
    return True

def extend(array,n,size):
    print(array)
    if array[n]=='0':
        array[n]='/'
        if can_be_extend(array,n,size):
            extend(array,n+1,size)
    if array[n]=='/':
        array[n]='|'
        if can_be_extend(array,n,size):
            extend(array,n+1,size)
    if array[n]=='|':
        array[n]='0'

size=2
array=[]
for x in range(size*size):
    array.append('0')
extend(array,0,size)


