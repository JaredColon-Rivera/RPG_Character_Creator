# Updated DND GUI

from graphics import *

hero_name = {
		"name" : "Barbarosas"
		}

hero_level = {
		"level" : 1
		}

hero_class = {
		"class" : "Sorcerer"
		}

hero_race = {
		"race" : "Dragonborn",
		"speed" : 6,
		"languages" : [],
		"feats" : []
		}

hero_race["feats"].append("Cast-Iron Stomach")
hero_race["feats"].append("Dwarven Resilience")
hero_race["feats"].append("Dwarven Weapon Proficiency")
hero_race["feats"].append("Encumbered Speed")
hero_race["feats"].append("Stand Your Ground")
hero_race["feats"].append("Low-Light Vision")

hero_race["languages"].append("Common")
hero_race["languages"].append("Draconic")
hero_race["languages"].append("Dwarven")

hero_gender = {
		"gender": "Female"
		}

hero_alnmt = {
		"alnmt" : "Lawful Neutral"
		}

hero_ab_scores = {
            "Strength" : 16,
            "Dexterity" : 14,
            "Constitution" : 20,
            "Intelligence" : 13,
            "Wisdom" : 16,
            "Charisma" : 14
            }

hero_ab_mods = {
        "Strength"     : 3,
        "Dexterity"    : 2,
        "Constitution" : 5,
        "Intelligence" : 1,
        "Wisdom"       : 3,
        "Charisma"     : 2
        }

# Hero Defenses
hero_defense = {
        "AC"   : 12,
        "FORT" : 13,
        "REF"  : 13,
        "WILL" : 14
        }

hero_skills = {
        "Acrobatics" : 0,
        "Arcana" : 0,
        "Athletics" : 0,
        "Bluff": 0,
        "Diplomacy" : 0,
        "Dungeoneering" : 0,
        "Endurance" : 0,
        "Heal" : 0,
        "History" : 0,
        "Insight" : 10,
        "Intimidate" : 0,
        "Nature" : 0,
        "Perception" : 10,
        "Religion" : 0,
        "Stealth" : 0,
        "Streetwise" : 0,
        "Thievery" : 0        
        }

# Hero Hit Points/Surges
hero_hitpoints = {
        "maxhp" : 60,
        "bloodied" : 30,
        "surgeval" : 15,
        "surgenum" : 10
        }

def dndgui():
	win = GraphWin("DND Character Creation", 750, 750)
	win.setCoords(0, 0, 100, 100)

	# Box Constructor
	def boxes(box, xp1, yp1, xp2, yp2):
		box = Rectangle(Point(xp1, yp1), Point(xp2, yp2))
		box.setFill("white")
		box.draw(win)

#---------------Title Section---------------#	

	# Title Box
	boxes("title_box", 20, 95.5, 80, 98.5)

	# Title
	Text(Point(50, 97), "DUNGEONS AND DRAGONS CHARACTER SHEET").draw(win)

#---------------First Section---------------#

	# First Box
	boxes("first_box", 5, 88, 95, 95)

	# Player Name
	#boxes("name_box", 5.75, 92, 22.25, 94.25)
	Text(Point(14, 93), "Character Name:").draw(win)
	Text(Point(29, 93), hero_name["name"]).draw(win)

	# Level
	#boxes("level_box", 45.75, 92, 52.2, 94.25)
	Text(Point(49, 93), "Level:").draw(win)
	Text(Point(56, 93), hero_level["level"]).draw(win)

	# Class
	#boxes("class_box", 69.75, 92, 76.25, 94.25)
	Text(Point(73, 93), "Class:").draw(win)
	Text(Point(84, 93), hero_class["class"]).draw(win)

	# Race
	#boxes("race_box", 15.75, 88.90, 22.25, 91.25)
	Text(Point(19.25, 90), "Race:").draw(win)
	Text(Point(29, 90), hero_race["race"]).draw(win)

	# Gender
	#boxes("gender_box", 44, 88.90, 52.25, 91.25)
	Text(Point(48, 90), "Gender:").draw(win)
	Text(Point(57, 90), hero_gender["gender"]).draw(win)

	# Alignment
	#boxes("alnmt_box", 65.75, 88.70, 76.25, 91.25)
	Text(Point(71, 90), "Alignment:").draw(win)
	Text(Point(84, 90), hero_alnmt["alnmt"]).draw(win)

#---------------Ability Scores/Mods Section---------------#

	# Ability Scores/Mods Box
	boxes("ab_box", 5, 65.50, 41.5, 87.50)

	# Ability Scores Text
	Text(Point(25, 86), "Ability Scores / Modifiers").draw(win)

	Text(Point(15, 83), "Strength:").draw(win)
	Text(Point(14.80, 80), "Dexterity:").draw(win)
	Text(Point(13.50, 77), "Constitution:").draw(win)
	Text(Point(13.75, 74), "Intelligence:").draw(win)
	Text(Point(15.10, 71), "Wisdom:").draw(win)
	Text(Point(14.50, 68), "Charisma:").draw(win)

	# Ability Scores Output
	i = -3
	for x in hero_ab_scores:
		i += 3
		Text(Point(23, 83 - i),hero_ab_scores[x]).draw(win)

	# Ability Mods Output
	i = -3
	for x in hero_ab_mods:
		i += 3
		Text(Point(31, 83 - i), "+ %s" % hero_ab_mods[x]).draw(win)

#---------------Defenses Section---------------#

	# Defenses Box
	boxes("defense_box", 42, 65.50, 58.5, 87.50)

	# Defenses
	Text(Point(50, 86), "Defenses").draw(win)

	# Defenses Text
	Text(Point(48, 82), "AC:").draw(win)
	Text(Point(46.6, 78), "FORT:").draw(win)
	Text(Point(47.3, 74), "REF:").draw(win)
	Text(Point(47, 70), "WILL:").draw(win)

	# Defenses Output
	i = -4
	for x in hero_defense:
		i += 4
		Text(Point(52, 82 - i), hero_defense[x]).draw(win)

#---------------Movement Section---------------#

	# Movement Box
	boxes("move_box", 59, 80, 95, 87.50)

	# Movement
	Text(Point(78, 86), "Movement").draw(win)
	Text(Point(76, 82), "Speed:").draw(win)
	Text(Point(82, 82), hero_race["speed"]).draw(win)

#---------------Senses Section---------------#

	# Senses Box
	boxes("sense_box", 59, 65.50, 95, 79.50)

	# Senses
	Text(Point(78, 78), "Senses").draw(win)

	Text(Point(73, 74), "Passive Insight:").draw(win)
	Text(Point(71, 70), "Passive Perception:").draw(win)

	# Senses Output
	Text(Point(83, 74), (10 + hero_skills["Perception"])).draw(win)
	Text(Point(83, 70), (10 + hero_skills["Insight"])).draw(win)

#---------------Skills Section---------------#

	# Skills Box
	boxes("skills_box", 5, 1, 41.5, 65)

	# Skills
	Text(Point(23.25, 62), "Skills").draw(win)

	i = -3
	for x in hero_skills:
		i += 3
		Text(Point(17, 58 - i),"%s:" % x).draw(win)

	# Skills Output
	i = -3
	for x in hero_skills:
		i += 3
		Text(Point(31,  58 - i), hero_skills[x]).draw(win)

#---------------Hit Points Section---------------#

	# Hit Points Box
	boxes("hp_box", 42, 51.50, 95, 65)

	# Hit Points/Healing Surges
	Text(Point(68.50, 62), "Hit Points").draw(win)

	Text(Point(58, 58), "Max HP:").draw(win)
	Text(Point(78, 58), "Bloodied:").draw(win)
	Text(Point(55.90, 55), "Surge Value:").draw(win)
	Text(Point(76.75, 55), "Surges/Day:").draw(win)

	# Hit Points/Healing Surges Output
	Text(Point(66, 58), hero_hitpoints["maxhp"]).draw(win)
	Text(Point(86, 58), hero_hitpoints["bloodied"]).draw(win)
	Text(Point(66, 55), hero_hitpoints["surgeval"]).draw(win)
	Text(Point(86, 55), hero_hitpoints["surgenum"]).draw(win)

#---------------Racial Features---------------#
	
	# Racial Feats Box
	boxes("racefeats_box", 42, 20.5, 95, 51)

	# Racial Feats
	Text(Point(68.5, 48), "Racial Features").draw(win)

	# Racial Feats Output
	i = -3
	for feats in hero_race["feats"]:
		i += 3
		Text(Point(68.5, 44 - i), feats).draw(win)

#---------------Languages---------------#

	# Languages Box
	boxes("lang_box", 42, 1, 95, 20)

	# Languages
	Text(Point(68.5, 17), "Languages Known").draw(win)

	# Languages Output
	i = -3
	for languages in hero_race["languages"]:
		i += 3
		Text(Point(68.5, 13 - i), languages).draw(win)


	win.getMouse()

dndgui()



