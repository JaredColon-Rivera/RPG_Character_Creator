# Summary of Hero

def summary():
    print("\nCongratulations!")
    print("You are %s, the (race) (class)." % hero_name["name"])
    print("Your alignment is %s." % hero_alnmt["alnmt"])
    print("\nYour Ability Scores:")
    for x in hero_ab_scores:
        print("> %s: %s" % (x, hero_ab_scores[x]))
    print("")
    print("\nYour Ability Modifiers:")
    for x in hero_ab_mods:
        print("> %s: %s" % (x, hero_ab_mods[x]))

summary()
        
