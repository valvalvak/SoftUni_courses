population = input().split(", ")
min_wealth = int(input())

population = [int(x) for x in population]
ifTrue = True

if not sum(population) < len(population) * min_wealth:
    for x in range(len(population)):
        if population[x] < min_wealth:
            diff = min_wealth - population[x]
            population[x] += diff
            for y in range(len(population)):
                if population[y] == max(population):
                    population[y] -= diff
else:
    ifTrue = False
    print("No equal distribution possible")
if ifTrue:
    print(population)


