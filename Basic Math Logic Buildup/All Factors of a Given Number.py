#Brutal Force
num = int(input("Enter the Number: "))
result = []
for i in range(1,num+1):
    if num % i == 0:
        result.append(i)
print(result)

#Time Complexity = O(n)
#Space Complexity = O(k) k is number of factors

#Better Solution
result = []
for i in range(1,(num//2)+1):
    if num % i == 0:
        result.append(i)
result.append(num)
print(result)

#Time Complexity = O(n/2) almost equal to O(n)
#Space Complexity = O(k) k is number of factors

#Optimal Solution
from math import sqrt
result = []
for i in range(1,int(sqrt(num)+1)):
    if num % i == 0:
        result.append(i)
        if num // i != i:
            result.append(num // i)
result.sort()
print(result)

#Time Complexity = O(sqrt(n) + o(nlogn) almost equal to O(n)
#Space Complexity = O(k) k is number of factors
