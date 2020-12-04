# Character Health

hero_ab_scores = {
            "Strength" : 16,
            "Dexterity" : 14,
            "Constitution" : 23,
            "Intelligence" : 13,
            "Wisdom" : 16,
            "Charisma" : 14
            }
hero_ab_mods = {
        "Strength"     : 0,
        "Dexterity"    : 0,
        "Constitution" : 5,
        "Intelligence" : 0,
        "Wisdom"       : 0,
        "Charisma"     : 0
        }

hero_class = {
        "initial_hp" : 12,
        "initial_surge" : 7
        }

# Hero Hit Points/Surges
hero_hitpoints = {
        "maxhp" : 0,
        "bloodied" : 0,
        "surgeval" : 0, 
        "surgenum" : 0 # Dependent on class
        }

def health():
    hero_hitpoints["maxhp"] += hero_class["initial_hp"] + hero_ab_scores["Constitution"]
    hero_hitpoints["bloodied"] += int(hero_hitpoints["maxhp"] / 2)
    hero_hitpoints["surgeval"] += int(hero_hitpoints["maxhp"] / 4)
    hero_hitpoints["surgenum"] += hero_class["initial_surge"] + hero_ab_mods["Constitution"]
    
health()

print(hero_hitpoints)