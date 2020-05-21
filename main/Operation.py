from level import Level
from room import Room
from inhabitant import Inhabitant
from nothing import Nothing
from dormitory import Dormitory

class Operation(object):
    """description of class"""
    @staticmethod
    def _get_dormitory_member(string):
        try:
            name = string.split()[1]
            name.rstrip("\n")
            dorm = Dormitory(name)
            return dorm
        except:
            return None
    @staticmethod
    def _get_Level_member(string):
        try:
            number = string.split()[1]
            return Level(int(number))
        except:
            return None
    @staticmethod
    def _get_room_member(string):
        try:
            inf_sp = string.split()
            number = inf_sp[1]
            sanit_st = inf_sp[2]
            gener_st = inf_sp[3]
            return Room(int(number), int(sanit_st), int(gener_st))
        except:
            return None
    @staticmethod
    def _get_inhabitant_member(string):
        try:
            inf_sp = string.split()
            name = inf_sp[0]
            surname = inf_sp[1]
            gender = inf_sp[2]
            age = inf_sp[3]
            status = inf_sp[4]
            return Inhabitant(name, surname, gender, int(age), status)
        except Simp:
            return None
    
    @staticmethod
    def getDormitory(inf):
        if not isinstance(inf, list):
            return
   
        level = None
        dormitory = None
        room = None
        inhabitant = None
        for i in inf:
            inf_word = i.split()[0]
            if inf_word == 'dorm':
                Fdormitory = True
                lvevel = None
                dormitory = Operation._get_dormitory_member(i)
            elif inf_word ==  "level":
                if dormitory == None:
                    print("Dormitory wasn't distinguished")
                    return

                if level != None:
                    if room != None:
                        level.rooms.append(room)
                        room = None

                    dormitory.levels.append(level)
                    level = None

                level = Operation._get_Level_member(i)
            
            elif inf_word == "room":
                if level == None:
                    print("level wasn't distinguished")
                    return

                if room != None:
                    level.rooms.append(room)
                    room = None

                room =Operation._get_room_member(i)
                inhabitant = None
            else:
                if room == None:
                    print("room wasn't distinguished")
                    return

                inhabitant = Operation._get_inhabitant_member(i)
                if inhabitant != None:
                    room.inhabitans.append(inhabitant)
                    inhabitant = None
                else:
                    print("inhabitant wasn't distinguished")
                    return

        if level != None and dormitory != None:
            if room != None:
                level.rooms.append(room)
            dormitory.levels.append(level)

        return dormitory


