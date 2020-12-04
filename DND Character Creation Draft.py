# DND Character Creation

import random
from graphics import *

# Racial Features

#Dragonborn
dragonborn_fury = "When you're bloodied, you gain a +1 bonus to attack rolls."
draconic_heritage = "Your healing surge value is equal to one-quarter \nof your maximum hit points + your Constitution modifier."
dragon_breath = "You can use 'dragon breath' as an encounter power."

# Hero Level
hero_level = {
        "level" : 1
        }

# Hero Name
hero_name = {
        "name" : 0
        }
# Hero Gender
hero_gender = {
        "gender" : 0
        }
# Hero Alignment
hero_alnmt = {
        "alnmt" : 0
        }

alignments = ["Lawful Good",
              "Neutral Good",
              "Chaotic Good",
              "Lawful Neutral",
              "True Neutral",
              "Chaotic Neutral",
              "Lawful Evil",
              "Neutral Evil",
              "Chaotic Evil"
              ]

# Hero Hitpoints
hero_hitpoints = {
        "maxhp" : 0,
        "bloodied" : 0,
        "surgeval" : 0,
        "surgenum" : 0
        }

# Hero Defenses
hero_defense = {
        "AC"   : 0,
        "FORT" : 0,
        "REF"  : 0,
        "WILL" : 0
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

# Hero Race
hero_race = {
        "race" : 0,
        "speed": 0,
        "languages" : [],
        "feats" : []
        }

races = [
        "Dragonborn",
        "Dwarves",
        "Eladrin",
        "Elves",
        "Gnomes",
        "Half-elves",
        "Half-orcs",
        "Halflings",
        "Humans",
        "Tiefling"
        ]

# Hero Class
hero_class = {
        "class" : 0,
        "initial_hp" : 0,
        "initial_surge" : 0,
        "feats" : []
        }

classes = [
        "Barbarian",
        "Bard",
        "Cleric",
        "Druid",
        "Fighter",
        "Monk",
        "Paladin",
        "Ranger",
        "Rogue",
        "Sorcerer",
        "Warlock",
        "Warlord",
        "Wizard"
        ]

# Hero Rolls and Ability Scores
initial_rolls = {
            "1" : 0,
            "2" : 0,
            "3" : 0,
            "4" : 0,
            "5" : 0,
            "6" : 0
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

# Hero Ability Modifiers
hero_ab_mods = {
        "Strength"     : 0,
        "Dexterity"    : 0,
        "Constitution" : 0,
        "Intelligence" : 0,
        "Wisdom"       : 0,
        "Charisma"     : 0
        }

# 1. Hero Name
def name():
    print("")
    print("Hello there adventurer! Before we start our journey,")
    print("you will have to create a name. ")
    def hname():
        print("")
        hero_name["name"] = input("What would you like to be called?: ")
        if len(hero_name["name"]) > 10:
            print ("Sorry, only 10 characters allowed.")
            hname()
        else:
            nameconfirm = input("Are you sure you want your name to be %s?: " % hero_name["name"])
            nameconfirm = nameconfirm.lower()
            if nameconfirm == "yes":
                print("")
                print("Glad to meet you %s! Now let's create your character." % hero_name["name"])
            elif nameconfirm == "no":
                print("")
                print("Sounds good. Take your time.")
                hname()
            else:
                print("")
                print("Unknown input. Please type in a name.")
                hname()
    hname()

name()

# Hero Gender
def gender():
    print("")
    print("> Male")
    print("> Female")
    print("> Other")
    genderch = input("What is your gender?: ")
    genderch = genderch.title()
    hero_gender["gender"] = genderch
    if genderch == "Male":
        print("")
    elif genderch == "Female":
        print("")
    elif genderch == "Other":
        print("")
    else:
        print("Unknown input.")
        gender()
    
gender()

print("Your gender is %s." % hero_gender["gender"])

# 2. Hero Alignment
def alignment():
    print("")
    print("Your hero will have a specific alignment.")
    print("")
    for x in alignments:
        print("> %s" % x)
    def algn():
        print("")
        alnmt = input("What is your alignment?: ")
        alnmt = alnmt.title()
        hero_alnmt["alnmt"] = alnmt

        if alnmt == "Lawful Good":
            print("")
        elif alnmt == "Neutral Good":
            print("")
        elif alnmt == "Chaotic Good":
            print("")
        elif alnmt == "Lawful Neutral":
            print("")
        elif alnmt == "True Neutral":
            print("")
        elif alnmt == "Chaotic Neutral":
            print("")
        elif alnmt == "Lawful Evil":
            print("")
        elif alnmt == "Neutral Evil":
            print("")
        elif alnmt == "Chaotic Evil":
            print("")
        else:
            print("Unknown input. Please enter an alignment as they are written.")
            algn()
    
    algn()

    print("Your alignment is %s." % hero_alnmt["alnmt"])
    
alignment()

# 3. Hero Race
def race_choice():
    print("")
    print("Now, you will pick a race.")
    print("")
    print("Below are the races that you can choose from:")
    for x in races:
        print("> %s" % x)
    print("")
    racepick = input("Which race would you like to learn about?: ")
    racepick = racepick.lower()
    print("")

    # Dragonborn Description and Initial Stats/Features
    def dragonborn_descr():
        print("Dragonborn. Born to fight, they are the race of \nwandering mercenaries, soldiers, and adventurers.\n")
        print("")
        print("Play a dragonborn if you want...")
        print("> a race that favors the warlord, fighter, and paladin classes")
        print("> to look like a dragon")
        print("> to be the proud heir of an ancient, fallen empire")
        print("> to breathe acid, cold, fire, lightning, or poison\n")
        print("The Dragonborn have the following stats:")
        print("> Strength  : +2")
        print("> Charisma  : +2")
        print("> Vision    : Normal Vision")
        print("> Languages : Common, Draconic")
        print("> History   : +2")
        print("> Intimidate: +2\n")
        print("The Dragonborn have the following features:")
        print("> Dragonborn Fury: %s" % dragonborn_fury)
        print("> Draconic Heritage: %s" % draconic_heritage)
        print("> Dragon Breath: %s" % dragon_breath)

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
        

    # Increasing Ability Scores
    def ab_score_increase(x):
        print("You increased %s by +2." % x)
        hero_ab_scores[x] += 2
    
    # Choosing Ability Scores
    def ab_score_pick(x):
        for x in hero_ab_scores:
            print("> %s" % x)
        print("")
        choice = input("Which stat would you like to add +2?: ")
        choice = choice.title()
        if choice == "Strength":
            ab_score_increase(choice)
        elif choice == "Dexterity":
            ab_score_increase(choice)
        elif choice == "Constitution":
            ab_score_increase(choice)
        elif choice == "Intelligence": 
            ab_score_increase(choice)
        elif choice == "Wisdom":
            ab_score_increase(choice)
        elif choice == "Charisma":                       
            ab_score_increase(choice)
        else:
            print("Unknown input.")
            print("Please type in an ability score to increase.")
            print("")
            ab_score_pick(x)


    # Dragonborn
    if racepick == "dragonborn":
        def dragonborn():
            dragonborn_descr()
            dbchoice = input("Would you like to be a Dragonborn?: ")
            dbchoice = dbchoice.lower()
            if dbchoice == "yes":
                print("You are a Dragonborn!")
                dragonborn_initial()
            elif dbchoice == "no":
                print("Sounds good. Take your time.")
                print("")
                race_choice()
            else:
                print("Unknown input. Please type in 'yes' or 'no'.")
                print("")
                dragonborn()

        dragonborn()
        
        
    # Dwarf
    elif racepick == "dwarves":
        def dwarf():
            print("")
            print("Dwarves. Short, stocky, stern, and strong. They have a connection to")
            print("the earth and often live in mountains or underground lands.")
            print("")
            print("The Dwarves have the following stat modifiers:")
            print("Constitution : +2")
            print("Wisdom       : +2")
            dchoice = input("Would you like to be a Dwarf?: ")
            dchoice = dchoice.lower()
            if dchoice == "yes":
                print("You are a Dwarf!")
                hero_ab_scores["Constitution"] += 2
                hero_ab_scores["Wisdom"] += 2
                hero_race["race"] = "Dwarf"
            elif dchoice == "no":
                print("Sounds good. Take your time.")
                print("")
                race_choice()
            else:
                print("Unknown input. Please type in 'yes' or 'no'.")
                print("")
                dwarf()
        dwarf()

    # Eladrin
    elif racepick == "eladrin":
        def eladrin():
            print("Eladrin. Creatures of magic with strong ties to nature. They live")
            print("in cities in the twilight realm of the Feywild.")
            print("")
            print("The Eladrin have the following stat modifiers:")
            print("Dexterity    : +2")
            print("Intelligence : +2")
            elchoice = input("Would you like to be an Eladrin?: ")
            elchoice = elchoice.lower()
            if elchoice == "yes":
                print("You are an Eladrin!")
                hero_ab_scores["Dexterity"] += 2
                hero_ab_scores["Intelligence"] += 2
                hero_race["race"] = "Eladrin"
            elif elchoice == "no":
                print("Sounds good. Take your time.")
                print("")
                race_choice()
            else:
                print("Unknown input. Please type in 'yes' or 'no'.")
                print("")
                eladrin()
        eladrin()
        
    # Elf
    elif racepick == "elves":
        def elf():
            print("Elves. Wild and free. Elves guard their forested lands using stealth")
            print("and deadly arrows from the trees.")
            print("")
            print("The Elves have the following stat modifiers:")
            print("Dexterity : +2")
            print("Wisdom    : +2")
            echoice = input("Would you like to be an Elf?: ")
            echoice = echoice.lower()
            if echoice == "yes":
                print("You are an Elf!")
                hero_ab_scores["Dexterity"] += 2
                hero_ab_scores["Wisdom"] += 2
                hero_race["race"] = "Elf"
            elif echoice == "no":
                print("Sounds good. Take your time.")
                print("")
                race_choice()
            else:
                print("Unknown input. Please type in 'yes' or 'no'.")
                print("")
                elf()
        elf()

    # Gnome
    elif racepick == "gnomes":
        def gnome():
            print("Gnomes. Mysterious, adventure-seeking, and strange.")
            print("Gnomes are the smallest common race.")
            print("")
            print("The Gnomes have the following stat modifiers:")
            print("Constitution: +2")
            print("Charisma: +2")
            print("Strength: -2")
            gchoice = input("Would you like to be a Gnome?: ")
            gchoice = gchoice.lower()
            if gchoice == "yes":
                print("You are a Gnome!")
                hero_ab_scores["Constitution"] += 2
                hero_ab_scores["Charisma"] += 2
                hero_ab_scores["Strength"] -= 2
                hero_race["race"] = "Gnome"
            elif gchoice == "no":
                print("Sounds good. Take your time.")
                print("")
                race_choice()
            else:
                print("Unknown input. Please type in 'yes' or 'no'.")
                print("")
                gnome()
        gnome()
        
    # Half-Elf
    elif racepick == "half-elves":
        def halfelf():
            print("Half-elves. Solitary, long-lived,, graceful and hearty.")
            print("Half-elves are few in number, and tend to be wanderers")
            print("due to their lack of homeland.")
            print("")
            print("The Half-elves have the following stat modifiers:")
            print("Constitution : +2")
            print("Charisma     : +2")
            hechoice = input("Would you like to be a Half-elf?: ")
            hechoice = hechoice.lower()
            if hechoice == "yes":
                print("You are a Half-elf!")
                hero_ab_scores["Constitution"] += 2
                hero_ab_scores["Charisma"] += 2
                hero_race["race"] = "Half-elf"
            elif hechoice == "no":
                print("Sounds good. Take your time.")
                print("")
                race_choice()
            else:
                print("Unknown input. Please type in 'yes' or 'no'.")
                print("")
                halfelf()
        halfelf()


    # Half-Orc
    elif racepick == "half-orcs":
        def halforc():
            print("Half-orcs. Independent, strong and distrusted. Half-orcs are")
            print("considered monstrosities by common folk.")
            print("They are tall and powerfully built.")
            print("")
            print("The Half-orcs can add +2 to any one ability score.")
            hochoice = input("Would you like to be a Half-orc?: ")
            hochoice = hochoice.lower()
            if hochoice == "yes":
                print("You are a Half-orc!")
                print("")
                hero_race["race"] = "Half-orc"
                ab_score_pick(x)
            elif hochoice == "no":
                print("Sounds good. Take your time.")
                print("")
                race_choice()
            else:
                print("Unknown input. Please type in 'yes' or 'no'.")
                print("")
                halforc()
        halforc()

    # Halfling
    elif racepick == "halflings":
        def halfling():
            print("Halflings. Optimistic, cheerful, curious, and small in stature.")
            print("On average, they are only 3 ft. tall. They are agile but physically weak.")
            print("")
            print("The Halflings have the following stat modifiers:")
            print("Dexterity: +2")
            print("Charisma: +2")
            hlchoice = input("Would you like to be a Halfling?: ")
            hlchoice = hlchoice.lower()
            if hlchoice == "yes":
                print("You are a Halfling!")
                print("")
                hero_ab_scores["Dexterity"] += 2
                hero_ab_scores["Charisma"] += 2
                hero_race["race"] = "Halfling"
            elif hlchoice == "no":
                print("Sounds good. Take your time.")
                print("")
                race_choice()
            else:
                print("Unknown input. Please type in 'yes' or 'no'.")
                print("")
                halfling()
        halfling()

    # Human
    elif racepick == "humans":
        def human():
            print("Humans. Adaptive, ambitious and well-balanced.")
            print("Humans are the dominant race, and are diverse in appearance and culture.")
            print("")
            print("The Humans can add +2 to any one ability score.")
            hnchoice = input("Would you like to be a Human?: ")
            hnchoice = hnchoice.lower()
            if hnchoice == "yes":
                print("You are a Human!")
                print("")
                hero_race["race"] = "Human"
                ab_score_pick(x)   
            elif hnchoice == "no":
                print("Sounds good. Take your time.")
                print("")
                race_choice()
            else:
                print("Unknown input. Please type in 'yes' or 'no'.")
                print("")
                human()
        human()


    # Tiefling
    elif racepick == "tiefling":
        def tiefling():
            print("Tieflings. Heirs to an ancient, infernal bloodline. They have")
            print("no realm of their own but instead live within human kingdoms and cities.")
            print("")
            print("The Tieflings have the following stat modifiers:")
            print("Intelligence : +2")
            print("Charimsa     : +2")
            tichoice = input("Would you like to be a Tiefling?: ")
            tichoice = tichoice.lower()
            if tichoice == "yes":
                print("You are a Tiefling!")
                print("")
                hero_ab_scores["Intelligence"] += 2
                hero_ab_scores["Charisma"] += 2
                hero_race["race"] = "Tiefling"
            elif tichoice == "no":
                print("Sounds good. Take your time.")
                print("")
                race_choice()
            else:
                print("Unknown input. Please type in 'yes' or 'no'.")
                print("")
                tiefling()
                
        tiefling()
                
            
    else:
        print("Unknown input. Please type in a race as they are displayed.")
        race_choice()
        
race_choice()


# 4. Hero Class
def hero_classes():
    print("")
    print("Now, you will pick a class.")
    print("")
    print("Here are all the classes to choose from:")
    for x in classes:
        print("> %s" % x)
    def class_choice():
        print("")
        choice = input("Which class would you like to learn about?: ")
        choice = choice.lower()

        # Barbarian
        if choice == "barbarian":
            def barbarian():
                print("")
                print("Barbarians. Brutal berserkers from the edge")
                print("of civilized lands.")
                brbnch = input("Would you like to be a Barbarian?: ")
                brbnch = brbnch.lower()
                if brbnch == "yes":
                    print("You are a Barbarian.")
                    hero_class["class"] = "Barbarian"
                elif brbnch == "no":
                    print("Sounds good. Take your time.")
                    hero_classes()
                else:
                    print("Unknown input. Please enter 'yes' or 'no'.")
                    barbarian()
            barbarian()

        # Bard
        elif choice == "bard":
            def bard():
                print("")
                print("Bards. They use skills and spells alike to bolster their allies,")
                print("confound their enemies, and build upon their fame.")
                bardch = input("Would you like to be a Bard?: ")
                bardch = bardch.lower()
                if bardch == "yes":
                    print("You are a Bard.")
                    hero_class["class"] = "Bard"
                elif bardch == "no":
                    print("Sounds good. Take your time.")
                    hero_classes()
                else:
                    print("Unknown input. Please enter 'yes' or 'no'.")
                    bard()
            bard()
            
        # Cleric
        elif choice == "cleric":
            def cleric():
                print("")
                print("Clerics. Devout followers of a deity, Clerics can heal wounds,")
                print("raise the dead, and call down the wrath of the gods.")
                clrcch = input("Would you like to be a Cleric?: ")
                clrcch = clrcch.lower()
                if clrcch == "yes":
                    print("You are a Cleric.")
                    hero_class["class"] = "Cleric"
                elif clrcch == "no":
                    print("Sounds good. Take your time.")
                    class_choice()
                else:
                    print("Unknown input. Please enter 'yes' or 'no'.")
                    cleric()
            cleric()
        
        # Druid
        elif choice == "druid":
            def druid():
                print("")
                print("Druids. Druids are worshippers of all things natural; a spellcaster,")
                print("friends to animals, and skilled at shapechanging.")
                drdch = input("Would you like to be a Druid?: ")
                drdch = drdch.lower()
                if drdch == "yes":
                    print("You are a Druid.")
                    hero_class["class"] = "Druid"
                elif drdch == "no":
                    print("Sounds good. Take your time.")
                    class_choice()
                else:
                    print("Unknown input. Please enter 'yes' or 'no'.")
                    druid()
            druid()
            
        # Fighter
        elif choice == "fighter":
            def fighter():
                print("")
                print("Fighters. Brave and stalwart, Fighters are a master of")
                print("all manner of arms and armor.")
                fghtrch = input("Would you like to be a Fighter?: ")
                fghtrch = fghtrch.lower()
                if fghtrch == "yes":
                    print("You are a Fighter.")
                    hero_class["class"] = "Fighter"
                elif fghtrch == "no":
                    print("Sounds good. Take your time.")
                    class_choice()
                else:
                    print("Unknown input. Please enter 'yes' or 'no'.")
                    fighter()
            fighter()
            
        # Monk
        elif choice == "monk":
            def monk():
                print("")
                print("Monks. Students of martial arts, Monks train their")
                print("bodies to be their greatest weapon and defense.")
                monkch = input("Would you like to be a Monk?: ")
                monkch = monkch.lower()
                if monkch == "yes":
                    print("You are a Monk.")
                    hero_class["class"] = "Monk"
                elif monkch == "no":
                    print("Sounds good. Take your time.")
                    class_choice()
                else:
                    print("Unknown input. Please enter 'yes' or 'no'.")
                    monk()
            monk()
        
        # Paladin
        elif choice == "paladin":
            def paladin():
                print("")
                print("Paladins. Paladins are the knights in shining armor,")
                print("devoted followers of law and good.")
                pldnch = input("Would you like to be a Paladin?: ")
                pldnch = pldnch.lower()
                if pldnch == "yes":
                    print("You are a Paladin.")
                    hero_class["class"] = "Paladin"
                elif pldnch == "no":
                    print("Sounds good. Take your time.")
                    class_choice()
                else:
                    print("Unknown input. Please enter 'yes' or 'no'.")
                    paladin()
            paladin()
            
        # Ranger
        elif choice == "ranger":
            def ranger():
                print("")
                print("Rangers. Trackers and hunters, Rangers are creatures")
                print("of the wild and of tracking down their favored foes.")
                rngrch = input("Would you like to be a Ranger?: ")
                rngrch = rngrch.lower()
                if rngrch == "yes":
                    print("You are a Ranger.")
                    hero_class["class"] = "Ranger"
                elif rngrch == "no":
                    print("Sounds good. Take your time.")
                    class_choice()
                else:
                    print("Unknown input. Please enter 'yes' or 'no'.")
                    ranger()
            ranger()

        # Rogue
        elif choice == "rogue":
            def rogue():
                print("")
                print("Rogues. The rogue is a thief and a scout, an opportunist")
                print("capable of delivering brutal strikes against unwary foes.")
                roguech = input("Would you like to be a Rogue?: ")
                roguech = roguech.lower()
                if roguech == "yes":
                    print("You are a Rogue.")
                    hero_class["class"] = "Rogue"
                elif roguech == "no":
                    print("Sounds good. Take your time.")
                    class_choice()
                else:
                    print("Unknown input. Please enter 'yes' or 'no'.")
                    rogue()
            rogue()
        
        # Sorcerer
        elif choice == "sorcerer":
            def sorcerer():
                print("")
                print("Sorcerers. The spellcasting sorcerers are born with an innate")
                print("knack for magic and have strange, eldritch powers.")
                srcrch = input("Would you like to be a Sorcerer?: ")
                srcrch = srcrch.lower()
                if srcrch == "yes":
                    print("You are a Sorcerer.")
                    hero_class["class"] = "Sorcerer"
                elif srcrch == "no":
                    print("Sounds good. Take your time.")
                    class_choice()
                else:
                    print("Unknown input. Please enter 'yes' or 'no'.")
                    sorcerer()
            sorcerer()
        
        # Warlock
        elif choice == "warlock":
            def warlock():
                print("")
                print("Warlocks. Experts in channelling arcan might wrested from primeval entities.")
                print("They commune with infernal intelligences and fey spirits to scour enemies.")
                wrlkchoice = input("Would you like to be a Warlock?: ")
                wrlkchoice = wrlkchoice.lower()
                if wrlkchoice == "yes":
                    print("You are a Warlock!")
                    hero_class["class"] = "Warlock"
                elif wrlkchoice == "no":
                    print("Sounds good. Take your time.")
                    class_choice()
                else:
                    print("Unknown input. Please enter 'yes' or 'no'.")
                    warlock()
            warlock()
                
        # Warlord
        elif choice == "warlord":
            def warlord():
                print("")
                print("Warlords. Accomplished and competent batle leaders. They stand on the front")
                print("line issuing commands and bolstering their allies while leading the battle with")
                print("weapon in hand.")
                wrldchoice = input("Would you like to be a Warlord?: ")
                wrldchoice = wrldchoice.lower()
                if wrldchoice == "yes":
                    print("You are a Warlord!")
                    hero_class["class"] = "Warlord"
                elif wrldchoice == "no":
                    print("Sounds good. Take your time.")
                    class_choice()
                else:
                    print("Unknown input. Please enter 'yes' or 'no'.")
                    warlord()
            warlord()
        
        # Wizard
        elif choice == "wizard":
            def wizard():
                print("")
                print("Wizards. The wizard masters magic through constant study that")
                print("gives him incredible magical power.")
                wzrdch = input("Would you like to be a Wizard?: ")
                wzrdch = wzrdch.lower()
                if wzrdch == "yes":
                    print("You are a Wizard.")
                    hero_class["class"] = "Wizard"
                elif wzrdch == "no":
                    print("Sounds good. Take your time.")
                    class_choice()
                else:
                    print("Unknown input. Please enter 'yes' or 'no'.")
                    wizard()
            wizard()

        # None
        else:
            print("Unknown input. Enter the class just as they are written.")
            class_choice()
        
    class_choice()

hero_classes()

# 5. Hero Rolls and Ability Scores
print("")
print("Now we will roll for your Ability Scores.")
def show_ab_scores():
    print("")
    print("Your ability scores are: ")
    for x in hero_ab_scores:
        print("%s : %s" % (x, hero_ab_scores[x]))

def rolls():
    for x in initial_rolls:
        initial_rolls[x] = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
        initial_rolls[x].sort()
        initial_rolls[x].reverse()
        initial_rolls[x] = (initial_rolls[x][0] + initial_rolls[x][1] + initial_rolls[x][2])
        if initial_rolls[x] < 10:
            initial_rolls[x] = 10
rolls()

def rolls_listed():
    print("")
    print("Your rolls are below:")
    for x in initial_rolls:
        print("Roll %s is %s." % (x, initial_rolls[x]))

def choosing(x):
    rolls_listed()
    chosen_stat = ("That stat has been chosen. Please choose another number.")
    choice = input("Which roll would you like to be your %s?: " % x)
        
    if choice == "1":
        if initial_rolls[choice] == "Chosen":
            print("")
            print(chosen_stat)
            choosing(x)
        else:
            hero_ab_scores[x] += initial_rolls[choice]
            initial_rolls[choice] = "Chosen"
    elif choice == "2":
        if initial_rolls[choice] == "Chosen":
            print("")
            print(chosen_stat)
            choosing(x)
        else:
            hero_ab_scores[x] += initial_rolls[choice]
            initial_rolls[choice] = "Chosen"
    elif choice == "3":
        if initial_rolls[choice] == "Chosen":
            print("")
            print(chosen_stat)
            choosing(x)
        else:
            hero_ab_scores[x] += initial_rolls[choice]
            initial_rolls[choice] = "Chosen"
    elif choice == "4":
        if initial_rolls[choice] == "Chosen":
            print("")
            print(chosen_stat)
            choosing(x)
        else:
            hero_ab_scores[x] += initial_rolls[choice]
            initial_rolls[choice] = "Chosen"
    elif choice == "5":
        if initial_rolls[choice] == "Chosen":
            print("")
            print(chosen_stat)
            choosing(x)
        else:
            hero_ab_scores[x] += initial_rolls[choice]
            initial_rolls[choice] = "Chosen"
    elif choice == "6":
        if initial_rolls[choice] == "Chosen":
            print("")
            print(chosen_stat)
            choosing(x)
        else:
            hero_ab_scores[x] += initial_rolls[choice]
            initial_rolls[choice] = "Chosen"
    else:
        print("Please choose an option from 1 to 6")
        choosing(x)

def choose_stats():
    for x in hero_ab_scores:
        choosing(x)

choose_stats()
show_ab_scores()

# 6. Hero Reroll and Ability Scores
def reroll_stats(x):
    hero_ab_scores[x] = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    hero_ab_scores[x].sort()
    hero_ab_scores[x].reverse()
    hero_ab_scores[x] = (hero_ab_scores[x][0] + hero_ab_scores[x][1] + hero_ab_scores[x][2])
    if hero_ab_scores[x] < 10:
        hero_ab_scores[x] = 10
    print("Your %s stat is now %s." % (x, hero_ab_scores[x]))

def reroll():
    print("")
    rrconfirm = input("Would you like to reroll one of your stats?: ")
    rrconfirm = rrconfirm.lower()
    if rrconfirm == "yes":
        rrstat = input("Sounds good. Which stat would you like to reroll?: ")
        rrstat = rrstat.title()
        if rrstat == "Strength":
            reroll_stats(rrstat)
        elif rrstat == "Dexterity":
            reroll_stats(rrstat)
        elif rrstat == "Constitution":
            reroll_stats(rrstat)
        elif rrstat == "Intelligence":
            reroll_stats(rrstat)
        elif rrstat == "Wisdom":
            reroll_stats(rrstat)
        elif rrstat == "Charisma":
            reroll_stats(rrstat)
        else:
            print("Unknown input. Please try again.")
            reroll()
    elif rrconfirm == "no":
        print("Sounds good! Let's continue.")
    else:
        print("Unknown input. Please type 'yes' or 'no'.")
        reroll()

reroll()

# 7. Hero Ability Modifiers
def ability_mods(x):
    if hero_ab_scores[x] <= 11:
        hero_ab_mods[x] = 0
    elif hero_ab_scores[x] == 12 or hero_ab_scores[x] == 13:
        hero_ab_mods[x] = 1
    elif hero_ab_scores[x] == 14 or hero_ab_scores[x] == 15:
        hero_ab_mods[x] = 2
    elif hero_ab_scores[x] == 16 or hero_ab_scores[x] == 17:
        hero_ab_mods[x] = 3
    elif hero_ab_scores[x] == 18 or hero_ab_scores[x] == 19:
        hero_ab_mods[x] = 4
    elif hero_ab_scores[x] >= 20:
        hero_ab_mods[x] = 5

def hero_mods():
    for x in hero_ab_mods:
        ability_mods(x)
        
hero_mods()

# 8. Summary of Hero
def summary():
    print("")
    print("Congratulations!")
    print("You are %s, the %s %s." %(hero_name["name"], hero_race["race"], hero_class["class"]))
    print("")
    print("Your alignment is %s." % hero_alnmt["alnmt"])
    print("")
    print("Your Ability Scores:")
    for x in hero_ab_scores:
        print("> %s: %s" % (x, hero_ab_scores[x]))
    print("")
    print("Your Ability Modifiers:")
    for x in hero_ab_mods:
        print("> %s: %s" % (x, hero_ab_mods[x]))

summary()

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

# Hero Hitpoints
def health():
    hero_hitpoints["maxhp"] += hero_class["initial_hp"] + hero_ab_scores["Constitution"]
    hero_hitpoints["bloodied"] += int(hero_hitpoints["maxhp"] / 2)
    hero_hitpoints["surgeval"] += int(hero_hitpoints["maxhp"] / 4)
    hero_hitpoints["surgenum"] += hero_class["initial_surge"] + hero_ab_mods["Constitution"]
    
health()

# Summary Interface
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




