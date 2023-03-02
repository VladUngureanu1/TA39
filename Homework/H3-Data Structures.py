# 1
musical_notes = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(type(musical_notes))
print(musical_notes)

print(musical_notes[::-1])
musical_notes = ['do', 'si', 'la', 'sol', 'fa', 'mi', 're', 'do']

musical_notes.reverse()
print(musical_notes)

# 2
print(musical_notes.count('do'))

# 3
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]

for x in(list2):
    list1.append(x)
print(list1)

list3 = list1 + list2
print(list3)

list1.extend(list2)
print(list1)

# 4
list3.sort()
print(list3)
list3.remove(0)
print(list3)

# 5
if len(list3) == 0:
    print('the list is empty')
else:
    print('the list is not empty')

# 6
list3.clear()
print(list3)

# 7
if len(list3) == 0:
    print('the list is empty')
else:
    print('the list is not empty')

# 8
dict1 = {'Anna':8, 'Jhon':10, 'Smith':5}
x = dict1.keys()
print(x)

# 9
x = dict1.get('Anna')
y = dict1.get('Jhon')
z = dict1.get('Smith')
print(f'Anna got note {x}.')
print(f'Jhone got note {y}.')
print(f'Smith got note {z}.')

# 10
dict1.update({'Smith':6})
print(dict1['Smith'])

# 11
dict1.pop('Jhon')
print(dict1)
dict1['Kent'] = '9'
print(dict1)

# 12
week_days = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
weekend = {'saturday', 'sunday'}
print(week_days)
week_days.add('monday') # the set does not accept duplicates
print(week_days)


# 13
if 'saturday' and 'sunday' in week_days:
    print(True)
else:
    print(False)

# 14
print(week_days - weekend)
print(week_days.difference(weekend))

print(weekend - week_days)
print(weekend.difference(week_days))

# 15
common_list = set(week_days).intersection(weekend)
print(common_list)

#Optional
field_players_list = ['Ronaldo', 'Hagi', 'Mutu', 'Lacatus', 'Messi']
reserve_player_list = ['Petrescu', 'Chivu', 'Popescu', 'Dobrin', 'Balaci']
removed_players_list = []
changes_made = 1
max_changes = 3
x = input('Leaves the field: \n')
y = input('Enter the field: \n')
z = max_changes - changes_made

if x in field_players_list and y in reserve_player_list and max_changes <= max_changes:
    field_players_list.remove(x)
    reserve_player_list.remove(y)
    removed_players_list.append(x)
    field_players_list.append(y)
    print(f'Entered {y}, exited {x}, still have {z} changes.')
    print(f'Players on the field: {field_players_list}')
    print(f'Reserve players: {reserve_player_list}')
    print(f'Out players: {removed_players_list}')
elif x not in field_players_list:
    print(f'The change can not be mada because player {x} is not on the field.')
elif y not in reserve_player_list:
    print(f'The change can not be made because player {y} is not reserve.')
else:
   print(f'Without changes! {z} remaining changes')