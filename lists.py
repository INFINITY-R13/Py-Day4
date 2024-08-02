fruits = ['Apple', 'Mango', 'Banana', 'Strawberry']
vegetables = ['Potato', 'Spinach', 'Onion', 'Tomato']

edibles = [fruits, vegetables]

print(fruits)
print(vegetables)
print(edibles)

print(fruits[0])
print(vegetables[-1])
print(edibles[0])
print(edibles[1][1])

fruits.append('pineapple')
print(fruits)

dairy = ['Milk', 'Egg']
edibles.extend([dairy])

print(edibles[2][0])

print(edibles)




