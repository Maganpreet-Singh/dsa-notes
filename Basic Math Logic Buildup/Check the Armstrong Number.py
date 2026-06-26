num = int(input("Enter the Number: "))
n = num
nod = len(str(n))
total = 0
while n > 0:
    ld = n % 10
    total = total + (ld ** nod)
    n = n // 10

if num == total:
    print(True)
else:
    print(False)

# Time Complexity = O(log n)
# Space Complexity = O(1)