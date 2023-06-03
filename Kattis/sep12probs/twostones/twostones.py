# alice takes stone 1 - 2
# bob takes stone 3 - 4
# alice takes stone 5 - 6
# when there is stone = 1 then
# the stones form a sequence 
# s1 s2 s3 s4 s5 s6
# players have to take consecutive stones
# when there are no more consecutive stones left
# then if the remaining count is odd, Alice wins.
# if the remaining count is even, Bob wins

# how should the stones be represented? 
# list, tuple, dict, set, string
# mutable vs new non-mutable

# custom abstract data structure? 
# stack, queue, linked list
# honestly, thinking of just starting with a list of booleans, but maybe something else that is smaller?

# where do they take the stones from?
# they can take stone i and stone i + 1

# need some method for checking if the list has no more consecutive untaken.. 
# i & ith == true, or last result
# current   last
# true      true
# true      false
# false     true
# false     false

# taking a stone involves checking for consecutive stones
# take stones until areConsecutiveStones == False

# assume Alice and Bob play optimally. 
# what the heck does that mean?

def main():
    stones = input()
    stone_sequence = [True] * int(stones)

    areConsecutiveStones = True
    while(areConsecutiveStones):
        sequence = remove_stones(stone_sequence)
        if sequence == False:
            areConsecutiveStones = False
            break
        stone_sequence[sequence[0]] = False
        stone_sequence[sequence[1]] = False

    check_win_count(stone_sequence)

def remove_stones(stone_sequence):
    # return the ith positions to remove
    for position in range(len(stone_sequence)):
        if position == len(stone_sequence) - 1:
            return False
        if stone_sequence[position] == True and stone_sequence[position+1] == True:
            return (position, position + 1)
    return False

def check_win_count(sequence):
    count = sequence.count(True)
    if count % 2 == 1:
        print('Alice')
    else:
        print('Bob')

main()