length = int(input())
validation_line = input()

open_brackets = "{[("
closed_brackets = "}])"
bracket_list = list()
ok_so_far = True
for i in range(length):
    char = validation_line[i]
    if char in open_brackets:
        bracket_list.append(char)
        next
    if bracket_list == [] and char in closed_brackets:
        print(f'{char} {i}')
        ok_so_far = False
        break
    if char in closed_brackets and open_brackets[closed_brackets.find(char)] == bracket_list[-1]:
        bracket_list.pop()
        next
    elif char in closed_brackets and open_brackets[closed_brackets.find(char)] != bracket_list[-1]:
        print(f'{char} {i}')
        ok_so_far = False
        break
    else:
        ok_so_far = True

if ok_so_far:
    print('ok so far')

### TODO
# should have combined some of the logic so that the code doesn't repeat.
# could have called quit() in the control logic to terminate rather than
# have an if check at the end. 