import Equipment


def main():
    leatherHead = Equipment.Armor('Blademaster','Leather','Head',1,71,-1,0,0,0,1,1,'Gathering',2,'Whim',3)
    leatherTorso = Equipment.Armor('Blademaster','Leather','Torso',1,71,-1,0,0,0,1,0,'Gathering',3,'Whim',2)
    leatherArms = Equipment.Armor('Blademaster','Leather','Arms',1,71,-1,0,0,0,1,1,'Gathering',1,'Whim',1)
    leatherWaist = Equipment.Armor('Blademaster','Leather','Waist',1,71,-1,0,0,0,1,0,'Gathering',3,'Whim',1,'Health',2,'Fate',-1)
    leatherFeet = Equipment.Armor('Blademaster','Leather','Feet',1,71,-1,0,0,0,1,0,'Gathering',1,'Whim',3)

    print "Details for the Leather Armor Set (Blademaster)"
    print '============================'
    leatherHead.ListDetails()
    print '============================'
    leatherTorso.ListDetails()
    print '============================'
    leatherArms.ListDetails()
    print '============================'
    leatherWaist.ListDetails()
    print '============================'
    leatherFeet.ListDetails()
    print '============================'

if __name__ == '__main__':
    main()