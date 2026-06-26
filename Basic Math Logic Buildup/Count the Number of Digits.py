num = int(input("Enter the Number: "))
n = num
count = 0
while n > 0:
    count += 1
    n = n // 10
print(count)

# Time Complexity = O(log n)
# Space Complexity = O(1)