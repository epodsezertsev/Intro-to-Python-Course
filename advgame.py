import time
import random


def print_pause(string):
    print(string)
    time.sleep(0)


def valid_input(prompt, options):
    while True:
        response = input(prompt)
        if response in options:
            break
        print_pause("Please input a valid number.")
    return response


def intro():
    print_pause("You wake up on a wooden carriage with your hands tied.")
    print_pause("You feel the carriage shake as the wooden wheels go "
                "over old cobblestone.")
    print_pause("You are surrounded by snowy mountain peaks and "
                "luscious pine trees.")
    print_pause("\"Hey you! You're finally awake!\"")
    print_pause("After some conversation, you realize you are in a cart "
                "with captured criminals")
    print_pause("The carriage hits a partuclarly big rock that distracts "
                "the guards.")


def run_away(inventory):
    if "weapon" in inventory:
        print_pause("You try to run and get caught by the guards.")
        print_pause("You fight them off and escape...")
        print_pause("Now you are forced to live in exhile.")
    else:
        print_pause("You try to run, but the guards shoot you with an arrow.")
    print_pause("GAME OVER")
    play_again()


def fight(inventory):
    if "weapon" in inventory:
        print_pause("You fight the monster with everything you've got!")
        print_pause("The mighty weapon in your hands helps slay the monster!")
        print_pause("Congratulations, you've become the town hero! YOU WON!!!")
    else:
        print_pause("You fight the monster with everything you've got!")
        print_pause("Unfortunately your might alone is not enough..")
        print_pause("GAME OVER")
    play_again()


def cart_chapter(weapons, enemy, inventory):
    cart_run = valid_input("Do you want to use this distraction to run?"
                           "\n1. Yes."
                           "\n2. No.\n", ["1", "2"])
    if cart_run == "1":
        run_away(inventory)
    elif cart_run == "2":
        print_pause("You decide to stay.")
        print_pause("The carriage eventually ends up in a small town "
                    "and stops.")
        print_pause("\"Why did we stop?\"")
        print_pause("\"Why do you think? We've reached the end of the line.\"")
        print_pause("The guards line up all the prisoners in front "
                    "of the gallows.")
        print_pause("As you are getting out of the cart you see an "
                    "opportunity to run.")
        gallows_chapter(weapons, enemy, inventory)


def gallows_chapter(weapons, enemy, inventory):
    gallows = valid_input("Do you want to run?"
                          "\n1. Yes."
                          "\n2. No.\n", ["1", "2"])
    if gallows == "1":
        run_away(inventory)
    elif gallows == "2":
        final_conflict(weapons, enemy, inventory)


def final_conflict(weapons, enemy, inventory):
    attacker = random.choice(enemy)
    weapon = random.choice(weapons)
    print_pause("You decide to stay.")
    print_pause("Suddenly, there is a horrific scream!")
    print_pause(f"The village is being attacked by a {attacker}!!!")
    print_pause(f"One of the guards is startled and drops his {weapon} "
                "as he tries to run.")
    print_pause(f"Do you want to pick up the {weapon}, fight "
                f"the {attacker}, or run?")
    conflict = valid_input("1. Pick up the weapon."
                           "\n2. Fight."
                           "\n3. Run.\n", ["1", "2", "3"])
    if conflict == "1":
        weapon_acquired(weapon, attacker, inventory)
    elif conflict == "2":
        fight(inventory)
    elif conflict == "3":
        run_away(inventory)


def weapon_acquired(weapon, attacker, inventory):
    inventory.append("weapon")
    print_pause(f"You picked up the {weapon} and it feels great "
                "in your hands!")
    print_pause(f"Do you want to fight the {attacker}, or run away?")
    final_fight = valid_input("1. Fight"
                              "\n2. Run.\n", ["1", "2"])
    if final_fight == "1":
        fight(inventory)
    if final_fight == "2":
        run_away(inventory)


def play_game():
    weapons = ["broadsword", "longbow", "mace", "axe", "halberd", "crossbow"]
    enemy = ["dragon", "troll", "giant", "witch", "werewolf", "vampire"]
    inventory = []
    intro()
    cart_chapter(weapons, enemy, inventory)


def play_again():
    replay = valid_input("Would you like to play again?"
                         "\n1. Yes"
                         "\n2. No\n", ["1", "2"])
    if replay == "1":
        play_game()


play_game()
