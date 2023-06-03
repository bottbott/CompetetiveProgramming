restaraunt_count = int(input())
restaurant_menus = {}
for i in range(restaraunt_count):
    item_count = int(input())
    restaurant_name = input()
    food = []
    for j in range(item_count):
        food.append(input())
    restaurant_menus[restaurant_name] =  food

yummy = False
for restaurant, food in restaurant_menus.items():
    if 'pancakes' in food and 'pea soup' in food:
        print(f'{restaurant}')
        yummy = True
        break

if not yummy:
    print('Anywhere is fine I guess')