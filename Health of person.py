"""
https://www.hackerearth.com/challenges/competitive/august-circuits-19/algorithm/attack-of-the-mind-flayer-3-119b5d47/
"""
import gc

for i in range(int(input())):
    n,m=[int(x) for x in input().split()]
    hp=list(map(int,input().split()))
    hap=hp.copy()
    
    red=list(map(int,input().split()))
    arr=[]
    
    for i in range(m):
        for j in range(i,n,i+1):
    
            hp[j]=hp[j]-red[i]
    
        for k in range(i,n):
            if hp[k]<=0:
                arr.append([i+1,k+1])
        for i in range(n):
            if hp[i]<=0:
                hap[i]=0
        hp=hap.copy()
    
    
    
    for i in range(1,n+1):
        if hp[i-1]>0:
            print(-1)
            
        for s in arr:
            if s[1]==i:
                print(s[0])
                break
    gc.collect()   
    
        
            
            
            
        
                
    
                
                
        
    
    
