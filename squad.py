
# n- name of the squad
# g- enum value of Goals
# hl- hero list, optional
class Squad:
    def __init__(self,n,g,hl=None):
        self.name = n
        self.goal = g
        self.heros = [] if hl is None else hl
        self.in_action = False

    def add_hero(self,h):
        self.heros.append(h)

    def add_all(self, hl):
        self.heros.extend(hl)
    def str_squad(self):
        return f"Squad name: {self.name}, squad goal: {self.goal.description}"