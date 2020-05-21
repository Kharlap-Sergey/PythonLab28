from inhabitant import Inhabitant
from nothing import Nothing

class Room(object):
    """this calss represents inhabitant object"""

    amount_members = 0
    def __init__(self, number = Nothing(), sanitary_state = Nothing(), general_state = Nothing()):
        Room.amount_members += 1

        self.number = number
        self._sanitary_state = sanitary_state
        self._general_state = general_state
        self.inhabitans = []

    def get_state_of_room(self):
        return self._sanitary_state + self._general_state

    def add_inhabitant(self, inhabitant):
        if isinstance(inhabitans, Inhabitant):
            self.inhabitans.append(inhabitant)

    def __str__(self):
        representer = f"room number {self.number}\tinhabitants:"

        for inhabitant in self.inhabitans:
            representer += '\n' + str(inhabitant)
        return representer

    def __del__(self):  # Деструктор класса
        Room.amount_members -= 1



