# Final Hero Class

hero_class = {
        "class" : 0,
        "initial_hp" : 0,
        "initial_surge" : 0,
        "feats" : []
        }

hero_defense = {
        "AC"   : 0,
        "FORT" : 0,
        "REF"  : 0,
        "WILL" : 0,
        "NONE" : 0
        }

hero_prof = {
        "armor" : [],
        "weapon" : []
        }

classes = [
        "Cleric",
        "Fighter",
        "Paladin",
        "Ranger",
        "Rogue",
        "Warlock",
        "Warlord",
        "Wizard"
        ]
#---------------Cleric Features---------------#
channel_divinity_cleric = "Once per encounter you can invoke divine power, such as 'turn undead' and 'divine fortune'"
healers_lore = "When you grant healing with one of your cleric powers that has the healing keyword, \nadd your Wisdom modifier to the hit points the recipient regains"
healing_word = "You can whisper a brief prayer and you or an ally gain an addition 1d6 hit points when they are spending a healing surge"
ritual_casting_cleric = "You possess a ritual book and it contains two rituals that you have mastered: the \nGentle Repose ritual and one other 1st-level ritual of your choice"

#---------------Fighter Features---------------#
combat_challenge = "Every time you attack an enemy, whether the attack hits or misses, you can choose to mark that target. The mark \nlasts until the end of your next turn. While a target is marked, \nit takes a –2 penalty to attack rolls for any attack that doesn’t include you as a target"
combat_superiority = "You gain a bonus to opportunity attacks equal to your Wisdom modifier"
fighter_weapon_talent = "Choose either one-handed or two-handed weapons. When using a weapon of \nyour chosen style, you gain a +1 bonus to attack rolls"

#---------------Paladin Features---------------#
channel_divinity_paladin = "Once per encounter you can invoke divine power, such as 'divine mettle' and 'divine strength'"
divine_challenge = " You can use the 'divine challenge' power to mark an enemy of your choice"
lay_on_hands = " You spend a healing surge but regain no hit points. Instead, the target regains \nhit points as if it had spent a healing surge. "

#---------------Ranger Features---------------#
archer_fighting_style = "You gain Defensive Mobility as a bonus feat"
two_blade_fighting_style = "You can wield a one-handed weapon on your off hand as if it were an off-hand weapon. \nIn addition, you gain Toughness as a bonus feat"
fighting_style = "You have the choice of of two fighting styles: \n> Archer Fighting Style: %s, \n> Two-Blade Fighting Style: %s" % (archer_fighting_style, two_blade_fighting_style)
hunters_quarry = "Once per turn as a minor action, you can designate the enemy nearest to you as your quarry. \nOnce per round, you deal extra damage to your quarry based off of your level"
prime_shot = "If none of your allies are nearer to your target than you are, you receive a +1 bonus to \nranged attack rolls against that target"

#---------------Rogue Features---------------#
artful_dodger = "You gain a bonus to AC equal to your Charisma modifier against opportunity attacks"
brutal_scoundrel = "You gain a bonus to Sneak Attack damage equal to your Strength modifier"
first_strike = "At the start of an encounter, you have combat advantage against any creatures that have not yet acted in that encounter"
rogue_tactics = "You can choose one of the following options: \n> Artful Dodger: %s, \n> Brutal Scoundrel: %s" % (artful_dodger, brutal_scoundrel)
rogue_weapon_tlnt = "When you wield a shuriken, your weapon damage die increase by one size. \nWhen you wield a dagger, you gain a +1 bonus to attack rolls"
sneak_attack = "Once per round, when you have combat advantage against an enemy and are using \na weapon from the light blade, the crossbow, or the sling weapon group, an attack you make \nagainst that enemy deals extra damage if the attack hits"

#---------------Warlock Features---------------#
eyebite = "You know the Eyebite at-will spell"
misty_step = "When an enemy under your Warlock's Curse is reduced to 0 hitpoints or fewer, you can immediately teleport 3 squares as a free action"
fey_pact = "You have forged a bargain with ancient, amoral powers of the Feywild. \nYou will know the following: \n> Eyebite: %s, \n> Misty Step: %s" % (eyebite, misty_step)
hellish_rebuke = "You know the Hellish Rebuke at-will skill"
dark_ones_blessing = "When an enemy under your Warlock's Curse is reduced to 0 hitpoints or fewer, you immediately gain temporary hitpoints equal to your level"
infernal_pact = "Long ago a forgotten race of devils created a secret path to power and taught it to the tieflings \nof old to weaken their fealty to Asmodeus. \nYou will know the following: Hellish Rebuke: %s, \nDark One's Blessing: %s" % (hellish_rebuke, dark_ones_blessing)
dire_radiance = "You know the Dire Radiance at-will spell"
fate_of_the_void = "When an enemy under your Warlock's Curse is reduced to 0 hitpoints or fewer, you gain a +1 bonus \nto any single d20 roll you make during your next turn (attack roll, saving throw, skill check, or ability check)"
star_pact = "You have mastered the astrologer's art, learning the secret names of the stars and gazing into the Far beyond, gaining great power thereby. \nYou will know the following: Dire Radiance: %s, \nFate of the Void: %s" % (dire_radiance, fate_of_the_void)
eldritch_blast = "You know the 'Eldritch Blast' at-will power. This power can be used as a basic attack"
eldritch_pact = "Choose one of the following pacts: \n> Fey Pact: %s \n> Infernal Pact: %s \n> Star Pact: %s. Your pact determines one of the at-will spells you know. \nEach pact includes a pact boon. The pact boon is a granted power you can use to further hex your enemies" % (fey_pact, infernal_pact, star_pact)
prime_shot = "If none of your allies are nearer to your target than you are, you receive a +1 bonus to ranged attack rolls against that target"
shadow_walk = "On your turn, if you move at least 3 squares away from where you started your turn, you gain concealment until the end of your next turn"
warlocks_curse = "Once per turn as a minor action, you can place a Warlock's Curse on the enemy nearest to you that you can see. \nA cursed enemy takes extra damage from your attacks"

#---------------Warlord Features---------------#
inspiring_presence = "When an ally who can see you spends an action point to take an extra action, that ally also regains \nlost hit points equal to one-half your level + your Charisma modifier. \nIf the ally can see multiple warlord allies who have this class feature, \nthe ally regains hit points from only one of them (the ally's choice)"
tactical_presence = "When an ally you can see spends an action point to make an extra attack, the ally gains a bonus to the \nattack roll equal to one-half your Intelligence modifier. \nIf multiple warlord allies who have this class feature can see the ally, he or \nshe gains the bonus from only one of them (the ally's choice)"
combat_leader = "You and each ally within 10 squares who can see and hear you gain a +2 power bonus to initiative"
commanding_presence = "Choose 1 of the following: \n> Inspiring Presence: %s, \n> Tactical Presence: %s" % (inspiring_presence, tactical_presence)
inspiring_word_descr = "You can use 'inspiring word' as an encounter power"

#---------------Wizard Features---------------#
ghost_sound = "You cause a sound as quiet as a whisper or as loud as a yelling or fighting creature to emanate from the target. \nYou can produce nonvocal sounds such as the ringing of a sword blow, jingling armor, or scraping stone"
light = "You cause the target to shed bright light. The light fills the target’s square and all squares within 4 squares of it. \nThe light lasts for 5 minutes. Putting out the light is a free action"
mage_hand = "You gesture toward an object nearby, and a spectral floating hand lifts the object into the air and moves it where you wish"
prestidigitation = "You perform an amusing magical trick, such as creating a dancing wisp of light, freshening a wilting flower, \nmaking a coin invisible, or warming a cold drink. You can have as many as three prestidigitation effects active at one time"
orb_of_imposition = "Once per encounter as a free action, you can use your orb to gain on the following two effects: \n> You can designate one creature you have cast a wizard spell upon that has an effect \nthat lasts until the subject succeeds on a saving throw. That creature takes a penalty to its saving \nthrows against that effect equal to your Wisdom modifier \n> Alternatively, you can choose to extend the duration of an effect created by a wizard at-will spell \nthat would otherwise end at the end of your current turn. \nThe effect instead ends at the end of your next turn"
staff_of_defense = "A staff of defense grants you a +1 bonus to AC. In addition, once per encounter as an immediate \ninterrupt, you gain a bonus to defense against one attack equal to your Constitution modifier. \nYou can declare the bonus after the Dungeon Master has already told you the damage total"
wand_of_accuracy = "Once per encounter as a free action, you gain a bonus to a single attack roll equal to your Dexterity modifier. \nYou must wield your wand to benefit from this feature"
arcane_implement_mastery = "Choose one of the following forms of implement mastery: \n> Orb of Imposition: %s \n> Staff of Defense: %s \nWand of Accuracy: %s" % (orb_of_imposition, staff_of_defense, wand_of_accuracy)
cantrips = "Cantrips are minor spells you gain at 1st level. You can use the following cantrips as at-will powers: \n> Ghost Sound: %s \n> Light: %s \n> Mage Hand: %s \n> Prestidigitation: %s" % (ghost_sound, light, mage_hand, prestidigitation)
ritual_casting_wizard = "You gain the Ritual Caster feat as a bonus feat, allowing you to use magical rituals"
spell_book_wizard = "You possess a spellbook, a book full of mystic lore in which you store your rituals and your daily and utility spells"

#---------------Class Description---------------#
def class_descr(classdescr, 
                classchoice,
                role, 
                powersource, 
                keyabilities1, keyabilities2, keyabilities3, keyabilities4, 
                armorprof1, armorprof2, armorprof3, armorprof4, armorprof5, armorprof6, armorprof7, armorprof8,
                weaponprof1, weaponprof2, weaponprof3, weaponprof4, weaponprof5,
                defbonusstat1, defbonusstat2, defbonusstat3,
                defbonus1, defbonus2, defbonus3,
                initialhp,
                hpperlvl,
                hsperday,
                trainedskill1, trainedskill2, trainedskill3, trainedskill4, trainedskill5, trainedskill6, trainedskill7, trainedskill8, trainedskill9, trainedskill10,
                skillchnum,
                buildoption1, buildoption2,
                classfeat1, classfeat2, classfeat3, classfeat4, classfeat5,
                classfeatdescr1, classfeatdescr2, classfeatdescr3, classfeatdescr4, classfeatdescr5):

    print("\n%s\n" % classdescr)
    print("> Role: %s" % role)
    print("> Power Source: %s" % powersource)
    print("> Key Abilities: %s, %s, %s, %s\n" % (keyabilities1, keyabilities2, keyabilities3, keyabilities4))
    print("> Armor Proficiencies: %s, %s, %s, %s, %s, %s, %s, %s" % (armorprof1, armorprof2, armorprof3, armorprof4, armorprof5, armorprof6, armorprof7, armorprof8))
    print("> Weapon Proficiencies: %s, %s, %s, %s, %s" % (weaponprof1, weaponprof2, weaponprof3, weaponprof4, weaponprof5))
    print("> Bonus to Defense: %s, %s, %s\n" % (defbonusstat1, defbonusstat2, defbonusstat3))
    print("> Hit Points at 1st Level: %s + Constitution Score" % initialhp)
    print("> Hit Points per Level Gained: %s" % hpperlvl)
    print("> Healing Surges per Day: %s + Constitution Modifier\n" % hsperday)
    print("Class Trained Skills:")
    print("> %s" % (trainedskill1))
    print("> %s" % (trainedskill2))
    print("Choose %s more skills from the list below:" % skillchnum)
    print("> %s" % (trainedskill3))
    print("> %s" % (trainedskill4))
    print("> %s" % (trainedskill5))
    print("> %s" % (trainedskill6))
    print("> %s" % (trainedskill7))
    print("> %s" % (trainedskill8))
    print("> %s" % (trainedskill9))
    print("> %s\n" % (trainedskill10))
    print("> Build Options: %s, %s" % (buildoption1, buildoption2))
    print("> %ss have the following Class Features:" % classchoice)
    print("> %s : %s" %(classfeat1, classfeatdescr1))
    print("> %s : %s" %(classfeat2, classfeatdescr2))
    print("> %s : %s" %(classfeat3, classfeatdescr3))
    print("> %s : %s" %(classfeat4, classfeatdescr4))
    print("> %s : %s\n" %(classfeat5, classfeatdescr5))

    #---------------Class Choice---------------#
    choice = input("Would you like to be a %s?: " % classchoice)
    choice = choice.lower()
    if choice == "yes":
        print("You are a %s!" % classchoice)

        #------------Class Prof/Def/Health/Feats---------------#
        hero_class["class"] = classchoice
        hero_prof["armor"].append(armorprof1)
        hero_prof["armor"].append(armorprof2)
        hero_prof["armor"].append(armorprof3)
        hero_prof["armor"].append(armorprof4)
        hero_prof["armor"].append(armorprof5)
        hero_prof["armor"].append(armorprof6)
        hero_prof["armor"].append(armorprof7)
        hero_prof["armor"].append(armorprof8)
        hero_prof["weapon"].append(weaponprof1)
        hero_prof["weapon"].append(weaponprof2)
        hero_prof["weapon"].append(weaponprof3)
        hero_prof["weapon"].append(weaponprof4)
        hero_prof["weapon"].append(weaponprof5)
        hero_defense[defbonus1] += 1
        hero_defense[defbonus2] += 1
        hero_defense[defbonus3] += 1
        hero_class["initial_hp"] += initialhp
        hero_hitpoints["surgenum"] += hsperday
        hero_class["feats"].append(classfeat1)
        hero_class["feats"].append(classfeat2)
        hero_class["feats"].append(classfeat3)
        hero_class["feats"].append(classfeat4)
        hero_class["feats"].append(classfeat5)

    elif choice == "no":
        print("Sounds good. Take your time.\n")
        class_choice()
    else:
        print("Unknown input.\n")
        class_choice()

def class_description(classpick):
    if classpick == "Cleric":
        #---------------Cleric Class---------------#
        class_descr(
                "Clerics are battle leaders who are invested with divine power. \nThey blast foes with magical prayes, bolster and heal companions, and lead the way \nto victory with a mace in one hand and a holy symbol in the other.",
                "Cleric",
                "Leader. You lead by shielding allies with your prayers, healing, and using powers that improve your allies' attacks",
                "Divine. You have been invested with the authority to wield divine power to behalf of a deity, faith, or philosophy",
                "Wisdom", "Strength", "Charisma", " ",
                "Cloth", "Leather", "Hide", "Chainmail", " ", " ", " ", " ",
                "Simple Melee", "Simple Ranged", " ", " ", " ",
                "Will", " ", " ",
                "WILL", "WILL", "NONE",
                12,
                5,
                7,
                "Religion", " ", "Arcana", "Diplomacy", "Heal", "History", "Insight", " ", " ", " ",
                3,
                "Battle Cleric", "Devoted Cleric",
                "Channel Divinity", "Healer's Lore", "Healing Word", "Ritual Casting", " ",
                channel_divinity_cleric, healers_lore, healing_word, ritual_casting_cleric, " ")
        
    elif classpick == "Fighter":
        #---------------Fighter Class---------------#
        class_descr(
                    "Fighters are determined combat adepts trained to protect the \nother members of their adventuring groups",
                    "Fighter",
                    "Defender. You are very tough and hae exceptional ability to contain enemies in melee",
                    "Martial. You have become a master of combat through endless hours of practice, \ndetermination, and your own sheer physical toughness",
                    "Strength", "Dexterity", "Wisdom", "Constitution",
                    "Cloth", "Leather", "Hide", "Chainmail", "Scale", "Light Shield", "Heavy Shield", " ",
                    "Simple Melee", "Military Melee", "Simple Ranged", "Military Ranged", " ",
                    "Fortitude", "Fortitude", " ",
                    15,
                    6,
                    9,
                    " ", " ", "Athletics", "Endurance", "Heal", "Intimidate", "Streetwise", " ", " ", " ",
                    3,
                    "Great Weapon Fighter", "Guardian Fighter",
                    "Combat Challenge", "Combat Superiority", "Fighter Weapon Talent", " ", " ",
                    combat_challenge, combat_superiority, fighter_weapon_talent, " ", " ")

    elif classpick == "Paladin":
         #---------------Paladin Class---------------#
        class_descr(
                    "Paladins are indomitable warriors who've pledged their prowess to something greater than themselves. \nPaladins smite enemies with divine authority, bolster the courage of nearby companions, \nand radiate as if a beacon of inextinguishable hope",
                    "Paladin",
                    "Defender. You are extremely durable, with high hit points and the ability to wear the heaviest armor. \nYou can issue bold challenges to foes and compel them to fight you rather than your allies",
                    "Divine. You are a divine warrior, a crusader and protector of your faith",
                    "Strength", "Charisma", "Wisdom", " ",
                    "Cloth", "Leather", "Hide", "Chainmail", "Scale", "Plate", "Light Shield", "Heavy Shield",
                    "Simple Melee", "Military Melee", "Simple Ranged", " ", " ",
                    "Fortitude", "Reflex", "Will",
                    15,
                    6,
                    10,
                    "Religion", " ", "Diplomacy", "Endurance", "Heal", "History", "Insight", "Intimidate", " ", " ",
                    3,
                    "Avenging Paladin", "Protecting Paladin",
                    "Channel Divinity", "Divine Challenge", "Lay On Hands", " ", " ",
                    channel_divinity_paladin, divine_challenge, lay_on_hands, " ", " ")

    elif classpick == "Ranger":
        #---------------Ranger Class---------------#
        class_descr(
                    "Rangers are watchful warriors who roam past the horizon to safeguard a region, a principle, or a way of life. \nMasters of bow and blade, rangers excel at hit-and-run assaults and can quickly and silently eliminate foes",
                    "Ranger",
                    "Striker. You concentrate on either ranged attacks or two-weapon melee fighting to deal a lit of damage to one enemy at a time. \nYour attacks rely on speed and mobility, since you prefer to use hit-and-run tactics whenever possible",
                    "Martial. Your talents depend on extensive training and practice, inner confidence, and natural proficiency",
                    "Strength", "Dexterity", "Wisdom", " ",
                    "Cloth", "Leather", "Hide", " ", " ", " ", " ", " ",
                    "Simple Melee", "Military Melee", "Simple Ranged", "Military Ranged", " ",
                    "Fortitude", "Reflex", " ",
                    12,
                    5,
                    6,
                    " ", " ", "Acrobatics", "Athletics", "Dungeoneering", "Endurance", "Heal", "Nature", "Perception", "Stealth",
                    4,
                    "Archer Ranger", "Two-Blade Ranger",
                    "Fighting Style", "Hunter's Quarry", "Prime Shot", " ", " ",
                    fighting_style, hunters_quarry, prime_shot, " ", " ")

    elif classpick == "Rogue":
        #---------------Rogue Class---------------#
        class_descr(
                    "Rogues are cunning and elusive adversaries. Rogues slip into and out of shadows on a whim, pass anywhere across the field of battle \nwithout fear of reprisal, and appear suddenly only to drive home a lethal blade",
                    "Rogue",
                    "Striker. You dart in to attack, do masive damage, and then retreat to safety. You do best when teamed with a defender to flank enemies",
                    "Martial. Your talents depend on extensive training and constant practice, innate skill, and natural coordination",
                    "Dexterity", "Strength", "Charisma", " ",
                    "Cloth", "Leather", " ", " ", " ", " ", " ", " ",
                    "Dagger", "Hand-Crossbow", "Shuriken", "Sling", "Short Sword", 
                    "Reflex", "Reflex", " ",
                    12,
                    5,
                    6,
                    "Stealth", "Thievery", "Acrobatics", "Athletics", "Bluff", "Dungeoneering", "Insight", "Intimidate", "Perception", "Streetwise",
                    4,
                    "Brawny Rogue", "Trickster Rogue",
                    "First Strike", "Rogue Tactics", "Rogue Weapon Talent", "Sneak Attack", " ",
                    first_strike, rogue_tactics, rogue_weapon_tlnt, sneak_attack, " ")

    elif classpick == "Warlock":
        #---------------Warlock Class---------------#
        class_descr(
                    "Warlocks channel arcane might wrested from primeval entities. They commune with infernal intelligencies and fey spirits, \nscour enemies with potent blasts of eldritch power, and bedevil foes with hexing curses",
                    "Warlock",
                    "Striker. Your attack powers are highly damaging and often weaken or hamper the target in some way. \nYou can elude attacks by flying, teleporting, or turning invisible",
                    "Arcane. You gain your magical power from a pact you forge with a powerful, supernatural force or an unnamed entity",
                    "Charisma", "Constitution", "Intelligence", " ",
                    "Cloth", "Leather", " ", " ", " ", " ", " ", " ",
                    "Simple Melee", "Simple Ranged", " ", " ", " ",
                    "Reflex", "Will", " ",
                    12,
                    5,
                    6,
                    " ", " ", "Arcana", "Bluff", "History", "Insight", "Intimidate", "Religion", "Streetwise", "Thievery",
                    4,
                    "Deceptive Warlock", "Scourge Warlock",
                    "Eldritch Blast", "Eldritch Pact", "Prime Shot", "Shadow Walk", "Warlock's Curse",
                    eldritch_blast, eldritch_pact, prime_shot, shadow_walk, warlocks_curse)

    elif classpick == "Warlord":
        #---------------Warlord Class---------------#
        class_descr(
                    "Warlords are accomplished and competent battle leaders. Warlords stand on the front line issuing commands and bolstering their allies \nwhile leading the battle with weapon in hand",
                    "Warlord",
                    "Leader. You are an inspiring commander and a master of battle tactics",
                    "Martial. You have become an expert in tactics through endless hours of training and practice, personal determination, \nand your own sheer physical toughness",
                    "Strength", "Intelligence", "Charisma", " ", 
                    "Cloth", "Leather", "Hide", "Chainmail", "Light Shield", " ", " ", " ",
                    "Simple Melee", "Military Melee", "Simple Ranged", " ", " ",
                    "Fortitude", "Will", " ", 
                    12,
                    5, 
                    7,
                    " ", " ", "Athletics", "Diplomacy", "Endurance", "Heal", "History", "Intimidate", " ", " ",
                    4,
                    "Inspiring Warlord", "Tactical Warlord", 
                    "Combat Leader", "Commanding Presence", "Inspiring Word", " ", " ", 
                    combat_leader, commanding_presence, inspiring_word_descr)

    elif classpick == "Wizard":
        #---------------Wizard Class---------------#
        class_descr(
                    "Wizards are scions of arcane magic. Wizards tap the true power that permeates the cosmos, research \nesoteric rituals that can alter time and space, and hurl balls of fire that incinerate massed foes",
                    "Wizard",
                    "Controller. You exert control through magical effects that cover large areas—sometimes hindering \nfoes, sometimes consuming them with fire",
                    "Arcane. You channel arcane forces through extensive study, hidden knowledge, and intricate preparation. \nTo you, magic is an art form, an expressive and powerful method by which you seek to \ncontrol the world around you",
                    "Intelligence", "Wisdom", "Dexterity", " ",
                    "Cloth", " ", " ", " ", " ", " ", " ", " ",
                    "Dagger", "Quarterstaff", " ", " ", " ",
                    "Will", "Will", " ", 
                    10,
                    4,
                    6,
                    "Arcana", " ", "Diplomacy", "Dungeoneering", "History", "Insight", "Nature", "Religion", " ", " ",
                    3,
                    "Control Wizard", "War Wizard", 
                    "Arcane Implement Mastery", "Cantrips", "Ritual Casting", "Spellbook", " ",
                    arcane_implement_mastery, cantrips, ritual_casting_wizard, spell_book_wizard)

def class_choice():
    print("Now, you will pick a class.")
    print("")
    print("Here are all the classes to choose from:")
    for x in classes:
        print("> %s" % x)
    classpick = input("\nWhich class would you like to learn about?: ")
    classpick = classpick.title()

    #---------------Hero Class Description---------------#
    if classpick in classes:
        class_description(classpick)
    else:
        print("Unknown input.")
        print("Please type in an ability score to increase.\n")
        class_choice()
        
class_choice()

