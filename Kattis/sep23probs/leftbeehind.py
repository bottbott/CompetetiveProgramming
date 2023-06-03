stop = False
while not(stop):
    sweet, sour = [int(i) for i in input().strip().split()]
    if not(sweet == 0 and sour == 0):    
        if sweet + sour == 13:
            print('Never speak again.')
        elif sweet > sour:
            print('To the convention.')
        elif sour > sweet:
            print('Left beehind.')
        elif sweet == sour:
            print('Undecided.')
    else:
        stop = True