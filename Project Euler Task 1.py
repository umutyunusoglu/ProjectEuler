# -*- coding: utf-8 -*-
"""
TASK:
If we list all the natural numbers below 10 that
are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""
import time

limit=1000

#Algorithm 1

total= 0
start= time.perf_counter()

result=0

for i in range(limit):
    if i%5==0 or i%3==0:
        result+=i
end= time.perf_counter()
total += end-start
algTime1= total

print("Algorithm 1 Result = ",result)
print("Algorithm 1 Lasted = ", algTime1, " Seconds.")

print("------------------------------")
#Algorithm 2
result=3

"""
3+2=5
5+1=6
6+3=9
9+1=10
10+2=12
12+3=15
15+3=18

18+2=20
20+1=21
21+3=24
24+1=25
25+2=27
27+3=30
30+3=33

addition pattern is 2,1,3,1,2,3,3

"""
total= 0
start= time.perf_counter()

counter=3
patternList=[2,1,3,1,2,3,3]

while counter<limit:
    for i in patternList:
        if(counter+i<limit):
            counter+=i 
            result+=counter
        else:
            counter+=i 
            break
end= time.perf_counter()      
total += end-start
algTime2= total

        
print("Algorithm 2 Result = ",result)
print("Algorithm 2 Lasted = ", algTime2, " Seconds.")


print("------------------------------")

if(algTime2>algTime1):
    print("Algorithm 1 is faster than Algorithm 2!")
elif(algTime1>algTime2):
    print("Algorithm 2 is faster than Algorithm 1!")
else:
    print("Both Algorithms performed equal!")
