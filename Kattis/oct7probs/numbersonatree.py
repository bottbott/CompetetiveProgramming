## original approaach was to basically walk down the nodes until I got to the right node and return it
## and I would generate an entire list of all the levels before walking down it. 
## Generating the list was bad news. Took up a bunch of memory when dealing with higher tree depths
## Refactored it to just return a list of ranges for each level that could be evaluated later on
## Still to slow to pass Kattis
## New strategy is to not go through the levels, and instead go directly to the level of interest based on
## len(directions) and then split that list until we arrive at the element

## New new strategy is to go directly to level of interest and move the start/end locations until we are at
## the right element and then return it. That way we avoid opening up a mega list into memory. 

## The above works and passes. I wonder if it's possible to directly create the range instead of a list of
## ranges as I have it now. Possible refactor for get_tree. Gonna leave it for now but fairly confident it
## would be possible. 

from utils import track

def get_tree(depth):
    depth += 1
    i = 2**(depth) - 1
    # num_list = list(range(1, i + 1))
    # numbers = [[] for _ in range(depth)]
    numbers = []
    # for num in range(depth + 1):
    #     for j in range(2**num): 
    #         numbers[num].append(num_list.pop())
    low_bound = 2 ** depth - 1
    for num in range(depth):
        numbers.append((range(low_bound, low_bound - 2 ** num, -1)))
        low_bound = low_bound - 2 ** num
    return numbers

## stepped through each depth and then moved the current location to the R/L and continued thru depths
def get_number_from_path_old(numbers, directions):
    search_depth = len(directions)
    current_location = list(numbers[0])[0]
    current_depth = 0
    for dir in directions:
        index = list(numbers[current_depth]).index(current_location)
        half_numbers = list(numbers[current_depth + 1])[index * 2: index * 2 + 2]
        if dir == 'R':
            current_location = half_numbers[1] # from the back half
        elif dir == 'L':
            current_location = half_numbers[0] # from the front half
        current_depth += 1
    return current_location

## attempted to only use the specific depth of interest and then opened up the list and halved it to reach
## the desired element
def get_number_from_depth_old(numbers, directions):
    depth = len(directions)
    numbers = list(numbers[depth])
    for dir in directions:
        length = len(numbers)
        if dir == 'R':
            numbers = numbers[length//2:length]
        if dir == 'L':
            numbers = numbers[0:length//2]
    return numbers[0]

def get_number_from_depth(numbers, directions):
    depth = len(directions)
    start, end = numbers[depth].start, numbers[depth].stop
    distance = start - end
    for dir in directions:
        if dir == 'R':
            start -= distance // 2
        if dir == 'L':
            end += distance // 2
        distance = start - end

    return start

@track
def main():
    user_input = input().strip().split()
    if len(user_input) > 1:
        tree_depth, directions = user_input
    else:
        tree_depth = user_input[0]
        directions = ''

    tree_depth = int(tree_depth)
    directions = list(directions)

    numbers = get_tree(tree_depth)

    number = get_number_from_depth(numbers, directions)

    print(number)

main()