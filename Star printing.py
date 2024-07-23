print('\tS T A R   P R I N T I N G')
user = int(input('How many times you want to print : '))
how = input('A for ascending & D for descending : ')
if how.lower() == 'a':
    for i in range(user)[:]: print((i+1)*'* ')
elif how.lower() == 'd':
    for i in range(user)[::-1]: print((i+1)*'* ')