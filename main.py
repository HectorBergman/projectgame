from tkinter.messagebox import YES
from SIST import printBoard
options = {'1':'left','2':'right','3':'forward','4':'backward'}
weapens = {'a': 'a banana', 'b' : 'a slipper', 'c': 'a gun'}



your_choice = input()
printBoard() 
print('You are in prison now and you must to escape')
print()
print('You have only 4 choices:')
print()
for option in options:
    print(f'{option}) {options[option]}')


print()
print('Choose your weapen!')
for weapen in weapens: 
    print(f'{weapen}) {weapens[weapen]}')


print('Do you want to open the door')
def fight_p():
    if your_choice == YES:
        print('What do you want to fight with?')
        
        return fight 