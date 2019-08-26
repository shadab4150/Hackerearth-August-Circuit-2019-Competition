for i in range(int(input())):
    n,m=[int(x) for x in input().split()]
    hp=list(map(int,input().split()))
    hap=hp.copy()
    
    red=list(map(int,input().split()))
    arr=[]
    for i in range(1,m+1):
        for j in range(i-1,n,i):
            hp[j]=hp[j]-red[i-1]
        for k in range(i-1,len(hp)):
            if hp[k]<=0:
                arr.append([i,k+1])
        for i in range(len(hp)):
            if hp[i]<=0:
                hap[i]=0
        hp=hap.copy()
    
    for i in hp:
        if i>0:
            und=hp.index(i)+1
    for rt in range(1,n+1):
        if rt==und:
            print(-1)
            
        for i in arr:
            if i[1]==rt and i[1]!=und:
                print(i[0])
                break
                
            
            
        
                
    
                
                
        
    
    