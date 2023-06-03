import sys
stop = False
i = 1
for line in sys.stdin:
    line = line.strip().split()
    numbers = line[1:]
    numbers = [int(i) for i in numbers]
    min_num = min(numbers)
    max_num = max(numbers)
    range = max_num - min_num
    print(f"Case {i}: {min_num} {max_num} {range}")
    i += 1
    