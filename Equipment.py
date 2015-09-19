class Armor(object):

    def __init__(self, armorType = 'Default', armorSet = 'Default', armorSlot = 'Default',
                 armorMin = 0, armorMax = 0, fireRes = 0, waterRes = 0, thunderRes = 0,
                 iceRes = 0, dragonRes = 0, numOfSlots = 0,
                 skill1 = 'Default', skill1Val = 0, skill2 = 'Default', skill2Val = 0,
                 skill3 = 'Default', skill3Val = 0, skill4 = 'Default', skill4Val = 0):
        self.armorType = armorType
        self.armorSet = armorSet
        self.armorSlot = armorSlot
        self.armorMin = armorMin
        self.armorMax = armorMax
        self.fireRes = fireRes
        self.waterRes = waterRes
        self.thunderRes = thunderRes
        self.iceRes = iceRes
        self.dragonRes = dragonRes
        self.numOfSlots = numOfSlots
        self.skill1 = skill1
        self.skill1Val = skill1Val
        self.skill2 = skill2
        self.skill2Val = skill2Val
        self.skill3 = skill3
        self.skill3Val = skill3Val
        self.skill4 = skill4
        self.skill4Val = skill4Val

    def ListSkills(self):
        print self.skill1 + ': ' + str(self.skill1Val)
        print self.skill2 + ': ' + str(self.skill2Val)
        print self.skill3 + ': ' + str(self.skill3Val)
        print self.skill4 + ': ' + str(self.skill4Val)

    def ListDefenses(self):
        print 'Armor: ' + str(self.armorMin) + '-' + str(self.armorMax)
        print 'Fire Resistance: ' + str(self.fireRes)
        print 'Water Resistance: ' + str(self.waterRes)
        print 'Thunder Resistance: ' + str(self.thunderRes)
        print 'Ice Resistance: ' + str(self.iceRes)
        print 'Drage Resistance: ' + str(self.dragonRes)

    def ListDetails(self):
        print self.armorSet + ' ' + self.armorSlot
        print 'Type: ' + self.armorType
        self.ListDefenses()
        print 'Number of slots: ' + str(self.numOfSlots)
        self.ListSkills()