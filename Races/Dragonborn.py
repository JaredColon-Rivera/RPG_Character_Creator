# Dragonborn Race

dragonborn_fury = "When you're bloodied, you gain a +1 bonus to attack rolls."
draconic_heritage = "Your healing surge value is equal to one-quarter \nof your maximum hit points + your Constitution modifier."
dragon_breath_descr = "You can use 'dragon breath' as an encounter power."

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

# Dragonborn Description
def dragonborn_descr():
    print("Dragonborn. Born to fight, they are the race of \nwandering mercenaries, soldiers, and adventurers.\n")
    print("Play a dragonborn if you want...")
    print("> a race that favors the warlord, fighter, and paladin classes")
    print("> to look like a dragon")
    print("> to be the proud heir of an ancient, fallen empire")
    print("> to breathe acid, cold, fire, lightning, or poison\n")
    print("The Dragonborn have the following stats:")
    print("> Strength  : +2")
    print("> Charisma  : +2")
    print("> Speed : 6 squares")
    print("> Vision    : Normal Vision")
    print("> Languages : Common, Draconic")
    print("> History   : +2")
    print("> Intimidate: +2\n")
    print("The Dragonborn have the following racial features:")
    print("> Dragonborn Fury: %s" % dragonborn_fury)
    print("> Draconic Heritage: %s" % draconic_heritage)
    print("> Dragon Breath: %s" % dragon_breath_descr)

dragonborn_descr()

# Dragonborn Initial Stats/Skills/Feats
def dragonborn_initial():
    hero_race["race"] = "Dragonborn"
    hero_race["speed"] = 6
    hero_race["feats"].append("Normal Vision")
    hero_race["languages"].append("Common")
    hero_race["languages"].append("Draconic")
    hero_race["feats"].append("Dragonborn Fury")
    hero_race["feats"].append("Draconic Heritage")
    hero_race["feats"].append("Dragon Breath")
    hero_ab_scores["Strength"] += 2
    hero_ab_scores["Charisma"] += 2
    hero_skills["History"] += 2
    hero_skills["Intimidate"] +=2
    
dragonborn_initial()