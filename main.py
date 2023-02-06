from random import randint
import sys


def run_game():
    character_select()
    beast_battle()


def beast_battle(character):
    while character.hp > 0:
        beast = Character()
        beastHP = 30
        beastAttack = 3
        print(
            f"The first beast enters the arena. It's tail is thick and spiked, You lock eyes and show no fear! It's HP is {beastHP} and it's attack is {beastAttack}\n")
        while beastHP > 0:
            beastMove = randint(1, 2)
            move = int(input("Choose (1-2) to anticipate the beasts move!\n"
                             "Your move: "))
            if move == beastMove:
                beastHP -= attack
                print(f"Beasts move: {beastMove}")
                if beastHP > 0:
                    print(f"You dodged the beasts attack and struck! Beast HP is now {beastHP}")
                else:
                    break
            else:
                hp -= beastAttack
                print(f"Beasts move: {beastMove}")
                if hp > 0:
                    print(f"You've been struck by the beast! Your HP is now {hp}!")
                else:
                    break
        print("the beast has been defeated! You won't be so lucky on the next beast. Good luck...")
        beastHP = 25
        beastAttack = 4
        while beastHP > 0:
            beastMove = randint(1, 3)
            move = int(input("Choose (1-3) to anticipate the beasts move!\n"
                             "Your move: "))
            if move == beastMove:
                beastHP -= attack
                print(f"Beasts move: {beastMove}")
                if beastHP > 0:
                    print(f"You dodged the beasts attack and struck! Beast HP is now {beastHP}")
                else:
                    break
            else:
                hp -= beastAttack
                print(f"Beasts move: {beastMove}")
                if hp > 0:
                    print(f"You've been struck by the beast! Your HP is now {hp}!")
                else:
                    break
        print("You have conquered the second beast! This next beast is even harder, Good luck...")
        beastHP = 20
        beastAttack = 5
        while beastHP > 0:
            beastMove = randint(1, 4)
            move = int(input("Choose (1-4) to anticipate the beasts move!\n"
                             "Your move: "))
            if move == beastMove:
                beastHP -= attack
                print(f"Beasts move: {beastMove}")
                if beastHP > 0:
                    print(f"You dodged the beasts attack and struck! Beast HP is now {beastHP}")
                else:
                    break
            else:
                hp -= beastAttack
                print(f"Beasts move: {beastMove}")
                if hp > 0:
                    print(f"You've been struck by the beast! Your HP is now {hp}!")
                else:
                    break
        if hp > 0:
            print("How you have survived, I have no idea. Great job conquering all beasts!")
        else:
            break
        break


def character_select():
    character = input("Welcome to the arena! Please choose your character:\n"
                      "(1) Samurai\n"
                      "(2) Prisoner\n"
                      "(3) Prophet\n")

    match character:
        case "1":
            character = Character("Samurai", 10, 20)
        case "2":
            character = Character("Prisoner", 20, 6)
        case "3":
            character = Character("Prophet", 30, 4)
        case _:
            character = Character("Hero", 100, 30)

    print(f"You have chosen the {character.name}! Your HP is {character.hp} and your attack is {character.attack}! Good luck in Battle!..")
    return character


def you_died():
    print("you Died!")
    sys.exit()


class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack


beasts = [
    {"name": "Grimclaw", "hp": 100, "attack": 50},
    {"name": "Shadowfang", "hp": 90, "attack": 60},
    {"name": "Thunderhoof", "hp": 110, "attack": 40},
    {"name": "Bloodtusk", "hp": 80, "attack": 70},
    {"name": "Firebreather", "hp": 120, "attack": 30}]
