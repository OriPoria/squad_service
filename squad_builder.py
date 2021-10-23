from abc import ABCMeta, abstractmethod
from hero import Goals
from squad import Squad
from heros_pool import out_of_box_squads


class SquadBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build(self,heros):
        pass


class GoodAndBadSquads(SquadBuilder):
    def build(self, heros):
        dic_squads = {}
        good_squad_name = "Good heros"
        bad_squad_name = "Bad heros"
        good_squad = Squad(good_squad_name, g="make all people good")
        bad_squad = Squad(bad_squad_name, g="make all people bad")
        dic_squads[good_squad_name] = good_squad
        dic_squads[bad_squad_name] = bad_squad

        for h in heros:
            if h.is_good:
                good_squad.add_hero(h)
            else:
                bad_squad.add_hero(h)
        return dic_squads


class ByGoals(SquadBuilder):
    def build(self, heros):
        dic_squads = {}
        for g in Goals:
            squad_heros = []
            for hero in heros:
                if g in hero.goals:
                    squad_heros.append(hero)
            if len(squad_heros) > 0:
                squad_name = f"Squad {str(g.index)}"
                squad = Squad(squad_name, g, hl=squad_heros)
                dic_squads[squad_name] = squad
        return dic_squads


class OutOfBoxSquads(SquadBuilder):


    def build(self, heros):
        dic_squads = {}
        for squad_name, goal in out_of_box_squads.items():
            squad_heros = [hero for hero in heros if goal in hero.goals]
            squad = Squad(squad_name, goal, hl=squad_heros)
            dic_squads[squad_name] = squad
        return dic_squads

