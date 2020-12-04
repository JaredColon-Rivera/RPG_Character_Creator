# DND Graphical Interface

from graphics import *

astiron_stomach = "+5 bonus to saving throws against poison"
dwarven_resilience = "You can use your second wind as a minor action instead of a standard action"
dwarven_weapon_prof = "You gain proficiency with the throwing hammer and the warhammer"
encumbered_speed = "You move at your normal speed even when it would normally be reduced by armor \nor a heavy load. (Difficult terrain or magical effects affect you normally)"
stand_your_ground = "When an effect forces you to move—through a pull, a push, or a slide—you can \nmove 1 square less than the effect specifies. \nIn addition, when an attack would knock you prone, you can immediately make a saving throw to avoid falling prone."

# Hero Name
hero_name = {
        "name" : "Jared"
        }

# Hero Level
hero_level = {
        "level" : 1
        }

# Hero Alignment
hero_alnmt = {
        "alnmt" : "Lawful Neutral"
        }

# Hero Gender
hero_gender = {
        "gender" : "Female"
        }

# Hero Race
hero_race = {
        "race" : 0,
        "size" : 0,
        "vision" : "Low-Light",
        }
        
# Hero Languages
hero_language = []
hero_language.append("Common")
hero_language.append("Draconic")
hero_language.append("Dwarven")

# Hero Feats
hero_race_feats = []
hero_race_feats.append("Cast-Iron Stomach")
hero_race_feats.append("Dwarven Resilience")
hero_race_feats.append("Dwarven Weapon Proficiency")
hero_race_feats.append("Encumbered Speed")
hero_race_feats.append("Stand Your Ground")

# Hero Class
hero_class = {
        "class" : "Sorcerer"
        }
hero_class_feats = []
hero_class_feats.append("Elemental Bolt")
hero_class_feats.append("Elemental Magic")
hero_class_feats.append("Elemental Specialty")
hero_class_feats.append("Escalating Elements")

# Hero Skills
hero_skills1 = {
        "Acrobatics" : 19,
        "Arcana" : 18,
        "Athletics" : 16,
        "Bluff": 7,
        "Diplomacy" : 9,
        "Dungeoneering" : 1,
        "Endurance" : 0,
        "Heal" : 0,
        "History" : 0
        }

hero_skills2 = {
        "Insight" : 19,
        "Intimidate" : 9,
        "Nature" : 0,
        "Perception" : 0,
        "Religion" : 20,
        "Stealth" : 2,
        "Streetwise" : 1,
        "Thievery" : 0        
        }

# Hero Rolls and Ability Scores
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

# Hero Defenses
hero_defense = {
        "AC"   : 12,
        "FORT" : 13,
        "REF"  : 13,
        "WILL" : 14
        }

# Hero Hit Points/Surges
hero_hitpoints = {
        "maxhp" : 60,
        "bloodied" : 30,
        "surgeval" : 15,
        "surgenum" : 10
        }

def dndgi():
    win = GraphWin("DND Character Creation", 600, 650)
    win.setCoords(0, 0, 50, 50)

    # Title
    Text(Point(25, 48.5), "DUNGEONS & DRAGONS").draw(win)

    # Top Section Box
    topbox = Rectangle(Point(1, 41), Point(49, 47))
    topbox.setFill("white")
    topbox.draw(win)

    # Middle Section Box
    midbox = Rectangle(Point(1, 25), Point(49, 40))
    midbox.setFill("white")
    midbox.draw(win)

    # Bottom Box
    botbox = Rectangle(Point(1, 2), Point(49, 24))
    botbox.setFill("white")
    botbox.draw(win)

    # Character Name
    Text(Point(8.8, 46), "Character Name:").draw(win)
    Text(Point(19, 46), hero_name["name"]).draw(win)

    # Level
    Text(Point(32, 46), "Level:").draw(win)
    Text(Point(38, 46), hero_level["level"]).draw(win)

    # Alignment
    Text(Point(30.5, 44), "Alignment:").draw(win)
    Text(Point(40, 44), hero_alnmt["alnmt"]).draw(win)

    # Class
    Text(Point(11.8, 44), "Class:").draw(win)
    Text(Point(19, 44), hero_class["class"]).draw(win)

    # Race
    Text(Point(11.8, 42), "Race:").draw(win)
    Text(Point(19, 42), hero_race["race"]).draw(win)

    # Gender
    Text(Point(31.5, 42), "Gender:").draw(win)
    Text(Point(38, 42), hero_gender["gender"]).draw(win)

    # Ability Scores
    Text(Point(10, 39), "Ability Scores").draw(win)

    Text(Point(7, 37), "Strength:").draw(win)
    Text(Point(6.8, 35), "Dexterity:").draw(win)
    Text(Point(5.9, 33), "Constitution:").draw(win)
    Text(Point(6.1, 31), "Intelligence:").draw(win)
    Text(Point(6.9, 29), "Wisdom:").draw(win)
    Text(Point(6.5, 27), "Charisma:").draw(win)
    
    i = -2
    for x in hero_ab_scores:
        i += 2
        Text(Point(12, 37 - i),hero_ab_scores[x]).draw(win)
        
    # Ability Modifiers
    Text(Point(21, 39), "Ability Modifiers").draw(win)
    
    i = -2
    for x in hero_ab_mods:
        i += 2
        Text(Point(21, 37 - i), "+ %s" % hero_ab_mods[x]).draw(win)

    # Hero Defenses
    Text(Point(30.5, 39), "Defenses").draw(win)

    Text(Point(29, 37), "AC:").draw(win)
    Text(Point(28.15, 35), "FORT:").draw(win)
    Text(Point(28.5, 33), "REF:").draw(win)
    Text(Point(28.26, 31), "WILL:").draw(win)
    i = -2
    for x in hero_defense:
        i += 2
        Text(Point(32, 37 - i), hero_defense[x]).draw(win)
        
    # Hero Hit Points
    Text(Point(43, 39), "Hit Points").draw(win)

    Text(Point(41, 37), "Max HP:").draw(win)
    Text(Point(40.6, 35), "Bloodied:").draw(win)
    Text(Point(39.65, 33), "Surge Value:").draw(win)
    Text(Point(39.7, 31), "Surges/Day:").draw(win)

    i = -2
    for x in hero_hitpoints:
        i += 2
        Text(Point(45, 37 - i), hero_hitpoints[x]).draw(win)

    # Skills
    Text(Point(15, 23), "Skills").draw(win)

    # Left Side Skills
    Text(Point(8.75, 20), "Acrobatics:").draw(win)
    Text(Point(9.8, 18), "Arcana:").draw(win)
    Text(Point(9.25, 16), "Athletics:").draw(win)
    Text(Point(10.50, 14), "Bluff:").draw(win)
    Text(Point(8.75, 12), "Diplomacy:").draw(win)
    Text(Point(7.25, 10), "Dungeoneering:").draw(win)
    Text(Point(8.5, 8), "Endurance:").draw(win)
    Text(Point(10.25, 6), "Heal:").draw(win)
    Text(Point(9.5, 4), "History:").draw(win)

    i = -2
    for x in hero_skills1:
        i += 2
        Text(Point(14, 20 - i), hero_skills1[x]).draw(win)


    # Right Side Skills
    Text(Point(20.5, 20), "Insight:").draw(win)
    Text(Point(19.5, 18), "Intimidate:").draw(win)
    Text(Point(20.4, 16), "Nature:").draw(win)
    Text(Point(19.1, 14), "Perception:").draw(win)
    Text(Point(19.90, 12), "Religion:").draw(win)
    Text(Point(20.2, 10), "Stealth:").draw(win)
    Text(Point(19.2, 8), "Streetwise:").draw(win)
    Text(Point(19.8, 6), "Thievery:").draw(win)

    i = -2
    for x in hero_skills2:
        i += 2
        Text(Point(24, 20 - i), hero_skills2[x]).draw(win)

    # Race Features
    Text(Point(38, 23), "Racial Features").draw(win)


    i = -2
    for x in hero_race_feats:
        i += 2
        Text(Point(38, 20 - i), x).draw(win)

    # Access Second Window
    win.getMouse()

    # Second Window
    win1 = GraphWin("DND Character Creation", 600, 650)
    win1.setCoords(0, 0, 50, 50)

    # Title
    Text(Point(25, 48.5), "DUNGEONS & DRAGONS").draw(win1)

    # Top Section Box
    topbox = Rectangle(Point(1, 30), Point(49, 47))
    topbox.setFill("white")
    topbox.draw(win1)
    
    # Features
    Text(Point(10, 45), "Feats").draw(win1)

    i = -2
    for x in hero_class_feats:
        i += 2
        Text(Point(10, 42 - i), x).draw(win1)

    # Languages
    Text(Point(25, 45), "Languages").draw(win1)

    i = -2
    for x in hero_language:
        i += 2
        Text(Point(25, 42 - i), x).draw(win1)


    # Vision
    Text(Point(40, 45), "Vision").draw(win1)
    Text(Point(40, 42), hero_race["vision"]).draw(win1)

    win1.getMouse()

dndgi()
        
