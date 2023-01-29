countries= ["India","Africa","America"]
cities = ["Delhi","Tanzania","New York"]

for i in zip(countries,cities):
    print(i)

print()

for count,country in enumerate(countries):
    print(count,country)

a= "Hello"
print(a.swapcase())