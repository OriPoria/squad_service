class Service:
    def __init__(self, ft, hl):
        self.fight_type = ft
        self.heros_list = hl
        self.squads = {}

    def build_squads(self, squads_builder):
        self.squads = squads_builder.build(self.heros_list)

    def print_all_squads(self):
        for sn in self.squads.keys():
            s = self.squads[sn]
            print(s.str_squad())
            print("Heros:")
            for h in s.heros:
                print("\t" + h.str_hero() + "\n")

    def fight(self, squad_a, squad_b):
        if len(list(set(squad_a.heros).intersection(set(squad_b.heros)))) > 0:
            print("Impossible to have a fight due to heros in both squads")
            return None
        print(f"Fight is starting: {squad_a.name} vs. {squad_b.name}")
        squad_a.in_action = True
        squad_b.in_action = True
        winner_squad = self.fight_type.fight(squad_a, squad_b)
        print("Winner squad in fight", winner_squad.name)
        squad_a.in_action = False
        squad_b.in_action = False

        return winner_squad
