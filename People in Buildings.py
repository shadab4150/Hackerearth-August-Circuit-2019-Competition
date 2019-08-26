import math
n=int(input())
def distance(k,l,m):
    man=math.sqrt((k[0]-c_x)**2+(k[1]-c_y)**2)
    return man
    
arr=[]
g=int(input())
for i in range(n):
    arr.append(list(map(int,input().split())))
buil=n//g
print(buil)
x=[p[0] for p in arr]
y=[p[1] for p in arr]
c_x=sum(x)/n
c_y=sum(y)/n
arr1=[]

for i in range(n):
    kl=round(distance(arr[i],c_x,c_y),3)
    arr1.append([i,kl])
kt=sorted(arr1,key=lambda x:x[1])
kt=[x[0]+1 for x in kt]  
if buil==1:
    print(n)
    print(*list(range(1,n+1)))
else:
    mark=0
    for i in range(buil):
        if i==buil-1:
            pot=kt[mark:]
            print(len(pot))
            print(*pot)
        else:
            pot=kt[mark:mark+g]
            mark+=g
        
            print(len(pot))
            print(*pot)
