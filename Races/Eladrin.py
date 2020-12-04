# Eladrin Race

eladrin_education = "You gain training in one additional skill (any skill, not just Class Skills)"
eladrin_weapon_prof = "You gain proficiency with the longsword"
eladrin_will = "You gain a +1 racial bonus to your Will defense. In addition, you gain a +5 racial \nbonus to saving throws against charm effects"
fey_origin = "Your ancestors were native to the Feywild, so you are considered a fey creature"
trance = "Rather than sleep, eladrin enter a meditative state known as trance. You need to spend 4 \nhours in this state to gain the same benefits other races gain from taking \na 6-hour extended rest. While in a trance, you are fully aware of your surroundings \nand notice approaching enemies and other events as normal."
fey_step = "You can use 'fey step' as an encounter power"

# Eladrin Description
def eladrin_descr():
	print("Eladrin. Creatures of magic with strong ties to nature. They live \nin cities in the twilight realm of the Feywild.\n")
    print("Play a Eladrin if you want...")
    print("> a race that favors the wizard, rogue, and warlord classes")
    print("> to be otherwordly and mysterious")
    print("> to be graceful and intelligent")
    print("> to teleport around the battlefield, cloaked in the magic of the Feywild\n")
    print("The Eladrin have the following stats:")
    print("> Intelligence : +2")
    print("> Dexterity : +2")
    print("> Speed : 6 squares")
    print("> Vision    : Low-Light")
    print("> Languages : Common, Elven")
    print("> Arcana   : +2")
    print("> History  : +2\n")
    print("The Eladrin have the following racial features:")
    print("> Eladrin Education: %s" % eladrin_education)
    print("> Eladrin Weapon Proficiency: %s" % eladrin_weapon_prof)
    print("> Eladrin Will: %s" % eladrin_will)
    print("> Fey Origin: %s" % fey_origin)
    print("> Trance: %s" % trance)
    print("> Fey Step: %s" % fey_step)


eladrin_descr()

# Eladrin Initial Stats/Skills/Feats
def eladrin_initial():
	hero_race["race"] = "Eladrin"
    hero_race["speed"] = 6
    hero_race["Feats"].append("Low-Light Vision")
    hero["language"].append("Common")
    hero["language"].append("Elven")
    hero_race["feats"].append("Eladrin Education")
    hero_race["feats"].append("Eladrin Weapon Proficiency")
    hero_race["feats"].append("Eladrin Will")
    hero_race["feats"].append("Fey Origin")
    hero_race["feats"].append("Trance")
    hero_race["feats"].append("Fey Step")
    hero_ab_scores["Intelligence"] += 2
    hero_ab_scores["Dexterity"] += 2
    hero_skills["Arcana"] += 2
    hero_skills["History"] +=2

eladrin_initial()