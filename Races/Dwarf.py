# Dwarf Race

castiron_stomach = "+5 bonus to saving throws against poison"
dwarven_resilience = "You can use your second wind as a minor action instead of a standard action"
dwarven_weapon_prof = "You gain proficiency with the throwing hammer and the warhammer"
encumbered_speed = "You move at your normal speed even when it would normally be reduced by armor \nor a heavy load. (Difficult terrain or magical effects affect you normally)"
stand_your_ground = "When an effect forces you to move—through a pull, a push, or a slide—you can \nmove 1 square less than the effect specifies. \nIn addition, when an attack would knock you prone, \nyou can immediately make a saving throw to avoid falling prone."

# Hero Race
hero_race = {
        "race" : 0,
        "speed" : 0,
        "languages" : [],
        "feats" : []
        }

# Hero Ability Scores
hero_ab_scores = {
            "Strength" : 0,
            "Dexterity" : 0,
            "Constitution" : 0,
            "Intelligence" : 0,
            "Wisdom" : 0,
            "Charisma" : 0
            }

# Hero Skills
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
        "Insight" : 0,
        "Intimidate" : 0,
        "Nature" : 0,
        "Perception" : 0,
        "Religion" : 0,
        "Stealth" : 0,
        "Streetwise" : 0,
        "Thievery" : 0        
        }

# Dwarf Description
def dwarf_descr():
    print("Dwarves. Short, stocky, stern, and strong. They have a connection to \nthe earth and often live in mountains or underground lands.")
    print("Play a Dwarf if you want...")
    print("> a race that favors the paladin, cleric, and fighter classes")
    print("> to be tough, gruff, and strong as bedrock")
    print("> to bring glory to your ancestors or serve as your god's right hand")
    print("> to be able to take as much punishment as you dish out\n")
    print("The Dwarves have the following stats:")
    print("> Constitution : +2")
    print("> Wisdom : +2")
    print("> Speed : 5 squares")
    print("> Vision    : Low-Light")
    print("> Languages : Common, Dwarven")
    print("> Dungeoneering   : +2")
    print("> Endurance       : +2\n")
    print("The Dwarves have the following racial features:")
    print("> Cast-Iron Stomach: %s" % castiron_stomach)
    print("> Dwarven Resilience: %s" % dwarven_resilience)
    print("> Dwarven Weapon Proficiency: %s" % dwarven_weapon_prof)
    print("> Encumbered Speed: %s" % encumbered_speed)
    print("> Stand Your Ground: %s" % stand_your_ground)
    
dwarf_descr()

# Dwarf Initial Stats/Skills/Feats
def dwarf_initial():
	hero_race["race"] = "Dwarf"
    hero_race["speed"] = 5
    hero_race["feats"].append("Low-Light Vision")
    hero_race["languages"].append("Common")
    hero_race["languages"].append("Dwarven")
    hero_race["feats"].append("Cast-Iron Stomach")
    hero_race["feats"].append("Dwarven Resilience")
    hero_race["feats"].append("Dwarven Weapon Proficiency")
    hero_race["feats"].append("Encumbered Speed")
    hero_race["feats"].append("Stand Your Ground")
    hero_ab_scores["Constitution"] += 2
    hero_ab_scores["Wisdom"] += 2
    hero_skills["Dungeoneering"] += 2
    hero_skills["Endurance"] +=2


dwarf_initial()