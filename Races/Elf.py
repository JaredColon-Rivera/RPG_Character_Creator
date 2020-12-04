# Elf Race

elven_weapon_prof = "You gain proficiency with the longbow and the shortbow"
fey_origin = "Your ancestors were native to the Feywild, so you are considered a fey creature"
group_awareness = "You grant non-elf allies within 5 squares of you a +1 bonus to Perception checks"
wild_step = "You ignore difficult terrain when you shift (even if you have a power that allows you to shift multiple squares)"
elven_accuracy = "You can use elven accuracy as an encounter power"

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

#--------------Race Description--------------#
def race_descr(
        racedescr, 
        race, 
        ifyouwant1, ifyouwant2, ifyouwant3, ifyouwant4, 
        stat1, stat2, 
        speed,
        vision, 
        language1, language2, 
        skill1, skill2, 
        racefeat1, racefeat2, racefeat3, racefeat4, racefeat5, racefeat6,
        racefeatdescr1, racefeatdescr2, racefeatdescr3, racefeatdescr4, racefeatdescr5, racefeatdescr6)

	print("%s\n" % racedescr)
    print("Play a %s if you want..." % race)
    print("> %s" % ifyouwant1)
    print("> %s" % ifyouwant2)
    print("> %s" % ifyouwant3)
    print("> %s\n" % ifyouwant4)
    print("The %s have the following stats:" % race)
    print("> %s : +2" % stat1)
    print("> %s : +2" % stat2)
    print("> Speed : %s squares" % speed)
    print("> Vision    : %s" % vision)
    print("> Languages : %s, %s" % (language1, language2))
    print("> %s   : +2" % skill1)
    print("> %s   : +2\n" % skill2)
    print("The %s have the following racial features:" % race)
    print("> %s: %s" % racefeat1, racefeatdescr1)
    print("> %s: %s" % racefeat2, racefeatdescr2)
    print("> %s: %s" % racefeat3, racefeatdescr3)
    print("> %s: %s" % racefeat4, racefeatdescr4)
    print("> %s: %s" % racefeat5, racefeatdescr5)
    print("> %s: %s\n" % racefeat6, racefeatdescr6)

    #---------------Race Choice---------------#
    choice = input("Would you like to be a %s?: " % race)
    choice = choice.lower()
    if choice == "yes":
        print("You are a %s!" % race)

        #---------------Race Stats/Skills/Feats---------------#
        hero_race["race"] = race
        hero_ab_scores[stat1] += 2
        hero_ab_scores[stat2] += 2
        hero_race["speed"] = speed
        hero_race["feats"].append(vision)
        hero["language"].append(language1)
        hero["language"].append(language2)
        hero_skills[skill1] += 2
        hero_skills[skill2] +=2
        hero_race["feats"].append(racefeat1)
        hero_race["feats"].append(racefeat2)
        hero_race["feats"].append(racefeat3)
        hero_race["feats"].append(racefeat4)
        hero_race["feats"].append(racefeat5)
        hero_race["feats"].append(racefeat6)

    elif choice == "no":
        print("Sounds good. Take your time.\n")
        race_choice()
    else:
        print("Unknown input.\n")
        race_choice()

# Elf Race
race_descr("Elves. Tall, long-lived, aloof, and connected to nature. Elves live in \nharmony with the natural world around them.",
			"Elf",
			"a race that favors the ranger, rogue, and cleric classes", "to be quick, quiet, and wild", "to lead your companions through the deep woods and pepper your enemies with arrows", "if you want4",
			"Dexterity", "Wisdom",
			7,
			"Low-Light",
			"Common", "Elven",
			"Nature", "Perception",
			"Elven Weapon Proficiency", "Fey Origin", "Group Awareness", "Wild Step", "Elven Accuracy",
			elven_weapon_prof, fey_origin, group_awareness, wild_step, elven_accuracy)