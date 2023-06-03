# S = (R1 + R2) / 2
# input is R1 and S1
numbers = input().split()

r1 = int(numbers[0])
s = int(numbers[1])

# R2 = 2S - R1
r2 = 2 * s - r1
print(r2)