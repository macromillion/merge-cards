import random
import time
import colored
from colored import stylize

# Change to 1 for ADMIN MODE, 0 for normal
launch_exceptions = 0


# Checks if input is number
def isNumber(s):
    for i in range(len(s)):
        if s[i].isdigit() != True:
            return False
    return True


# List bases for working generation of cards and dialogue, can be changed to diffrent card styles
suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
nums = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'King', 'Queen']
user_fullHand = []
com_fullHand = []
com_noResponses = ['No, sorry', 'Nope', 'No', 'Thats a no', 'Nah']

# Generates card for specified mode
if launch_exceptions == 0:
    for x in range(0, 7):
        userGenn_card = random.choice(nums) + ' of ' + random.choice(suits)
        user_fullHand.append(userGenn_card)
    for x in range(0, 7):
        comGenn_card = random.choice(nums) + ' of ' + random.choice(suits)
        com_fullHand.append(comGenn_card)

# Displays your current hand upon command call


def show_yourHand():
    if not user_fullHand:
        print('\n')
        print(stylize('Your hand is empty!', colored.fg("red")))
    print('\n')
    print(*user_fullHand, sep="\n")


# Main function of the file


def touch():
    print('\n')

    # Checks if the user has under 7 cards, if else force discards them
    cards_inHand = len(user_fullHand)
    if cards_inHand > 7:
        cardsTo_discard = cards_inHand - 7
        cardsTo_discard = str(cardsTo_discard)
        cards_inHand = str(cards_inHand)
        print(
            'You have ' + cards_inHand +
            ' cards in your hand, your must have 7 or lower at all times. Please discard '
            + cardsTo_discard + '.')
        for x in range(0, int(cardsTo_discard)):
            try:
                discard_card = input('Card: ')
                user_fullHand.remove(discard_card)
                print(stylize("[-1] " + discard_card, colored.fg("red")))
            except ValueError:

                touch()

    # Checks if the user has the needed amount of merges to win the game
    if 'Merge' and 'Merge' and 'Merge' in user_fullHand:
        print('Ye won mate!')
        exit()

    # Main input slot, for command usage and general printage
    touch_1 = input()

    # Check if the COM user has a mentioned suit
    if 'check' in touch_1:
        if 'spades' in touch_1:
            print('You: Do you have any Spades?')
            if 'Spades' in str(com_fullHand):
                print('Com: Yes')
                cards_inHand = len(user_fullHand)
                if cards_inHand >= 7:
                    print(
                        stylize(
                            'Your hand is full, would you like to discard a card? y/n',
                            colored.fg("red")))
                    yesno_ans = str(input())
                    if yesno_ans == 'y':
                        try:
                            discard_card = input('Card: ')
                            user_fullHand.remove(discard_card)
                            print(
                                stylize("[-1] " + discard_card,
                                        colored.fg("red")))
                        except ValueError:
                            print(
                                stylize("You don't own this card!",
                                        colored.fg("red")))
                            touch()
                        new_card = random.choice(nums) + ' of Spades'
                        user_fullHand.append(new_card)
                        print(stylize("[+1] " + new_card, colored.fg("green")))
                    elif yesno_ans == 'n':
                        touch()
                    else:
                        print(stylize('Invalid input!', colored.fg("red")))
                        touch()
                else:
                    new_card = random.choice(nums) + ' of Spades'
                    user_fullHand.append(new_card)
                    print(stylize("[+1] " + new_card, colored.fg("green")))
            else:
                print('Com: No')
        if 'hearts' in touch_1:
            print('You: Do you have any Hearts?')
            if 'Hearts' in str(com_fullHand):
                print('Com: Yes')
                cards_inHand = len(user_fullHand)
                if cards_inHand >= 7:
                    print(
                        stylize(
                            'Your hand is full, would you like to discard a card? y/n',
                            colored.fg("red")))
                    yesno_ans = str(input())
                    if yesno_ans == 'y':
                        try:
                            discard_card = input('Card: ')
                            user_fullHand.remove(discard_card)
                            print(
                                stylize("[-1] " + discard_card,
                                        colored.fg("red")))
                        except ValueError:
                            print(
                                stylize("You don't own this card!",
                                        colored.fg("red")))
                            touch()
                        new_card = random.choice(nums) + ' of Spades'
                        user_fullHand.append(new_card)
                        print(stylize("[+1] " + new_card, colored.fg("green")))
                    elif yesno_ans == 'n':
                        touch()
                    else:
                        print(stylize('Invalid input!', colored.fg("red")))
                        touch()
                else:
                    new_card = random.choice(nums) + ' of Spades'
                    user_fullHand.append(new_card)
                    print(stylize("[+1] " + new_card, colored.fg("green")))
            else:
                print('Com: No')
        if 'diamonds' in touch_1:
            print('You: Do you have any Diamonds?')
            if 'Diamonds' in str(com_fullHand):
                print('Com: Yes')
                cards_inHand = len(user_fullHand)
                if cards_inHand >= 7:
                    print(
                        stylize(
                            'Your hand is full, would you like to discard a card? y/n',
                            colored.fg("red")))
                    yesno_ans = str(input())
                    if yesno_ans == 'y':
                        try:
                            discard_card = input('Card: ')
                            user_fullHand.remove(discard_card)
                            print(
                                stylize("[-1] " + discard_card,
                                        colored.fg("red")))
                        except ValueError:
                            print(
                                stylize("You don't own this card!",
                                        colored.fg("red")))
                            touch()
                        new_card = random.choice(nums) + ' of Diamonds'
                        user_fullHand.append(new_card)
                        print(stylize("[+1] " + new_card, colored.fg("green")))
                    elif yesno_ans == 'n':
                        touch()
                    else:
                        print(stylize('Invalid input!', colored.fg("red")))
                        touch()
                else:
                    new_card = random.choice(nums) + ' of Spades'
                    user_fullHand.append(new_card)
                    print(stylize("[+1] " + new_card, colored.fg("green")))
            else:
                print('Com: No')
        if 'clubs' in touch_1:
            print('You: Do you have any Clubs?')
            if 'Spades' in str(com_fullHand):
                print('Com: Yes')
                cards_inHand = len(user_fullHand)
                if cards_inHand >= 7:
                    print(
                        stylize(
                            'Your hand is full, would you like to discard a card? y/n',
                            colored.fg("red")))
                    yesno_ans = str(input())
                    if yesno_ans == 'y':
                        try:
                            discard_card = input('Card: ')
                            user_fullHand.remove(discard_card)
                            print(
                                stylize("[-1] " + discard_card,
                                        colored.fg("red")))
                        except ValueError:
                            print(
                                stylize("You don't own this card!",
                                        colored.fg("red")))
                            touch()
                        new_card = random.choice(nums) + ' of Spades'
                        user_fullHand.append(new_card)
                        print(stylize("[+1] " + new_card, colored.fg("green")))
                    elif yesno_ans == 'n':
                        touch()
                    else:
                        print(stylize('Invalid input!', colored.fg("red")))
                        touch()
                else:
                    new_card = random.choice(nums) + ' of Spades'
                    user_fullHand.append(new_card)
                    print(stylize("[+1] " + new_card, colored.fg("green")))
            else:
                print(random.com_noResponses)

    # Displays the user's hand
    if 'hand' in touch_1:
        show_yourHand()

    # Discards inputted cards
    if 'discard' in touch_1:
        try:
            card1 = input('Card: ')
            user_fullHand.remove(str(card1))
            print(stylize("[-1] " + card1, colored.fg("red")))
        except ValueError:
            print(stylize("You don't own this card!", colored.fg("red")))

    # Merges two cards of a mentioned suit
    if 'merge' in touch_1:
        card1 = input('Card 1: ')
        try:
            user_fullHand.remove(str(card1))
        except ValueError:
            print(stylize("You don't own this card!", colored.fg("red")))
            touch()
        card2 = input('Card 2: ')
        try:
            user_fullHand.remove(str(card2))
        except ValueError:
            print(stylize("You don't own this card!", colored.fg("red")))
            touch()
        if 'Spades' in card1 and card2:
            if 'Merge' not in card1 and card2:
                print(stylize("[-2] Spades suit", colored.fg("red")))
                new_card = 'Spades Merge'
                user_fullHand.append(new_card)
                print(stylize("[+1] Spades Merge", colored.fg("green")))
        if 'Hearts' in card1 and card2:
            if 'Merge' not in card1 and card2:
                print(stylize("[-2] Hearts suit", colored.fg("red")))
                new_card = 'Hearts Merge'
                user_fullHand.append(new_card)
                print(stylize("[+1] Hearts Merge", colored.fg("green")))
        if 'Diamonds' in card1 and card2:
            if 'Merge' not in card1 and card2:
                print(stylize("[-2] Diamonds suit", colored.fg("red")))
                new_card = 'Diamonds Merge'
                user_fullHand.append(new_card)
                print(stylize("[+1] Diamonds Merge", colored.fg("green")))
        if 'Clubs' in card1 and card2:
            if 'Merge' not in card1 and card2:
                print(stylize("[-2] Clubs suit", colored.fg("red")))
                new_card = 'Clubs Merge'
                user_fullHand.append(new_card)
                print(stylize("[+1] Clubs Merge", colored.fg("green")))
        if 'Merge' in card1 and card2:
            if 'Merge x2' not in card1 and card2:
                if 'Spades' in card1 and card2:
                    print(stylize("[-2] Spades Merge", colored.fg("red")))
                    new_card = 'Spades Merge x2'
                    user_fullHand.append(new_card)
                    print(stylize("[+1] Spades Merge x2", colored.fg("green")))
                if 'Hearts' in card1 and card2:
                    print(stylize("[-2] Hearts Merge", colored.fg("red")))
                    new_card = 'Hearts Merge x2'
                    user_fullHand.append(new_card)
                    print(stylize("[+1] Hearts Merge x2", colored.fg("green")))
                if 'Diamonds' in card1 and card2:
                    print(stylize("[-2] Diamonds Merge", colored.fg("red")))
                    new_card = 'Diamonds Merge x2'
                    user_fullHand.append(new_card)
                    print(
                        stylize("[+1] Diamonds Merge x2", colored.fg("green")))
                if 'Clubs' in card1 and card2:
                    print(stylize("[-2] Clubs Merge", colored.fg("red")))
                    new_card = 'Clubs Merge x2'
                    user_fullHand.append(new_card)
                    print(stylize("[+1] Clubs Merge x2", colored.fg("green")))
        if 'Merge x2' in card1 and card2:
            if 'Spades' in card1 and card2:
                print(stylize("[-2] Spades Merge x2", colored.fg("red")))
                new_card = 'Quad Spades Merge '
                user_fullHand.append(new_card)
                print(stylize("[+1] Quad Spades Merge", colored.fg("green")))
            if 'Hearts' in card1 and card2:
                print(stylize("[-2] Hearts Merge x2", colored.fg("red")))
                new_card = 'Quad Hearts Merge'
                user_fullHand.append(new_card)
                print(stylize("[+1] Quad Hearts Merge", colored.fg("green")))
            if 'Diamonds' in card1 and card2:
                print(stylize("[-2] Diamonds Merge x2", colored.fg("red")))
                new_card = 'Quad Diamonds Merge '
                user_fullHand.append(new_card)
                print(stylize("[+1] Quad Diamonds Merge", colored.fg("green")))
            if 'Clubs' in card1 and card2:
                print(stylize("[-2] Clubs Merge x2", colored.fg("red")))
                new_card = 'Quad Clubs Merge '
                user_fullHand.append(new_card)
                print(stylize("[+1] Quad Clubs Merge", colored.fg("green")))

    # Restarts program after action
    touch()


# Displays the instructions for normal and instructions for hard, dependent on launch options
def start():
    if launch_exceptions == 1:
        print('''
  
▄▀█ █▀▄ █▀▄▀█ █ █▄░█   █▀▄▀█ █▀█ █▀▄ █▀▀
█▀█ █▄▀ █░▀░█ █ █░▀█   █░▀░█ █▄█ █▄▀ ██▄
''')
    print(
        "Welcome to ADMIN MODE, this mode isn't really as intense as is looks, this mode is mainly used just to debug code and play around with the mechanics. Checking hands with the bot will always come out with 'no' because the bot is not set to have any cards. Have fun!"
    )
    show_yourHand()
    touch()


if launch_exceptions == 0:
    print('''
█▀▄▀█ █▀▀ █▀█ █▀▀ █▀▀ █▀▀ ▄▀█ █▀█ █▀▄ █▀
█░▀░█ ██▄ █▀▄ █▄█ ██▄ █▄▄ █▀█ █▀▄ █▄▀ ▄█
''')
    print(
        'Instructions: Get 3 "Merge Cards" to win. To merge two cards, type "merge" and input the two cards you would like to merge, make sure they are the same suit or they will be unable to be merged. To check if the COM user has a card, type "check + the suit of the card" and the COM will notify you if they have that suit. Good luck, your hand is generated below!'
    )
    show_yourHand()
    touch()


# ADMIN MODE menu for card generation, notif. phrase and menu options
def adminMenu(op):
    if launch_exceptions == 0:
        pass
    if launch_exceptions == 1:
        user_fullHand = []
        print('\n')
        if op == True:
            print(
                stylize(
                    '**ADMIN MODE IS ENABLED, TO DISABLE: SET THE LAUNCH_EXCEPTIONS VARIABLE TO 0',
                    colored.fg("red")))
        elif op == False:
            pass
        try:
            count = int(input('Spades: '))
            for x in range(0, count):
                new_card = random.choice(nums) + ' of Spades'
                user_fullHand.append(new_card)
        except ValueError:
            print(
                stylize('Please insert a numerical value!', colored.fg("red")))
            adminMenu(False)
        try:
            count = int(input('Clubs: '))
            for x in range(0, count):
                new_card = random.choice(nums) + ' of Clubs'
                user_fullHand.append(new_card)
        except ValueError:
            print(
                stylize('Please insert a numerical value!', colored.fg("red")))
            adminMenu(False)
        try:
            count = int(input('Diamonds: '))
            for x in range(0, count):
                new_card = random.choice(nums) + ' of Diamonds'
                user_fullHand.append(new_card)
        except ValueError:
            print(
                stylize('Please insert a numerical value!', colored.fg("red")))
            adminMenu(False)
        try:
            count = int(input('Hearts: '))
            for x in range(0, count):
                new_card = random.choice(nums) + ' of Hearts'
                user_fullHand.append(new_card)
        except ValueError:
            print(
                stylize('Please insert a numerical value!', colored.fg("red")))
            adminMenu(False)
        start()


# Calling functions

adminMenu(True)
