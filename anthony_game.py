unit_types = ["I", "M", "T", "L", "H", "A"]
ranks = [4, 4.1, 5, 5.1, 6, 6.1, 7, 7.1, 7.2]

class Unit:
    #create a unit with the following rank and unit type. sacrificed units
    #set to nothing
    def __init__(self, rank, unit_type):
        #Checks if the rank and unit types passed in are in the
        #list of ranks and unit types
        if(not(rank in ranks) or not(unit_type in unit_types)):
            print("rank or unit type invalid")
            quit()
        
        self.rank = rank
        self.unit_type = unit_type
        self.units_sacrificed = []

    #printing out the object
    def __str__(self):
        return f"{self.rank} star {self.unit_type} = {self.units_sacrificed}"

    #checks if the unit should be promoted
    def requirements_met(self, units):
        flag = False
        #4.1 Star = 3 same type 4 Star unit
        if(self.rank == 4):
            #check there are 3 units to sacrifice
            if(len(units)<2):
                print("not enough units to promote")
                return
            #check all 3 units are 4 Star
            flag = (units[0].rank == units[1].rank == 4)
            #check all same type
            flag = flag and (self.unit_type == units[0].unit_type == units[1].unit_type)
        #5 Star = 3 of any type 4.1 Star unit
        elif(self.rank == 4.1):
            #check there are 3 units to sacrifice
            if(len(units)<2):
                print("not enough units to promote")
                return
            #check all 3 units are 4.1 Star units
            flag = (units[0].rank == units[1].rank == 4.1)
        #5.1 Star = 2 same type 5 Star unit
        elif(self.rank == 5):
            #check there are 2 units to sacrifice
            if(len(units)<1):
                print("not enough units to promote")
                return
            #check all 2 units are 5 star units
            flag = (units[0].rank == 5)
            #check all same type
            flag = flag and (self.unit_type == units[0].unit_type)
        #6 Star = 3 of any type 5.1 Star unit
        elif(self.rank == 5.1):
            #check there are 3 units to sacrifice
            if(len(units)<2):
                print("not enough units to promote")
                return
            #check all 3 units are 5.1 Star units
            flag = (units[0].rank == units[1].rank == 5.1)
        #6.1 Star = 2 same type 6 Star unit
        elif(self.rank == 6):
            #check there are 2 units to sacrifice
            if(len(units)<1):
                print("not enough units to promote")
                return
            #check all 2 units are 6 Star units
            flag = (units[0].rank == 6)
            #check all same type
            flag = flag and (self.unit_type == units[0].unit_type)
        #7 Star = 3 of any type 6.1 Star unit
        elif(self.rank == 6.1):
            #check there are 3 units to sacrifice
            if(len(units)<2):
                print("not enough units to promote")
                return
            #check all 3 units are 6.1 Star units
            flag = (units[0].rank == units[1].rank == 6.1)
        #7.1 Star = 3 same type 7 Star unit
        elif(self.rank == 7):
            #check there are 3 units to sacrifice
            if(len(units)<2):
                print("not enough units to promote")
                return
            #check all 3 units are 7 Star units
            flag = (units[0].rank == units[1].rank == 7)
            #check all same type
            flag = flag and (self.unit_type == units[0].unit_type == units[1].unit_type)
        #7.2 Star = 3 of any type 7.1 Star unit
        elif(self.rank == 7.1):
            #check there are 3 units to sacrifice
            if(len(units)<2):
                print("not enough units to promote")
                return
            #check all 3 units are 7.1 Star units
            flag = (units[0].rank == units[1].rank == 7.1)
            
        return flag
        
    #promotes the unit when valid sacrifices
    def promote(self, units):
        need_2 = [5, 6]
        need_3 = [4, 4.1, 5.1, 6.1, 7, 7.1]
        if(self.requirements_met(units)):
            if(self.rank in need_2):
                self.units_sacrificed.append([units[0]])
            elif(self.rank in need_3):
                self.units_sacrificed.append([units[0], units[1]])
            self.rank = ranks[ranks.index(self.rank) + 1]
            return True

#execution begins here
print (unit_types)
print(ranks)

myunit = Unit(4, "I")
print(myunit)
myunit.promote([Unit(4, "I"), Unit(4, "I")])
print(myunit)

