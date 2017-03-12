import random
'''
The key idea of this program is to equate the strings
"rock", "paper", "scissors", "lizard", "Spock" to numbers as follows:
'''
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

CHARACTERS = {'1': 'ROCK', '2': 'PAPER', '3': 'SCISSORS', '4': 'LIZARD', '5': 'SPOCK'}


def name_to_number(name):

    if name == 'ROCK':
        name = 0
    elif name == 'SPOCK':
        name = 1
    elif name == 'PAPER':
        name = 2
    elif name == 'LIZARD':
        name = 3
    elif name == 'SCISSORS':
        name = 4
    else:
        print("Don't be a NUT!\n"
              "")
        rpsls()
    return name


def number_to_name(number):
    # convert number to a name using if/elif/else
    if number == 0:
        number = 'ROCK'
    elif number == 1:
        number = 'SPOCK'
    elif number == 2:
        number = 'PAPER'
    elif number == 3:
        number = 'LIZARD'
    elif number == 4:
        number = 'SCISSORS'
    else:
        rpsls()
    return number


def rpsls():
    # prints rules
    print("It's very simple. Scissors cuts paper.\n"
          "Paper covers rock. Rock crushes lizard. \n"
          "Lizard poisons Spock. Spock smashes scissors. \n"
          "Scissors decapitates lizard. Lizard eats paper. \n"
          "Paper disproves Spock. Spock vaporizes rock.\n"
          "And as it always has, rock crushes scissors. \n"
          "\n"
          "1)ROCK 2)PAPER 3)SCISSORS 4)LIZARD 5)SPOCK\n"
          "")
    # print out the message for the player's choice
    player_choice = str.upper(input('What is your choice?\n'))
    for nr in player_choice:
        for key, value in CHARACTERS.items():
            if nr == key:
                player_choice = CHARACTERS[nr]

    print('Player choose ' + player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # convert comp_number to comp_choice using the function number_to_name()
    number_to_name(comp_number)

    # print out the message for computer's choice
    print('Computer choose ' + number_to_name(comp_number))

    # compute difference of comp_number and player_number modulo five
    result = (comp_number - player_number) % 5

    # determine winner, print winner message
    if result == 0:
        msg = 'Player and computer tie!'
        print(msg)
    elif result == 1 or result == 2:
        msg = 'Computer wins!'
        print(msg)
    elif result == 3 or result == 4:
        msg = 'Player wins!'
        print(msg)
    else:
        msg = 'Error! Try again...'
        print(msg)
        rpsls()

rpsls()
