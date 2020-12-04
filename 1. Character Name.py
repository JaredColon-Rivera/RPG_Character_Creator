#Hero name

hero_name = {
        "name" : 0
        }

def name():
    print("Hello there adventurer! Before we start our journey, \nyou will have to create a name.\n")
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
                print("\nGlad to meet you %s! Now let's create your character." % hero_name["name"])
            elif nameconfirm == "no":
                print("\nSounds good. Take your time.")
                hname()
            else:
                print("\nUnknown input. Please type in a name.")
                hname()
    hname() 
name()