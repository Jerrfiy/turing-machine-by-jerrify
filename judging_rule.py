# This is a function decide whether the input correct or not


def judging_note(list):
    for i in list:
        if i != 0 and i != 1:
            print('Wrong input.')
            break
