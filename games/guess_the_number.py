import random

x = random.randrange(1, 21, 1)
print('**** **** **** ****')
print('**** Guess the number ranges between 1 and 20 ****')
#print('Number : ', x)
chance = 0

while True:
    if chance == 5:
        print('Sorry!!! Better luck next time')
        print('\tThe number is ', x)
        break
    y = int(input('Enter the guessed number : '))
    chance += 1
    if x == y:
        print('\t**** Congratz!!! you found the number ****')
        break
    elif y > x:
        print('\tThe number you guessed is higher than the actual')
    elif y < x:
        print('\tThe number you guessed is lesser than the actual')

    remaining = 5 - chance
    print('\tYou have only {} chance to guess the correct number'.format(remaining))

print('**** **** **** ****')
