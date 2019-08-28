"""
https://www.hackerearth.com/challenges/competitive/august-circuits-19/algorithm/yet-another-gcd-sum-problem-4dc63a13/#c195677
"""
# python 3
from math import gcd

def gcd_ar(arr):
    x = reduce(gcd,arr)
    return x


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

