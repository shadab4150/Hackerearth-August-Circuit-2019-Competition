def count(arr):
    c=0
    for i in arr:
        c+=i.count('1')
    return c
        
get_bin=(lambda x, n: format(x, 'b').zfill(n))        
row,col,x=[int(x) for x in input().split()]
arr=[]
for i in range(row):
    arr.append(input())
for i in range(x):
    l=list(map(int,input().split()))
    if l[0]==2:
        print(count(arr))
    else:
        if l[2]>0:
            c_move=l[2]
            for i in range(row-l[2]):
                arr[i]=arr[i+c_move]
            for i in range(1,l[2]+1):
                arr[-i]='0'*col
        if l[2]<0:
            for i in range(row-1,abs(l[2])-1,-1):
                arr[i]=arr[i-abs(l[2])]
            for i in range(abs(l[2])):
                arr[i]='0'*col
        if l[1]>0:
            for i in range(len(arr)):
                s=int(arr[i],2)<<l[1]
                arr[i]=get_bin(s,col)[-col:]
        if l[1]<0:
            for i in range(len(arr)):
                s=int(arr[i],2)>>abs(l[1])
                arr[i]=get_bin(s,col)[-col:]
    
    print(arr)        
                 
            
                
                
            
                
        
        