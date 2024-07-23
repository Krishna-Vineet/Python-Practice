lines = ['What game do you want to play?', 'Wrong input, Run again', 'Type your choice (Snake/Water/Gun)', 'This function is for Snake Water Gun game.', 'How many turns you want to play?', 'From: GamesON Game Team - Future of Gaming India.', 'Developed, Coded & Tested by Krishna.', 'Spelling mistake or Wrong input, CPU will given 5 points', 'You are not yet Born', 'You seemed to be the oldest person alive', 'I think you want to be younger than you are.', 'I don\'t think you will alive till then.']
print(f'All {len(lines)} sentences are :\n')
no = 1
for i in lines:
    print(f'{no}) {i}')
    no+=1
user = input('\nWhat you want too search? : ')
result_no = 0
no = 1
for items in lines:
    if user.lower() in items.lower():
        result_no+=1
    else: pass
print(f'\n\t{result_no} result(s) found.\n')
no = 1
for items in lines:
    if user.lower() in items.lower():
        print(f'{no}) {items}')
        no+=1
    else: pass
add = input('\nDo you want to add sentences.\nY for yes and N for no : ')
if add.upper() == 'Y':
    what = input('\nWrite the sentence : ')
    lines.append(what)
    print('\tSentence added successfully.')
elif add.upper() == 'N': print('\tThanks for Using..')
else: print('\tYou typed something else, Closing the programm.')