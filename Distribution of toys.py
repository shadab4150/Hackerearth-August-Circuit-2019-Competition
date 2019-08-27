"""
https://www.hackerearth.com/challenges/competitive/august-circuits-19/algorithm/stranger-game-3-1f0d2f47/
"""
"""
You are playing with N toys. 
All the toys are identical. It is your duty to distribute all the toys among your other three friends. 
After the distribution of toys, the person with the highest number of toys is the winner. 
There can be more than one winner if more than one person has the highest number of toys. 
You do not want to declare more than one winner. 
Each of them must have at least one toy otherwise the friends get angry. 
Your task is to determine the number of ways the toys can be distributed among your three friends. 
So that there is not more than one winner and all of them contain at least one toy.
"""

# python 3

def fact(s):

    if s==1 or s==0:
        return 1
    if s>1:
        res=1
        for i in range(1,s+1):
            res*=i

        return res

def toys(n):

    count=fact(n-1)/(2*fact(n-1-2))

    if n%3==0:
        d=n//3
        red=((d//2)*3)+1
        if d%2==0:
            red=red-3
    else:
        d=(n//3)+1
        e=n-(2*d)
        red=(1+(e//2))*3
        if e%2==0:
            red=red-3

    return int(count-red)

for i in range(int(input())):
    n=int(input())
    if n<4:
        print(0)
    else:
        print(toys(n))
    
    
