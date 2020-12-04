
import random

def reroll_stats(x):
    hero_ab_scores[x] = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    hero_ab_scores[x].sort()
    hero_ab_scores[x].reverse()
    hero_ab_scores[x] = (hero_ab_scores[x][0] + hero_ab_scores[x][1] + hero_ab_scores[x][2])
    if hero_ab_scores[x] < 10:
        hero_ab_scores[x] = 10
    print("Your %s stat is now %s." % (x, hero_ab_scores[x]))

def reroll():
    while True:
        rrconfirm = input("\nWould you like to reroll one of your stats?: ")
        rrconfirm = rrconfirm.lower()
        if rrconfirm == "yes" or rrconfirm == "y":
            rrstat = int(input("Sounds good. Which stat would you like to reroll?: "))
            for scores in abili
            rrstat = str(rrstat)
            #if rrstat in hero_ab_scores:
            #    reroll_stats(rrstat)
            if rrstat == "Strength":
                reroll_stats(rrstat)
            elif rrstat == "Dexterity":
                reroll_stats(rrstat)
            elif rrstat == "Constitution":
                reroll_stats(rrstat)
            elif rrstat == "Intelligence":
                reroll_stats(rrstat)
            elif rrstat == "Wisdom":
                reroll_stats(rrstat)
            elif rrstat == "Charisma":
                reroll_stats(rrstat)
            else:
                print("Unknown input. Please try again.")
                reroll()
        elif rrconfirm == "no" or rrconfirm == "n":
            print("Sounds good! Let's continue.")
        else:
            print("Unknown input. Please type 'yes' or 'no'.")
            reroll()

reroll()
