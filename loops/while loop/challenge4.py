# 4. Ask for the name of somebody the user wants to invite to a party. After this, display the message "[name] has now been invited"
# and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this until they no longer want to invite anyone
# else to the party and then display how many people they have coming to the party.

invite_list = []
count = 0
name = input('Enter name of person to invite : ')

print(f'{name} has now been invited')
invite_list.append(name)
count += 1

choice = input('Do you want to invite someone ? (y/n) ')


while choice.lower() == 'y':
    invite_name = input('Enter name of the person you want to invite : ')
    print(f'{invite_name} has now been invited')
    invite_list.append(invite_name)
    count += 1
    choice = input('Do you want to add more? (y/n) ')

print(f'You invited {count} people')
# print(f'{invite_list} has been invited', sep=',')
# print(f'{invite_list} has been invited', sep=',')
print(*invite_list, sep=',')
