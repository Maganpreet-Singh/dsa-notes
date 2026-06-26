import math

def Count_Digit(num):
    return int(math.log10(num)) + 1

print(Count_Digit(489965))