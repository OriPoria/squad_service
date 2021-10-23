from abc import ABCMeta, abstractmethod
import random
import math

class FightType(metaclass=ABCMeta):
    def delete_deaths(self, sq_a, sq_b):
        sq_a.heros[:] = [hero for hero in sq_a.heros if hero.is_alive]
        sq_b.heros[:] = [hero for hero in sq_b.heros if hero.is_alive]

    # Returns the winner squad
    @abstractmethod
    def fight(self, squad_a, squad_b):
        pass

    @abstractmethod
    def update_heros_popularity(self, winner, loser):
        pass


class SimpleFight(FightType):
    def fight(self, squad_a, squad_b):
        power_a_sum = sum(hero.get_power() for hero in squad_a.heros)
        power_b_sum = sum(hero.get_power() for hero in squad_b.heros)
        if (power_a_sum > power_b_sum):
            return squad_a
        return squad_b

    def update_heros_popularity(self, winner, loser):
        pass

HERO_DAMAGE = 10

class OneVsOne(FightType):
    def __init__(self, single_fight_metric):
        self.single_fight_metric = single_fight_metric

    def update_heros_popularity(self, winner, loser):
        if (winner.is_good and loser.is_good) or (winner.is_good != True and loser.is_good != True):
            winner.attributes.popularity += 1
        elif winner.is_good and loser.is_good != True:
            winner.attributes.popularity += 2
        elif winner.is_good != True and loser.is_good:
            winner.attributes.popularity -= 1
    def print_single_fight(self, hero_a, hero_b):
        print(f"{hero_a.name} vs {hero_b.name}")
        print("\tHeros power:")
        print(f"\t{hero_a.name}: {hero_a.get_power()}")
        print(f"\t{hero_b.name}: {hero_b.get_power()}")


    def fight(self, squad_a, squad_b):
        while (len(squad_a.heros) > 0 and len(squad_b.heros) > 0):
            random.shuffle(squad_a.heros)
            random.shuffle(squad_b.heros)
            for hero_a, hero_b in zip(squad_a.heros, squad_b.heros):
                self.print_single_fight(hero_a, hero_b)
                winner, loser = self.single_fight_metric(hero_a, hero_b)
                print("Winner:", winner.name)
                loser.inc_injury_deg(HERO_DAMAGE)
            self.delete_deaths(squad_a, squad_b)
        if (len(squad_b.heros) > 0):
            return squad_b
        return squad_a

SQUAD_DAMAGE = 2

class AllVsAll(FightType):
    def __init__(self, squad_pow_met):
        self.squad_power_metric = squad_pow_met

    def update_heros_popularity(self, winners, losers):
        good_death = 0
        bad_death = 0
        for h in losers.heros:
            if h.is_alive is False:
                if h.is_good:
                    good_death += 1
                else:
                    bad_death += 1
        popularity_change = bad_death - good_death
        if popularity_change != 0:
            for h in winners.heros:
                old_good = h.is_good
                h.attributes.popularity += popularity_change
                if (h.is_good and old_good is False):
                    print(f"{h.name} is now good")
                elif h.is_good is False and old_good:
                    print(f"{h.name} is now bad")

    def fight(self, squad_a, squad_b):
        while len(squad_a.heros) > 0 and len(squad_b.heros) > 0:
            squad_a_power = self.squad_power_metric(squad_a)
            squad_b_power = self.squad_power_metric(squad_b)
            if squad_a_power < squad_b_power:
                [h.inc_injury_deg(SQUAD_DAMAGE) for h in squad_a.heros]
                self.update_heros_popularity(squad_b, squad_a)
            else:
                [h.inc_injury_deg(SQUAD_DAMAGE) for h in squad_b.heros]
                self.update_heros_popularity(squad_a, squad_b)
            self.delete_deaths(squad_a, squad_b)
        if len(squad_b.heros) > 0:
            return squad_b
        return squad_a

def single_fight_random(hero_a, hero_b):
    hero_a_power = hero_a.get_power()
    hero_b_power = hero_b.get_power()
    power_a_fraction = hero_a_power / (hero_a_power+hero_b_power)
    fight_val = random.uniform(0.0, 1.0)
    if fight_val < power_a_fraction:
        return hero_a, hero_b
    return hero_b, hero_a

def single_fight(hero_a, hero_b):
    hero_a_power = hero_a.get_power()
    hero_b_power = hero_b.get_power()
    if hero_a_power > hero_b_power:
        return hero_a, hero_b
    return hero_b, hero_a

# Evaluate the power of all squad. reduce the power if the squad is not homogeneous
def squad_power_metric(squad):
    total_power = 0
    good_heros = 0
    weapons = {}
    for h in squad.heros:
        if (h.is_good == True):
            good_heros += 1
        total_power += h.get_power()
        if h.weapons_object is not None:
            for w in h.weapons_object.weapons_list:
                if w in weapons:
                    weapons[w] += 1
                else:
                    weapons[w] = 1
                    total_power += w.attack_power+w.defense_power
    penalty = normpdf(good_heros/len(squad.heros),0.5,0.1)*5
    total_power -= penalty
    return total_power

def normpdf(x, mean, sd):
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom
