from enum import Enum

AVIATION_POWER = 8


# goal enum holds an index and a description of the enum
class Goals(Enum):
    EAT = 1, "eat pizza"
    KILL = 2, "kill all people"
    BETTER = 3, "make better world"
    LAUGH = 4, "laugh all day"
    DESTROY = 5, "destroy buildings"
    REST = 6, "rest"
    REVENGE = 7, "revenge"
    SAVE = 8, "save the world"
    PEACE = 9, "make world peace"
    TSUNAMI = 10, "make big tsunami"
    EARTHQUAKE = 11, "earthquake"

    def __init__(self, num, description):
        self._index = num
        self._description = description

    @property
    def index(self):
        return self._index

    @property
    def description(self):
        return self._description


    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

class Hero:

    def __init__(self, na, powr, att):
        self.name = na
        self.__is_alive = True
        self.__power = powr
        self.attributes = att
        self.att_power = None

        self.__injured_degree = 0.0
        self.weapons_object = None
        self.weapons_power = 0
        self.goals = []
        self.__set_attributes_power()

    def set_weapons(self, weapons_obj):
        self.weapons_object = weapons_obj
        self.weapons_power = self.weapons_object.attack_power()

    def set_goals(self, goals):
        self.goals = goals

    def __set_attributes_power(self):
        att = self.attributes
        self.att_power = (int(att.aviation)) * AVIATION_POWER + att.strength + att.agility

    def get_power(self):
        return self.weapons_power + \
               ((100.0 - self.__injured_degree) / 100) * (self.att_power + self.__power)

    def inc_injury_deg(self, value):
        self.__injured_degree += value
        if (self.__injured_degree > 100):
            self.__is_alive = False
            print(self.name, "is dead!")
    def str_hero(self):
        result = f"{self.name}\n"
        result += f"\tPower={self.get_power()}\n"
        result += "\tAttributes: "+self.attributes.str_att()+"\n"
        if self.weapons_object != None:
            result += "\tWeapons: "+self.weapons_object.str_weapon_obj()
        return result


    @property
    def is_good(self):
        return self.attributes.popularity > 5

    @property
    def is_alive(self):
        return self.__is_alive