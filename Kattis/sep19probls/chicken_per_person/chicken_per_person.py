people, chicken = [int(input) for input in input().strip().split()]

peoplediff = chicken - people
chickendiff = people - chicken
s = '' if peoplediff >= -1 and peoplediff <= 1 else 's'

if people > chicken:
    print(f"Dr. Chaz needs {chickendiff} more piece{s} of chicken!")
else:
    print(f'Dr. Chaz will have {peoplediff} piece{s} of chicken left over!')

