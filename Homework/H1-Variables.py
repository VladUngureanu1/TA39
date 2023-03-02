# 1
# A variable is a storage space that we can label and in which we can add various types of data

# 2
competitor = "Jhon"
age = 30
score = 9.9
medal = True

# 3
print(type(competitor))
print(type(age))
print(type(score))
print(type(medal))

print(type(competitor), type(age), type(score), type(medal))

# 4
score = round(score)
print(score)
print(type(score))

# 5
print(f'The name of today-s  competitor is {competitor}.')
print(f'He is {age} years old.')
print(f'His score is {score} out of 10.')
print(f'Did he win a gold medal last year? {medal}!')

# 6
first_name = input('Fill with first name: ')
last_name = input('Fill with last name: ')
number_characters = len(first_name) + len(last_name)
print(f'Full name has {number_characters} characters.')
print(f'Full name has {len(first_name) + len(last_name)} characters.')

# 7
lenght = int(input('Lenght: '))
width = int(input('Width: '))
triangle_area = lenght * width
print(f'The area of the triangle is {triangle_area} cm.')
print(f'The area of the triangle is {lenght * width} cm.')

# 8
sentence = 'Coral is either the stupidest animal or the smartest rock'
print(sentence.count(' the '))


# 9
sentence = 'Coral is either the stupidest animal or the smartest rock'
assert sentence == int(sentence)
print('Contains numbers')