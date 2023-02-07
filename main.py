from random import randint
import sys


def run_game():
    character = character_select()
    beast_battle(character)


def character_select():
    character = input("Welcome to the arena! Please choose your character:\n"
                      "(1) Samurai\n"
                      "(2) Prisoner\n"
                      "(3) Prophet\n")

    match character:
        case "1":
            return Character("Samurai", 10, 20)
        case "2":
            return Character("Prisoner", 20, 6)
        case "3":
            return Character("Prophet", 30, 4)
        case "H":
            return Character("Hero", 100, 30)
        case _:
            print("Please choose an available option")
            run_game()


def you_died():
    print("You Died!")
    run_game()


def beast_battle(character):
    print(
        f"You have chosen the {character.name}! Your HP is {character.hp} and your attack is {character.attack}! Good luck in Battle!..")

    while character.hp > 0:
        beast_name = beasts[1]["name"]
        beast_hp = beasts[1]["hp"]
        beast_attack = beasts[1]["attack"]
        print(
            f"{beast_name} enters the arena. It's tail is thick and spiked, You lock eyes and show no fear! It's HP is {beast_hp} and it's attack is {beast_attack}\n")
        while beast_hp > 0:
            # beast_move = randint(0, 10)
            beast_move = 4
            move = int(input("Choose (0-9) to anticipate the beasts move!\n"
                             "Your move: "))
            if move != beast_move:
                beast_hp -= character.attack
                print(f"Beasts move: {beast_move}")
                if beast_hp > 0:
                    print(f"You dodged the beasts attack and struck! Beast HP is now {beast_hp}")
                else:
                    break
            else:
                character.hp -= beast_attack
                print(f"Beasts move: {beast_move}")
                if character.hp > 0:
                    print(f"You've been struck by the beast! Your HP is now {character.hp}!")
                else:
                    you_died()
        print("the beast has been defeated! You won't be so lucky on the next beast. Good luck...")
        beast_name = "Shadowfang"
        beast_hp = 90
        beast_attack = 60
        while beast_hp > 0:
            beast_move = randint(1, 3)
            move = int(input("Choose (1-3) to anticipate the beasts move!\n"
                             "Your move: "))
            if move == beast_move:
                beast_hp -= attack
                print(f"Beasts move: {beast_move}")
                if beast_hp > 0:
                    print(f"You dodged the beasts attack and struck! Beast HP is now {beast_hp}")
                else:
                    break
            else:
                hp -= beast_attack
                print(f"Beasts move: {beast_move}")
                if hp > 0:
                    print(f"You've been struck by the beast! Your HP is now {hp}!")
                else:
                    break
        print("You have conquered the second beast! This next beast is even harder, Good luck...")
        beast_hp = 20
        beast_attack = 5
        while beast_hp > 0:
            beast_move = randint(1, 4)
            move = int(input("Choose (1-4) to anticipate the beasts move!\n"
                             "Your move: "))
            if move == beast_move:
                beast_hp -= attack
                print(f"Beasts move: {beast_move}")
                if beast_hp > 0:
                    print(f"You dodged the beasts attack and struck! Beast HP is now {beast_hp}")
                else:
                    break
            else:
                hp -= beast_attack
                print(f"Beasts move: {beast_move}")
                if hp > 0:
                    print(f"You've been struck by the beast! Your HP is now {hp}!")
                else:
                    break
        if hp > 0:
            print("How you have survived, I have no idea. Great job conquering all beasts!")
        else:
            break
        break


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

run_game()
