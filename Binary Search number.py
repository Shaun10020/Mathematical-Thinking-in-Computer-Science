print("Key in lower bound")
lower=int(input())
print("Key in upper bound")
upper=int(input())

while int((upper-lower))!=1:
    diff=int((upper-lower)/2+lower)
    print(diff)
    print("If larger input Y, if smaller input N")
    yes=input()
    if yes == 'Y':
        lower=int(diff)
    else:
        upper=int(diff)
