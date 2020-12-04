#FINAL Ability Modifiers

hero_ab_scores = {
        "Strength"     : 11,
        "Dexterity"    : 13,
        "Constitution" : 15,
        "Intelligence" : 17,
        "Wisdom"       : 19,
        "Charisma"     : 21,
        }

hero_ab_mods = {
        "Strength"     : 0,
        "Dexterity"    : 0,
        "Constitution" : 0,
        "Intelligence" : 0,
        "Wisdom"       : 0,
        "Charisma"     : 0
        }

def ability_mods(x):
    if hero_ab_scores[x] <= 11:
        hero_ab_mods[x] = 0
    elif hero_ab_scores[x] == 12 or hero_ab_scores[x] == 13:
        hero_ab_mods[x] = 1
    elif hero_ab_scores[x] == 14 or hero_ab_scores[x] == 15:
        hero_ab_mods[x] = 2
    elif hero_ab_scores[x] == 16 or hero_ab_scores[x] == 17:
        hero_ab_mods[x] = 3
    elif hero_ab_scores[x] == 18 or hero_ab_scores[x] == 19:
        hero_ab_mods[x] = 4
    elif hero_ab_scores[x] >= 20:
        hero_ab_mods[x] = 5

def hero_mods():
    for x in hero_ab_mods:
        ability_mods(x)
hero_mods()
print(hero_ab_mods)
