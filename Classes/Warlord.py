# Warlord Class
inspiring_presence = "When an ally who can see you spends an action point to take an extra action, that ally also regains \nlost hit points equal to one-half your level + your Charisma modifier. \nIf the ally can see multiple warlord allies who have this class feature, \nthe ally regains hit points from only one of them (the ally's choice)"
tactical_presence = "When an ally you can see spends an action point to make an extra attack, the ally gains a bonus to the \nattack roll equal to one-half your Intelligence modifier. \nIf multiple warlord allies who have this class feature can see the ally, he or \nshe gains the bonus from only one of them (the ally's choice)"
combat_leader = "You and each ally within 10 squares who can see and hear you gain a +2 power bonus to initiative"
commanding_presence = "Choose 1 of the following: \nInspiring Presence: %s, \nTactical Presence: %s" % (inspiring_presence, tactical_presence)
inspiring_word_descr = "You can use 'inspiring word' as an encounter power"

# Warlord Description
def warlord_descr():
	print("Warlords. Accomplished and competent battle leaders. \nThey stand in the front lines issuing commands in battle.\n")
	print("> Role: Leader. You are the inspiring commander and a master \nof battle tactics.\n")
	print("> Power Source: Martial. You have an expert in tactics through \nendless hours of training and practice personal determination \nand your own sheer physical toughness.")
	print("> Key Abilities: Strength, Intelligence, Charisma\n")
	print("> Armor Proficiencies: Cloth, Leather, Hide, Chainmail, Light Shield\n")
	print("> Weapon Proficiencies: Simple Melee, Military Melee, Simple Ranged\n")
	print("> Bonus to Defense: Fortitude +1, Will +1\n")
	print("> Hit Points at 1st level: 12 + Constitution Score")
	print("> Hit Points per level gained: 5")
	print("> Healing Surges per Day: 7 + Constitution Modifier\n")
	print("Trained Skills: Choose four trained skills from the list below:")
	print("> Athletics (Str)")
	print("> Diplomacy (Cha)")
	print("> Endurance (Con)")
	print("> Heal (Wis)")
	print("> History (Int)")
	print("> Intimidate (Cha)\n")
	print("Build options: Inspiring Warlord, Tactical Warlord")
	print("Warlords have the following Class Features:")
	print("> Combat Leader: %s" % combat_leader)
	print("> Commanding Presence: %s" % commanding_presence)
	print("> Inspiring Word: %s" % inspiring_word_descr)

warlord_descr()

# Warlord Initial Stats/Feats
def warlord_initial():
    hero_hitpoints["maxhp"] = 12 + hero_ab_scores["Constitution"]
    hero_class["initial_hp"] = hero_hitpoints["maxhp"]
    hero_hitpoints["surgenum"] = (7 + hero_ab_mods["Constitution"])
    hero_class["feats"].append("Combat Leader")
    hero_class["feats"].append("Commanding Presence")
    hero_class["feats"].append("Inspiring Word")

warlord_initial()