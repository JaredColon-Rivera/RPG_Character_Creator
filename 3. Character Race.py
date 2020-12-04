# Hero Race

hero_ab_scores = {
            "Strength" : 0,
            "Dexterity" : 0,
            "Constitution" : 0,
            "Intelligence" : 0,
            "Wisdom" : 0,
            "Charisma" : 0,
            }

hero_race = {
        "race" : 0,
        "speed" : 0,
        "languages" : [],
        "feats" : []
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
        "Thievery" : 0,  
        }

races = [
        "Dragonborn",
        "Dwarves",
        "Eladrin",
        "Elves",
        "Half-elves",
        "Halflings",
        "Humans",
        "Tieflings"
        ]

# Updated Character Race

#---------------Dragonborn Features---------------#
dragonborn_fury = "When you're bloodied, you gain a +1 bonus to attack rolls."
draconic_heritage = "Your healing surge value is equal to one-quarter \nof your maximum hit points + your Constitution modifier."
dragon_breath_descr = "You can use 'dragon breath' as an encounter power."

#--------------Dwarven Features---------------#
castiron_stomach = "+5 bonus to saving throws against poison"
dwarven_resilience = "You can use your second wind as a minor action instead of a standard action"
dwarven_weapon_prof = "You gain proficiency with the throwing hammer and the warhammer"
encumbered_speed = "You move at your normal speed even when it would normally be reduced by armor \nor a heavy load. (Difficult terrain or magical effects affect you normally)"
stand_your_ground = "When an effect forces you to move—through a pull, a push, or a slide—you can \nmove 1 square less than the effect specifies. \nIn addition, when an attack would knock you prone, \nyou can immediately make a saving throw to avoid falling prone."

#---------------Eladrin Features---------------#
eladrin_education = "You gain training in one additional skill (any skill, not just Class Skills)"
eladrin_weapon_prof = "You gain proficiency with the longsword"
eladrin_will = "You gain a +1 racial bonus to your Will defense. In addition, you gain a +5 racial \nbonus to saving throws against charm effects"
fey_origin = "Your ancestors were native to the Feywild, so you are considered a fey creature"
trance = "Rather than sleep, eladrin enter a meditative state known as trance. You need to spend 4 \nhours in this state to gain the same benefits other races gain from taking \na 6-hour extended rest. While in a trance, you are fully aware of your surroundings \nand notice approaching enemies and other events as normal."
fey_step = "You can use 'fey step' as an encounter power"

#---------------Elven Features---------------#
elven_weapon_prof = "You gain proficiency with the longbow and the shortbow"
fey_origin = "Your ancestors were native to the Feywild, so you are considered a fey creature"
group_awareness = "You grant non-elf allies within 5 squares of you a +1 bonus to Perception checks"
wild_step = "You ignore difficult terrain when you shift (even if you have a power that allows you to shift multiple squares)"
elven_accuracy = "You can use elven accuracy as an encounter power"

#---------------Half-Elf Features---------------#
dual_heritage = "You can take feats that have either elf or human as a prerequesite (as well as those \nspecifically for half-elves) as long as you meet any other requirements"
group_diplomacy = "You grant allies within 10 squares of you a +1 bonus to Diplomacy checks"
dilettante = "At 1st level, you choose a 1st-level at-will attack power from a class different from yours. \nYou can use that power as an encounter power"

#---------------Halfling Features---------------#
bold = "You gain a +5 bonus to saving throws against fear"
nimble_reaction = "You gain a +2 bonus to AC against opportunity attacks"
second_chance = "You can use second chance as an encounter power"

#---------------Human Features---------------#
bonus_atwill_power = "You know on extra at-will power from your class"
bonus_feat = "You gain a bonus feat at 1st level. You must meet the feats prerequesite"
bonus_skill = "You gain training in one additional skill from your class skill list"
human_def_bonuses = "+1 to Fortitude, Reflex, and Will defenses"

#---------------Tiefling Features---------------#
bloodhunt = "You gain +1 bonus to attack rolls against bloodied foes"
fire_res = "You have resist fire 5 + one-half your level"
infernal_wrath = "You can use infernal wrath as an encounter power"

#--------------Race Description--------------#
def race_descr(
        racedescr, 
        race, 
        ifyouwant1, ifyouwant2, ifyouwant3, ifyouwant4, 
        stat1, stat2, 
        speed,
        vision, 
        language1, language2, language3,
        skill1, skill2, 
        racefeat1, racefeat2, racefeat3, racefeat4, racefeat5, racefeat6,
        racefeatdescr1, racefeatdescr2, racefeatdescr3, racefeatdescr4, racefeatdescr5, racefeatdescr6):

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
    print("> Languages : %s, %s, %s" % (language1, language2, language3))
    print("> %s   : +2" % skill1)
    print("> %s   : +2\n" % skill2)
    print("The %s have the following racial features:" % race)
    print("> %s: %s" % (racefeat1, racefeatdescr1))
    print("> %s: %s" % (racefeat2, racefeatdescr2))
    print("> %s: %s" % (racefeat3, racefeatdescr3))
    print("> %s: %s" % (racefeat4, racefeatdescr4))
    print("> %s: %s" % (racefeat5, racefeatdescr5))
    print("> %s: %s\n" % (racefeat6, racefeatdescr6))

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
        hero_race["languages"].append(language1)
        hero_race["languages"].append(language2)
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

def race_description(racepick):
    if racepick == "Dragonborn":
        #---------------Dragonborn Race---------------#
        race_descr(
                "Dragonborn. Born to fight, they are the race of \nwandering mercenaries, soldiers, and adventurers.",
                "Dragonborn", 
                "a race that favors the warlord, fighter, and paladin classes", "to look like a dragon", "to be the proud heir of an ancient, fallen empire", "to breathe acid, cold, fire, lightning, or poison", 
                "Strength", "Charisma", 
                6,
                "Normal Vision", 
                "Common", "Draconic", " ",
                "History", "Intimidate", 
                "Dragonborn Fury", "Draconic Heritage", "Dragon Breath", " ", " ", " ",
                dragonborn_fury, draconic_heritage, dragon_breath_descr, " ", " ", " ")

    elif racepick == "Dwarves":
        #---------------Dwarven Race---------------#
        race_descr(
                "Dwarves. Short, stocky, stern, and strong. They have a connection to \nthe earth and often live in mountains or underground lands.", 
                "Dwarf", 
                "a race that favors the paladin, cleric, and fighter classes", "to be tough, gruff, and strong as bedrock", "to bring glory to your ancestors or serve as your god's right hand", "to be able to take as much punishment as you dish out", 
                "Constitution", "Wisdom", 
                5,
                "Low-Light", 
                "Common", "Dwarven", " ",
                "Dungeoneering", "Endurance", 
                "Cast-Iron Stomach", "Dwarven Resilience", "Dwarven Weapon Proficiency", "Encumbered Speed", "Stand Your Ground", " ",
                castiron_stomach, dwarven_resilience, dwarven_weapon_prof, encumbered_speed, stand_your_ground, " ")

    elif racepick == "Eladrin":
        #---------------Eladrin Race---------------#
        race_descr(
                "Eladrin. Creatures of magic with strong ties to nature. They live \nin cities in the twilight realm of the Feywild.",
                "Eladrin", 
                "a race that favors the wizard, rogue, and warlord classes", "to be otherwordly and mysterious", "to be graceful and intelligent", "to teleport around the battlefield, cloaked in the magic of the Feywild", 
                "Intelligence", "Dexterity", 
                6,
                "Low-Light", 
                "Common", "Elven", " ",
                "Arcana", "History", 
                "Eladrin Education", "Eladrin Weapon Proficiency", "Eladrin Will", "Fey Origin", "Trance", "Fey Step",
                eladrin_education, eladrin_weapon_prof, eladrin_will, fey_origin, trance, fey_step)

    elif racepick == "Elves":
        #---------------Elf Race---------------#
        race_descr(
                "Elves. Tall, long-lived, aloof, and connected to nature. Elves live in \nharmony with the natural world around them.",
                "Elf",
                "a race that favors the ranger, rogue, and cleric classes", "to be quick, quiet, and wild", "to lead your companions through the deep woods and pepper your enemies with arrows", " ",
                "Dexterity", "Wisdom",
                7,
                "Low-Light",
                "Common", "Elven", " ",
                "Nature", "Perception",
                "Elven Weapon Proficiency", "Fey Origin", "Group Awareness", "Wild Step", "Elven Accuracy", " ",
                elven_weapon_prof, fey_origin, group_awareness, wild_step, elven_accuracy, " ")

    elif racepick == "Half-elves":
        #---------------Half-Elf Race---------------#
        race_descr(
                "Half-elves. Descended from elves and humans, they are a vital race in which \nthe best features of elves and humans often appear.",
                "Half-Elf",
                "a race that favors the warlord, paladin, and warlock classes", "to be an outgoing, enthusiastic leader", "to be a charismatic hero equally at home in two different cultures", " ",
                "Constitution", "Charisma",
                6,
                "Low-Light",
                "Common", "Elven", "Choice of one other",
                "Diplomacy", "Insight",
                "Dilettante", "Dual Heritage", "Group Diplomacy", " ", " ", " ",
                dilettante, dual_heritage, group_diplomacy, " ", " ", " ")

    elif racepick == "Halflings":
        #---------------Halfling Race---------------#
        race_descr(
                "Halflings. A small race known for their resourcefulness, quick wits, and steady nerves.",
                "Halfling",
                "a race that favors the rogue, ranger, and warlock classes", "to be a plucky hero who is all too easy to underestimate", "to be likable, warm, and friendly",
                "Dexterity", "Charisma",
                6,
                "Normal Vision",
                "Common", "Choice of one other", " ",
                "Acrobatics", "Thievery",
                "Bold", "Nimble Reaction", "Second Chance", " ", " ", " ",
                bold, nimble_reaction, second_chance, " ", " ", " ")

    elif racepick == "Humans":
        #---------------Human Race---------------#
        race_descr(
                "Humans. Of all the civilized races, humans are th emost adaptable and diverse. \nHuman settlements can be found almost anywhere, and human morals, customs, and interests vary greatly.",
                "Human",
                "to be able to excel at any class you choose", "to be decisive, resourceful hero with enough determination to face any challenge", "to have the most versatility and flexibility of any race", 
                "Choose one ability score of your choice and gain", " ",
                6,
                "Normal Vision",
                "Common", "Choice of one other", " ",
                " ", " ",
                "Bonus At-Will Power", "Bonus Feat", "Bonus Skill", "Human Defense Bonuses", " ", " ",
                bonus_atwill_power, bonus_feat, bonus_skill, human_def_bonuses, " ", " ")
        
    elif racepick == "Tieflings":
        #---------------Tiefling Race---------------#
        race_descr(
                "Tieflings. Heirs to an ancient, infernal bloodline, tieflings have no realms of their \nown but instead live within human kingdoms and cities. They are descended from human nobles \nwho bargained wiht dark powers, and long ago their empire subjugated half the world.",
                "Tiefling",
                "a race that favors the warlock, warlord, and rogue classes", "to be a hero who has a dark side to overcome", "to be good at tricking, intimidating, or persuading others to do your will",
                "Intelligence", "Charisma",
                6, 
                "Low-Light",
                "Common", "Choice of one other", " ",
                "Bluff", "Stealth",
                "Bloodhunt", "Fire Resistance", "Infernal Wrath", " ", " ", " ",
                bloodhunt, fire_res, infernal_wrath, " ", " ", " ")

#---------------Race Choice Initial---------------#
def race_choice():
    print("\nNow, you will pick a race.\n")
    print("Below are the races that you can choose from:")
    for x in races:
        print("> %s" % x)
    racepick = input("\nWhich race would you like to learn about?: ")
    racepick = racepick.title()

     #---------------Race Descriptions---------------#
    if racepick in races:
        race_description(racepick)
    else:
        print("Unknown input. Please type in the races as they are written.")
        race_choice()

    #---------------Increasing Ability Scores--------------#
    def ab_score_increase(x):
        print("You increased %s by +2." % x)
        hero_ab_scores[x] += 2
    
    #---------------Choosing Ability Scores---------------#
    def ab_score_pick(x):
        for x in hero_ab_scores:
            print("> %s" % x)
        choice = input("Which stat would you like to add +2?: ")
        choice = choice.title()
        if choice in hero_ab_scores:
           ab_score_increase(choice)
        else:
            print("Unknown input.")
            print("Please type in an ability score to increase.\n")
            ab_score_pick(x)

race_choice()