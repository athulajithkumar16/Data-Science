# 4. Ask for the name of somebody the user wants to invite to a party. After this, display the message "[name] has now been invited"
# and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this until they no longer want to invite anyone
# else to the party and then display how many people they have coming to the party.

name = input('Enter name of person to invite : ')
count = 0

print(f'{name} has now been invited')
count += 1

choice = input('Do you want to invite someone ? (y/n) ')

while choice.lower() == 'y':
    invite_name = input('Enter name of the person you want to invite : ')
    print(f'{invite_name} has now been invited')
    count += 1
    choice = input('Do you want to add more? (y/n) ')

print(f'You invited {count} people')
