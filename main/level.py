from room import Room
from nothing import Nothing

class Level(object):
    """this calss represents level object"""
    amount_members = 0
    def __init__(self, number = Nothing()):
        Level.amount_members += 1

        self.bestrooms = []
        self.rooms = []
        self.number = number
        self.duty_list = Nothing()

    def add_room(self, room):
        if isinstance(room, Room):
            self.rooms.append(inhabitant)

    def _finde_best_rooms(self):
        self.bestrooms = []
        if(len(self.rooms) == 0):
            self.bestrooms = []
        else:
            best = self.rooms[0]
            for i in self.rooms:
                if best.get_state_of_room() < i.get_state_of_room():
                    best = i

            for i in self.rooms:
                if best.get_state_of_room() == i.get_state_of_room():
                    self.bestrooms.append(i);

    def get_str_duty_list(self):
        list = self._make_duty_list()
        str_list = ""
        for i in range(0, len(list)):
            boof = f"\nday {i+1}:"
            for inhabitant in list[i]:
                boof += f"\n{inhabitant}"
            str_list += boof
        return str_list

    def _make_duty_list(self, days = 30):
        inhabitants = []
        for room in self.rooms:
            inhabitants.extend(room.inhabitans)

        ans = []
        for i in range(days):
            ans.append(self._get_today_dutys(inhabitants))
        return ans

    def _get_today_dutys(self, inhabitants):

        ans = []
        for i in range(2):
            ans.append(self._get_next_duty(inhabitants))

        return ans

    def _get_next_duty(self, inhabitants):
        inhabitants = sorted(inhabitants, key = lambda inhabitant: inhabitant.duty_degree)
        
        for i in range(1, len(inhabitants)):
            if inhabitants[i].status != "S":
                inhabitants[i].duty_degree -= 1
        return inhabitants[0]

    def __str__(self):
        representer = f"level number - {self.number}\nrooms:"
        for room in self.rooms:
            representer += '\n' + str(room)

        return representer

    def __del__(self):  # Деструктор класса
        Level.amount_members -= 1

