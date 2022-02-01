# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 18:40:31 2022

@author: DBarros
"""


def solution(N):
    counter=N
    if N < 100:
        sum=int(N/10)+N%10
        while(True):
            if(int(counter/10)+counter%10 == sum*2): 
                return counter
            else:
                counter +=1
        
    else:
        sum=int(N/100)+N%10 +int(N/10)%10
        while(counter <150):
            print(int(counter/100)+counter%10+int(counter/10)%10)
            if int(counter/100)+counter%10+int((counter/10)%10) == sum*2: 
                return counter
            else:
                counter +=1


n=101
print(solution(n))
