spells = ["Rain Fire","Ice Lance","Teleport","Mana Ward","Arcane Missles"]

print ('''
Available spells:
1. {}
2. {}
3. {}
4. {}
5. {}

'''.format(spells[0],spells[1],spells[2],spells[3],spells[4]))

spellsequence = str(input('Enter 5 spell for activation(space-seperates): '))
splitspell = spellsequence.split(" ")
spellsactivationsequence = [spells[int(splitspell[0])-1],spells[int(splitspell[1])-1],spells[int(splitspell[2])-1],spells[int(splitspell[3])-1],
                            spells[int(splitspell[4])-1]]

print ('''
Activation Sequence 
{}
{}       
{}
{}
{}       
'''.format(spellsactivationsequence[0],spellsactivationsequence[1],spellsactivationsequence[2],spellsactivationsequence[3],spellsactivationsequence[4]))
print ("Ultimate Secret Spell: {} + {} + {}".format(spellsactivationsequence[0],spellsactivationsequence[2],spellsactivationsequence[4]))