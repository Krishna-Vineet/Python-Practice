end = False
while not end:
    user_birth = input('\nEnter your DOB or YOB : ')
    if user_birth:
        if int(user_birth[-4:]) > 2020:
            print('You are not yet Born')
            end = True
            break
        elif int(user_birth[-4:]) < 1900:
            print('You seemed to be the oldest person alive')
            end = True
            break
        elif len(user_birth) > 3: print(f'You will be of 100 till {int(user_birth[-4:]) + 100}, if you alive')
    else:
        print('You didn\'t type anything')
        continue
    want_to_end = input('\nDo you want to end / You also can know your age on particular year.\nIf you want to end enter Y else enter N : ')
    if want_to_end.upper() == 'Y':
        end = True
        break
    elif want_to_end.upper() == 'N': pass
    else:
        print('You typed something wrong.\n\t\tClosing the programme')
        end = True
        break
    which_year = input('\nEnter a valid year : ')
    if int(which_year) < int(user_birth): print(f'You were not born in {which_year}') 
    elif int(which_year) < 2020: print(f'I think you want to be younger than you are. Well, your age on {which_year} was {int(which_year)-int(user_birth)}')
    elif int(which_year) > (int(user_birth[-4:]) + 120): print(f'I don\'t think you will alive till {which_year}')
    else: print(f'Your age on year {which_year} will be {int(which_year) - int(user_birth)}')
    end = True
    break
