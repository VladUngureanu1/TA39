# 1
def sum(a, b):
    return a + b
print(sum(9, 7))
print(sum(100, 100))

# 2
def even_number(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(even_number(4))
print(even_number(5))

# 3
def sum_of_letters(first_name, middle_name, last_name):
    return len(first_name + middle_name + last_name)
print(sum_of_letters('Vladut', 'Ungureanu', 'Constantin'))

# 4
def rectangle_area(length, height):
    return length * height
print(rectangle_area(5, 10))

# 5
def circle_area(radius):
    return 3.14 * (radius * radius) # (radius ** 2) => radius squared
print(circle_area(5))


# 6
def string(digit):
    if 'a' in digit:
        return True
    else:
        return False
print(string('vlad'))
print(string('min'))

# 7
def show_characters(cale_text):
    nr_lowercase = 0
    nr_uppercase = 0
    for character in cale_text:
        if character.islower():
            nr_lowercase += 1
        elif character.isupper():
            nr_uppercase += 1
    print("The number of lowercase characters is", nr_lowercase)
    print("The number of uppercase characters is", nr_uppercase)
show_characters("Anna has apples")

# 8
def only_positive(*nums):
    for num in nums:
        if num > 0:
            print(num, end=' ')


only_positive(11, -21, 0, 45, 66, -93)

# 9
def numbers(x, y):
    if x > y:
        print("First number", x, "is bigger than second number", y)
    elif x < y:
        print("Second number", y, "is bigger than first number", x)
    else:
        print("Numbers", x, "și", y, "are equals.")
numbers(5, 2)
numbers(2, 5)
numbers(5, 5)

# 10
def add_in_set(number, set_numbers):
    if number in set_numbers:
        print('I did not add the number to the set. It already exists.')
        return False
    else:
        set_numbers.add(number)
        print('I added the new number to the set.')
        return True

add_in_set(3, {2, 3, 5})