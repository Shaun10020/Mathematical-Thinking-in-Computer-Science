def is_permutation(p):
  return (set(p)==set(range(len(p))))

def is_even(p):
  counter=0
  for x in range(len(p)):
    while x!=p[x]:
      a=p[x]
      i=x+1
      j=x
      while p[a]!=a:
        (p[i],p[j])=(p[j],p[i])
        counter+=1
        i+=1
        j+=1
  if counter%2==0:
    return True
  else:
    return False

def solution(position):
  ref=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
  seq=[]
  for x in range(len(position)):
    while ref[x]!=position[x]:
      a=position[x]
      i=x+1
      j=x
      while position[ref.index(a)]!=a:
        (position[i],position[j])=(position[j],position[i])
        seq.append(i)
        seq.append(j)
        i+=1
        j+=1
  return seq
       
print (solution([2,3,1,4,5,6,7,8,9,10,11,12,13,14,15,0] ))