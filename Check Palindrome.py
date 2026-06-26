num = int(input("Enter the Number: "))
n = num
result = 0
while n > 0:
    ld = n % 10
    result = (result*10) + ld
    n = n // 10

if num == result:
    print(True)
else:
    print(False)

# Time Complexity = O(log n)
# Space Complexity = O(1)