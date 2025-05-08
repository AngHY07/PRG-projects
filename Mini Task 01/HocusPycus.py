# Ang Hao Yi (10273989D)
spells = ["Rain of Fire","Ice Lance","Teleport","Mana Ward","Arcane Missiles"]

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

print (f'''
Activation Sequence:
{spells[int(splitspell[0])-1]}
{spells[int(splitspell[1])-1]}       
{spells[int(splitspell[2])-1]}
{spells[int(splitspell[3])-1]}
{spells[int(splitspell[4])-1]}       
''')
print ("Ultimate Secret Spell: {} + {} + {}".format(spells[int(splitspell[0])-1],spells[int(splitspell[2])-1],spells[int(splitspell[-1])-1]))