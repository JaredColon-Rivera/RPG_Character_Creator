# DND Defenses


# Hero Defenses
hero_defense = {
        "AC"   : 0,
        "FORT" : 0,
        "REF"  : 0,
        "WILL" : 0
        }

# Hero Ability Scores
hero_ab_scores = {
            "Strength" : 16,
            "Dexterity" : 14,
            "Constitution" : 20,
            "Intelligence" : 13,
            "Wisdom" : 16,
            "Charisma" : 14
            }

# Hero Ability Modifiers
hero_ab_mods = {
        "Strength"     : 3,
        "Dexterity"    : 2,
        "Constitution" : 5,
        "Intelligence" : 1,
        "Wisdom"       : 3,
        "Charisma"     : 2
        }

# Hero Defense
def defense():
    # AC
    if hero_ab_scores["Intelligence"] >= hero_ab_scores["Dexterity"]:
        hero_defense["AC"] = 10 + hero_ab_mods["Intelligence"]
    else:
        hero_defense["AC"] = 10 + hero_ab_mods["Dexterity"]
    # FORT
    if hero_ab_scores["Strength"] >= hero_ab_scores["Constitution"]:
        hero_defense["FORT"] = 10 + hero_ab_mods["Strength"]
    else:
        hero_defense["FORT"] = 10 + hero_ab_mods["Constitution"]

    # REF
    if hero_ab_scores["Dexterity"] >= hero_ab_scores["Intelligence"]:
        hero_defense["REF"] = 10 + hero_ab_mods["Dexterity"]
    else:
        hero_defense["REF"] = 10 + hero_ab_mods["Intelligence"]

    # WILL
    if hero_ab_scores["Wisdom"] >= hero_ab_scores["Charisma"]:
        hero_defense["WILL"] = 10 + hero_ab_mods["Wisdom"]
    else:
        hero_defense["WILL"] = 10 + hero_ab_mods["Charisma"]
        
defense()
