# Class Template

# Hero Ability Scores
hero_ab_scores = {
            "Strength" : 0,
            "Dexterity" : 0,
            "Constitution" : 0,
            "Intelligence" : 0,
            "Wisdom" : 0,
            "Charisma" : 0
            }
            
# Hero Ability Modifiers
hero_ab_mods = {
        "Strength"     : 0,
        "Dexterity"    : 0,
        "Constitution" : 0,
        "Intelligence" : 0,
        "Wisdom"       : 0,
        "Charisma"     : 0
        }

# Hero CLass
hero_class = {
        "initial_hp" : 0,
        "initial_surge" : 0,
        "feats" : []
        }

# Hero Hit Points/Surges
hero_hitpoints = {
        "maxhp" : 0,
        "bloodied" : 0,
        "surgeval" : 0, 
        "surgenum" : 0 # Dependent on class
        }

# Class Description
def class_descr():
	print("Description\n")
	print("> Role: ")
	print("> Power Source: ")
	print("> Key Abilities: \n")
	print("> Armor Proficiencies: ")
	print("> Weapon Proficiencies: ")
	print("> Bonus to Defense: \n")
	print("> Hit Points at 1st Level: ")
	print("> Hit Points per Level Gained: ")
	print("> Healing Surges per Day: \n")
	print("Trained Skills: Choose x trained skills from the list below:")
	print("> ")
	print("> ")
	print("> ")
	print("> ")
	print("> \n")
	print("> Build Options: ")
	print("> Class have the following Class Features:")
	print(">  ")
	print(">  ")
	print(">  ")

# Class Initial Stats/Feats
def class_initial():
	hero_hitpoints["maxhp"] = 
    hero_class["initial_hp"] = 
    hero_hitpoints["surgenum"] = 
    hero_class["feats"].append("")
    hero_class["feats"].append("")
    hero_class["feats"].append("")