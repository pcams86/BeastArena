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
            return Character("Samurai", 150, 70)
        case "2":
            return Character("Prisoner", 250, 40)
        case "3":
            return Character("Prophet", 350, 30)
        case "H":
            return Character("Hero", 1000, 10000)
        case _:
            print("Please choose an available option")
            run_game()


def you_died():
    print("You Died!")
    run_game()


def beast_battle(character):
    print(
        f"You have chosen the {character.name}! Your HP is {character.hp} and your attack is {character.attack}! Good luck in Battle!..")
    move_range = 9

    while character.hp > 0:
        beast_number = randint(0, len(beasts) - 1)
        beast_name = beasts[beast_number]["name"]
        beast_hp = beasts[beast_number]["hp"]
        beast_attack = beasts[beast_number]["attack"]
        beast_story = beasts[beast_number]["story"]
        del beasts[beast_number]
        print(beast_story)
        while beast_hp > 0:
            beast_move = randint(0, move_range)
            # beast_move = 4
            move = int(input(f"Choose (0-{move_range}) to anticipate the beasts move!\n"
                             "Your move: "))
            if move > move_range or move < 0:
                print("Dude, come on...")
            elif move != beast_move:
                beast_hp -= character.attack
                print(f"Beasts move: {beast_move}")
                if beast_hp > 0:
                    print(f"You dodged {beast_name}'s attack and struck! {beast_name}'s HP is now {beast_hp}")
                else:
                    move_range -= 2
                    break
            else:
                character.hp -= beast_attack
                print(f"Beasts move: {beast_move}")
                if character.hp > 0:
                    print(f"You've been struck by the beast! Your HP is now {character.hp}!")
                else:
                    you_died()
        if len(beasts) != 0:
            print("**********************************************************************************\n"
                  "the beast has been defeated! You won't be so lucky on the next beast. Good luck...\n"
                  "**********************************************************************************")
        else:
            print(f"CONGRATULATIONS {character.name}! YOU HAVE SURVIVED THE BEAST ARENA")
            sys.exit()


class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack


beasts = [
    {"name": "Grimclaw", "hp": 100, "attack": 50, "story": "Grimclaw's story"},
    {"name": "Shadowfang", "hp": 90, "attack": 60, "story": "Shadowfangs's story"},
    {"name": "Thunderhoof", "hp": 110, "attack": 40, "story": "Thunderhoof's story"},
    {"name": "Bloodtusk", "hp": 80, "attack": 70, "story": "Bloodtusk's story"},
    {"name": "Firebreather", "hp": 120, "attack": 30, "story": "Firebreather's story"}]

run_game()
