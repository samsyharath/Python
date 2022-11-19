'''
Fantasy Battle Game
By Samson Syharath
Date: 11/19/2022
'''

# This version contains answers to task 1-4 as well as all 5 bonus tasks.
import sys

wizard = "Wizard"
elf = "Elf"
human = "Human"
halfling = "Halfling"  # Halfling choice is Bonus task 3

wizard_hp = 70
elf_hp = 100
human_hp = 150
halfling_hp = 120

wizard_damage = 150
elf_damage = 100
human_damage = 20
halfling_damage = 50

dragon_hp = 300
dragon_damage = 50

choice = " "


def end_game():
    '''End Game'''
    sys.exit()


while True:  # Bonus task 5 (replay)
    while True:
        print("1)", wizard)
        print("2)", elf)
        print("3)", human)
        print("4)", halfling)  # Bonus task 3
        print("5) Exit")  # Bonus task 4
        print(' ')
        print("-" * 20 + "\n")

        choice = input("Choose your character: ").lower()

        if choice == "1" or choice == wizard.lower():  # the 'or' is for bonus 1 and 2
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break

        if choice == "2" or choice == elf.lower():  # the 'or' is for bonus 1 and 2
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break

        if choice == "3" or choice == human.lower():  # the 'or' is for bonus 1 and 2
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break

        if choice == "4" or choice == "Exit".lower:  # the 'or' is for bonus 1 and 2
            character = halfling
            my_hp = halfling_hp
            my_damage = halfling_damage
            break
        if choice == "5" or choice == "exit":
            end_game()

        print("Unknown character")
        break
    print("You have chosen the character: " + character)
    print("Health: " + str(my_hp))
    print("Damage: " + str(my_damage))

    while True:  # Battle sequence
        dragon_hp = dragon_hp - my_damage
        print("The", character, "damaged the Dragon!")
        print("The Dragon's health is now:", dragon_hp)
        print(' ')
        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            break

        my_hp = my_hp - dragon_damage
        print("The dragon strikes back at the", character)
        print("The", character+"\'s health is now", str(my_hp))
        print(' ')
        if my_hp <= 0:
            print("You have lost the battle.")
            break

    # Bonus Task 5 (replay)
    replay = input("Would you like to play again? ").lower()
    if replay == "yes" or replay == "y":
        dragon_hp = 300
        continue
    else:
        end_game()
