# an int between [1, 1000]
planets = int(input())


# pop, growth factor and food prod are ints from [1, 1000000000]
# int datatype should be sufficient in Python for large GF and FP #
planet_metrics = []
for planet in range(planets):
    pop, growth_factor, food_prod = input().split()
    planet_metrics.append((int(pop), int(growth_factor), int(food_prod)))


# P = P * R ^ i < = F
# solve for i
# mathematical approach suffers from floating point inprecision
# probably got my numbers donked up for the population.
for pop, growth_factor, food_prod in planet_metrics:
    years = food_prod / (pop * growth_factor)
    # needed to find out how to round up without Math module.
    # https://stackoverflow.com/questions/57115951/rounding-a-math-calculation-up-without-math-ceil#:~:text=As%20far%20as%20I've,and%20you'll%20be%20fine.
    # The below returns the int of years which rounds down and then
    # the next part checks if years is fractional [0,1]
    # if it is fractional then it returns true and is converted to 1
    # if it isn't it returns false and is converted to 0
    years_rounded = int(years) + int((years - int(years)) > 0)
    print(years_rounded)