"""
https://www.hackerearth.com/challenges/competitive/august-circuits-19/algorithm/yet-another-gcd-sum-problem-4dc63a13/#c195677
"""
# python 3
import math
def find_gcd(x, y): 
    ans=math.gcd(x,y)
    return ans

def gcd_ar(arr):
    
    num1 = arr[0] 
    num2 = arr[1] 
    gcd = find_gcd(num1, num2) 
  
    for i in range(2, len(arr)): 
        gcd = find_gcd(gcd, arr[i])
    return gcd

n,m=[int(x) for x in input().split()]
array=list(map(int,input().split()))

for i in range(m):
    l,r=[int(x) for x in input().split()]
    result=0
    for j in range(l-1,r-1):
        for k in range(j+1,r):
            cat=array[j:k+1]
            result+=gcd_ar(cat)
    result=result+sum(array[l-1:r])
    print(result)

