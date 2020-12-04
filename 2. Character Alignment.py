#FINAL Hero Alignment

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

def alignment():
    print("\nYour hero will have a specific alignment.\n")
    for x in alignments:
        print("> %s" % x)
    def algn():
        alnmt = input("What is your alignment?: ")
        alnmt = alnmt.title()
        hero_alnmt["alnmt"] = alnmt
        if hero_alnmt["alnmt"] in alignments:
          print("Your alignment is %s." % hero_alnmt["alnmt"])
        else:
            print("Unknown input. Please enter an alignment as they are written.")
            algn()
    algn()
alignment()
