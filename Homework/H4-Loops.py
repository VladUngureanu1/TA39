# 1
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in range(len(cars)):
    print(f'My favourite car is {cars[i]}')

for car in cars:
    print(f'My favourite car is {car}')

i = 0
while i < len(cars):
    print(f'Masina mea preferata este {cars[i]}')
    i += 1

#2
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
lengt_str = len(cars)
for i in range(lengt_str-1):
    cars[i] = cars[i].upper()
    # i = i + 1
    cars[0] = cars[0].lower()
else:
    cars[lengt_str - 1] = cars[lengt_str-1].lower()
print(cars)

# 3
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for car in cars:
    if car == 'Mercedes':
        print('I found the car you wanted.')
        break
    else:
        print(f'I found the car {car}. Still searching')

# 4
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for car in cars:
    if car == 'Trabant' or car == 'Lastun':
        continue
    print(f'You might like the car {car}.')

# 5
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
old_cars =[]
for i in range(len(cars)):
    if cars[i] == 'Trabant' or cars[i] == 'Lastun':
        old_cars.append(cars[i])
        cars[i] = 'Tesla'
print(f'New models {cars}')
print(f'Old models {old_cars}')

# 6
car_price = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
    }
budget = 15000

# 7
for cars in car_price:
    if car_price[cars] < budget:
        print(cars)
# 8
for cars in car_price.items():
    print(cars)

# 9
for cars in car_price:
    if car_price[cars] < budget:
        print(f'For a budget below 15,000 euros you can choose the car {cars}')

# 10
for cars in car_price:
    print(cars)

# 11
numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
duplicate = []
for number in numbers:
    if number == 3:
        duplicate.append(1)
print(len(duplicate))


# 12
numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
sum = 0
for number in numbers:
    sum += number
print(sum)

# 13
numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
max = 0
for number in numbers:
    if number > max:
        max = number
    print(max)

# 14
numbers= [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
negative = []
for number in numbers:
    if number > 0:
        number = -number
        negative.append(number)
print(negative)
