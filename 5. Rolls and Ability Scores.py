# FINAL Ability Score Rolls

import random

initial_rolls = {
            "1" : 0,
            "2" : 0,
            "3" : 0,
            "4" : 0,
            "5" : 0,
            "6" : 0
            }

ab_scores_list = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

hero_ab_scores = {
            "Strength" : 0,
            "Dexterity" : 0,
            "Constitution" : 0,
            "Intelligence" : 0,
            "Wisdom" : 0,
            "Charisma" : 0
            }


def show_ab_scores():
    print("\nYour ability scores are: ")
    for scores in ab_score_list:
        print("%s : %s" % (x, scores))

def rolls():
    for rolls in initial_rolls:
        initial_rolls[rolls] = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
        initial_rolls[rolls].sort()
        initial_rolls[rolls].reverse()
        initial_rolls[rolls] = (initial_rolls[rolls][0] + initial_rolls[rolls][1] + initial_rolls[rolls][2])
        if initial_rolls[rolls] < 10:
            initial_rolls[rolls] = 10
rolls()

def rolls_listed():
    print("\nYour rolls are below:")
    for x in initial_rolls:
        print("Roll %s is %s." % (x, initial_rolls[x]))

chosen_stat = ("That stat has been chosen. Please choose another number.")

def choosing(x):
    rolls_listed()
    choice = int(input("Which roll would you like to be your %s?: " % x))
    choice = str(ab_scores_list[choice - 1])
    print(choice)
    if choice in ab_scores_list:
        if initial_rolls[choice] == "Chosen":
            print(chosen_stat)
        else:
            hero_ab_scores[x] += initial_rolls[choice]
            initial_rolls[choice] = "Chosen"
            print("Your %s stat is %s." % (x, hero_ab_scores[x]))
    """ if choice == "1":
        if initial_rolls[choice] == "Chosen":
            print(chosen_stat)
        else:
            hero_ab_scores[x] += initial_rolls[choice]
            initial_rolls[choice] = "Chosen"
            print("Your %s stat is %s." % (x, hero_ab_scores[x]))
    elif choice == "2":
        if initial_rolls[choice] == "Chosen":
            print(chosen_stat)
        else:
            hero_ab_scores[x] += initial_rolls[choice]
            initial_rolls[choice] = "Chosen"
            print("Your %s stat is %s." % (x, hero_ab_scores[x]))
    elif choice == "3":
        if initial_rolls[choice] == "Chosen":
            print(chosen_stat)
        else:
            hero_ab_scores[x] += initial_rolls[choice]
            initial_rolls[choice] = "Chosen"
            print("Your %s stat is %s." % (x, hero_ab_scores[x]))
    elif choice == "4":
        if initial_rolls[choice] == "Chosen":
            print(chosen_stat)
        else:
            hero_ab_scores[x] += initial_rolls[choice]
            initial_rolls[choice] = "Chosen"
            print("Your %s stat is %s." % (x, hero_ab_scores[x]))
    elif choice == "5":
        if initial_rolls[choice] == "Chosen":
            print(chosen_stat)
        else:
            hero_ab_scores[x] += initial_rolls[choice]
            initial_rolls[choice] = "Chosen"
            print("Your %s stat is %s." % (x, hero_ab_scores[x]))
    elif choice == "6":
        if initial_rolls[choice] == "Chosen":
            print(chosen_stat)
        else:
            hero_ab_scores[x] += initial_rolls[choice]
            initial_rolls[choice] = "Chosen"
            print("Your %s stat is %s." % (x, hero_ab_scores[x]))"""
    """else:
        print("Please choose an option from 1 to 6")
        choosing(x)"""

def choosing_stats():
    for x in hero_ab_scores:
        choosing(x)
choosing_stats()

show_ab_scores()
