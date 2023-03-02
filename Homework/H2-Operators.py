# 1
#If else - is used when the code needs a condition.

# 2
x = 100
if (x) >= 0 and type(x) == int :
    print(f' {x} is a natural number')
else:
    print(f' {x} is not a natural number')

# 3
x = int(input('enter number\n'))
if x > 0:
    print(f' {x} is a positive number')
elif x < 0:
    print(f' {x} is not a positive number')
elif x == 0:
    print(f' {x} is a neutral number')

# 4
x = int(input('enter a number\n'))
if x >= -2 and x <= 13:
    print(f'{x} is in the range -2:13')
else:
    print(f'{x} is not in the range')

# 5
x = int(input('enter a number\n'))
y = int(input('enter a number\n'))
z = abs(x-y)
print(z)
if z < abs(5):
    print(f'the difference is < 5')
elif z == abs(5):
    print(f'the difference is 5')
else:
    print(f'the difference is > 5')

# 6
x = int(input('enter a number\n'))
if not (x >= 5 and x <= 27):
    print(f'{x} is not in the range 5-27')
else:
    print(f'{x} is in the range 5-27')

# 7
x = int(input('enter a number x\n'))
y = int(input('enter a number y\n'))
if x == y:
    print(f'x=y')
elif x > y:
    print(f'x>y')
elif x < y:
    print(f'x<y')

# 8
x = int(input('enter the side A\n'))
y = int(input('enter the side  B\n'))
z = int(input('enter the side C\n'))
if x == y == z:
    print(f'the triangle is equilateral')
elif x == y or y == z or z == x :
    print(f'the triangle is isosceles')
else:
    print(f'the triangle is certain')

# 9
x = input('enter a letter\n')
if x.lower() in ('a', 'e', 'i', 'o', 'u'):
    print(f'{x} is a vowel')
elif x.upper() in ('A', 'E', 'I', 'O', 'U'):
    print(f'{x} is a vowel')
else:
    print(f'{x} is not a vowel')

# 10
x = int(input('enter a note\n'))
if x >= 9 :
    print(f'The note is A')
elif x >= 8 and x <= 9:
    print(f'The note is B')
elif x >= 7 and x <= 8:
    print(f'The note is C')
elif x >= 6 and x <= 7:
    print(f'The note is D')
elif x >= 4 or x <= 6:
    print(f'The note is E')
elif x < 4:
    print(f'The note is F')
else:
    print(f'You enter a wrong note')
