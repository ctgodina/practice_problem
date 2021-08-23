import copy
import random
unit_types = ["I", "M", "T", "L", "H", "A"]
ranks = [4, 4.1, 5, 5.1, 6, 6.1, 7, 7.1, 7.2]

class Unit:
    #create a unit with the following rank and unit type. sacrificed units
    #set to nothing
    def __init__(self, rank, unit_type):
        #Checks if the rank and unit types passed in are in the
        #list of ranks and unit types
        if(not(rank in ranks) or not(unit_type in unit_types)):
            print("rank ", rank, "or unit type ", unit_type, "invalid")
            quit()
        
        self.rank = rank
        self.unit_type = unit_type
        self.units_sacrificed = []

    #printing out the object
    def __str__(self):
        return f"{self.rank} star {self.unit_type}"
        #return f"{self.rank} star {self.unit_type} = {self.units_sacrificed}"

    def __repr__(self):
        return str(self)
    
    #checks if the unit should be promoted
    def requirements_met(self, units):
        flag = False
        if(self in units):
            u = 0
        else:
            u = 1
        #4.1 Star = 3 same type 4 Star unit
        if(self.rank == 4):
            #check there are 3 units to sacrifice
            if(len(units)<3-u):
                print("not enough units to promote")
                return False
            #check all 3 units are 4 Star
            flag = (units[0].rank == units[1].rank == 4)
            #check all same type
            flag = flag and (self.unit_type == units[0].unit_type == units[1].unit_type)
        #5 Star = 3 of any type 4.1 Star unit
        elif(self.rank == 4.1):
            #check there are 3 units to sacrifice
            if(len(units)<3-u):
                print("not enough units to promote")
                return False
            #check all 3 units are 4.1 Star units
            flag = (units[0].rank == units[1].rank == 4.1)
        #5.1 Star = 2 same type 5 Star unit
        elif(self.rank == 5):
            #check there are 2 units to sacrifice
            if(len(units)<2-u):
                print("not enough units to promote")
                return False
            #check all 2 units are 5 star units
            flag = (units[0].rank == 5)
            #check all same type
            flag = flag and (self.unit_type == units[0].unit_type)
        #6 Star = 3 of any type 5.1 Star unit
        elif(self.rank == 5.1):
            #check there are 3 units to sacrifice
            if(len(units)<3-u):
                print("not enough units to promote")
                return False
            #check all 3 units are 5.1 Star units
            flag = (units[0].rank == units[1].rank == 5.1)
        #6.1 Star = 2 same type 6 Star unit
        elif(self.rank == 6):
            #check there are 2 units to sacrifice
            if(len(units)<2-u):
                print("not enough units to promote")
                return False
            #check all 2 units are 6 Star units
            flag = (units[0].rank == 6)
            #check all same type
            flag = flag and (self.unit_type == units[0].unit_type)
        #7 Star = 3 of any type 6.1 Star unit
        elif(self.rank == 6.1):
            #check there are 3 units to sacrifice
            if(len(units)<3-u):
                print("not enough units to promote")
                return False
            #check all 3 units are 6.1 Star units
            flag = (units[0].rank == units[1].rank == 6.1)
        #7.1 Star = 3 same type 7 Star unit
        elif(self.rank == 7):
            #check there are 3 units to sacrifice
            if(len(units)<3-u):
                print("not enough units to promote")
                return False
            #check all 3 units are 7 Star units
            flag = (units[0].rank == units[1].rank == 7)
            #check all same type
            flag = flag and (self.unit_type == units[0].unit_type == units[1].unit_type)
        #7.2 Star = 3 of any type 7.1 Star unit
        elif(self.rank == 7.1):
            #check there are 3 units to sacrifice
            if(len(units)<3-u):
                print("not enough units to promote")
                return False
            #check all 3 units are 7.1 Star units
            flag = (units[0].rank == units[1].rank == 7.1)
            
        return flag
        
    #promotes the unit when valid sacrifices
    def promote(self, units):
        need_2 = [5, 6]
        need_3 = [4, 4.1, 5.1, 6.1, 7, 7.1]
        idx = -1 #default is units not in same list as promoted unit
        if(self in units):
            idx = units.index(self)
        if(self.requirements_met(units[idx:])):
            if(self.rank in need_2):
                self.units_sacrificed.append(copy.deepcopy([units[idx+1]]))
                units.remove(units[idx+1])
            elif(self.rank in need_3):
                self.units_sacrificed.append(copy.deepcopy([units[idx+1], units[idx+2]]))
                units.remove(units[idx+1])
                units.remove(units[idx+1])
            self.rank = ranks[ranks.index(self.rank) + 1]
            return True
        return False

#execution begins here
#TODO: i can get 7.1I but need the other 7.1 of other stuff while dividing the 5 types evenly
print (unit_types)
print(ranks)

squad = []
not_I = []
rand_types = random.sample(unit_types, 2)
rand_type1 = rand_types[0]
rand_type2 = rand_types[1]

for k in range(96): #6 groups dividing the 5 types equally to make up 2916 - 36 
    for i in range(1,6):
        not_I = not_I + [Unit(4, unit_types[i]) for j in range(6)]

#7.2I = 7.1I 7.1X 7.1X
#7.1I = 7I 7I 7I
for k in range(3):
    #7I = 6.1I 6.1X 6.1X
    #6.1I = 6I 6I
    for j in range(2):
        #6I = 5.1 I 5.1 X 5.1X    
        #5.1I = 5I 5I
        for i in range(2):
            #5I = 4.1I 4.1X 4.1X
            squad = squad + [Unit(4,"I") for i in range(3)] #4.1I 
            squad = squad + [not_I.pop(0) for x in range(6)] #4.1X 4.1X
        #5.1X 5.1X
        squad = squad + [not_I.pop(0) for x in range(2*2*9)] #9 units in 5I 2 of those in 5.1 and need 2 of 5.1X
    #6.1X 6.1X
    squad = squad + [not_I.pop(0) for x in range(2*108)]
#7.1X 7.1X
#Below replacing I with a random unit type not I
#7.1I = 7I 7I 7I
for k in range(3):
    #7I = 6.1I 6.1X 6.1X
    #6.1I = 6I 6I
    for j in range(2):
        #6I = 5.1 I 5.1 X 5.1X    
        #5.1I = 5I 5I
        for i in range(2):
            #5I = 4.1I 4.1X 4.1X
            squad = squad + [Unit(4,rand_type1) for i in range(3)] #4.1I
            for x in range(6):#4.1X 4.1X
                not_rand_type = [item for item in not_I if( (item.unit_type is not rand_type1) or (item.unit_type is not rand_type2) )]
                member = not_rand_type.pop(0)
                not_I.remove(member)
                squad = squad + [member]
        #5.1X 5.1X
        squad = squad + [not_I.pop(0) for x in range(2*2*9)] #9 units in 5I 2 of those in 5.1 and need 2 of 5.1X
    #6.1X 6.1X
    squad = squad + [not_I.pop(0) for x in range(2*108)]
#Below replacing I with a random unit type not I
#7.1I = 7I 7I 7I
for k in range(3):
    #7I = 6.1I 6.1X 6.1X
    #6.1I = 6I 6I
    for j in range(2):
        #6I = 5.1 I 5.1 X 5.1X    
        #5.1I = 5I 5I
        for i in range(2):
            #5I = 4.1I 4.1X 4.1X
            squad = squad + [Unit(4,rand_type2) for i in range(3)] #4.1I
            for x in range(6):#4.1X 4.1X
                not_rand_type = [item for item in not_I if( (item.unit_type is not rand_type1) or (item.unit_type is not rand_type2) )]
                member = not_rand_type.pop(0)
                not_I.remove(member)
                squad = squad + [member]
        #5.1X 5.1X
        squad = squad + [not_I.pop(0) for x in range(2*2*9)] #9 units in 5I 2 of those in 5.1 and need 2 of 5.1X
    #6.1X 6.1X
    squad = squad + [not_I.pop(0) for x in range(2*108)]
print("SQUAD LENGTH OF ", len(squad))
print("Random type number 1 is ", rand_type1)
print("Random type number 2 is", rand_type2)
for u_type in unit_types:
    print("Amount of ", u_type, " in squad", len([member for member in squad if(member.unit_type is u_type)]))
exit_loop = False
while True:
    print(squad)
    for unit in squad:
        if(unit.promote(squad)==False):
            exit_loop = True
            break
    if exit_loop:
        break
    

print(squad)
