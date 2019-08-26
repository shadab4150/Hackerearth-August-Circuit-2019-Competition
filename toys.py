from itertools import product

def toys(n):
    count=0
    for roll in product(range(1,n-1), repeat = 3):
        if sum(roll)==n and roll.count(max(roll))==1:
            count+=1
    return count
for i in range(int(input())):
    k=int(input())
    if k<4:
        print(0)
    else:
        print(toys(k))
        
    
    