from service import Service
from squad_builder import OutOfBoxSquads, ByGoals
from fight_type import *
from heros_pool import create_heros_pool
from hero import Hero, Goals
from hero_data import Attributes, weapons_pool, WeaponsObject
from squad import Squad

def first_presentaion():
    print("First presentaion:")
    heros = create_heros_pool()
    create_squads_by_common_goals = ByGoals()
    my_service = Service(OneVsOne(single_fight), heros )
    my_service.build_squads(create_squads_by_common_goals)
    my_service.print_all_squads()

    first_squad = my_service.squads['Squad 5']
    second_squad = my_service.squads['Squad 6']
    my_service.fight(first_squad,second_squad)

    first_squad = my_service.squads['Squad 5']
    second_squad = my_service.squads['Squad 7']
    my_service.fight(first_squad,second_squad)

def second_presentation():
    heros = create_heros_pool()
    print("Second presentation:")
    out_of_box_squads_builder = OutOfBoxSquads()
    my_service = Service(AllVsAll(squad_power_metric), heros)
    my_service.build_squads(out_of_box_squads_builder)
    my_service.print_all_squads()

    fight_list = []
    for s in my_service.squads:
        fight_list.append(my_service.squads[s])
    my_service.fight(fight_list[0], fight_list[1])
    print("Squads status:")
    for k,s in my_service.squads.items():
        print(f"{s.name} has " + str(len(s.heros)) + " heros")
    print("")
    my_service.fight(fight_list[0], fight_list[2])
    print("Squads status:")
    for k,s in my_service.squads.items():
        print(f"{s.name} has " + str(len(s.heros)) + " heros")


def create_squad(num):
    print(f"Choose the name of the {num} squad")
    name = input("Enter a name: ")
    print("Choose the goal of the squad (by index)")
    my_enums = []
    for enum in Goals:
        my_enums.append(enum)
    for enum in Goals.list():
        print(enum)
    goal = input()
    goal = my_enums[int(goal) - 1]
    squad = Squad(name, goal)
    return squad

def create_attributes():
    print("Set the hero's attributes")
    aviation = input("If it has aviation ability press 1, else press 2: ")
    if aviation == "1":
        aviation = True
    else:
        aviation = False
    stre = float(input("set strength skill (0-10) "))
    agil= float(input("set agility skill (0-10) "))
    pop= int(input("set popularity skill (0-10) "))
    return Attributes(aviation,stre,agil,pop)


def create_hero():
    name = input("Choose hero's name ")
    att = create_attributes()
    pow = float(input("Choose hero's power (0-10)"))
    hero = Hero(name, pow, att)
    print("Choose hero's weapons ")
    weapons_list = []
    i = 0
    for k,v in weapons_pool.items():
        weapons_list.append(k)
        print(str(i+1), k)
        i+=1
    wep_idx = int(input())
    wo = WeaponsObject([weapons_pool[weapons_list[wep_idx-1]]])
    hero.set_weapons(wo)
    return hero

def create_heros():
    heros = []
    while (True):
        h = create_hero()
        heros.append(h)
        another_hero = input("Do you want to add another? (Y/N)")
        if another_hero.upper() == "N":
            break
    return heros

def custom():

    print("Let's start create the squads!")
    squad_a = create_squad("first")
    print("Build squads' heros")
    heros_a = create_heros()
    squad_a.add_all(heros_a)
    print(squad_a.str_squad())
    squad_b = create_squad("second")
    heros_b = create_heros()
    squad_b.add_all(heros_b)
    print(squad_b.str_squad())

    ans = input("Do you want to start a fight? (Y/N) ")
    if ans.upper() == "Y":
        service = Service(OneVsOne(single_fight_random),[squad_a,squad_b])
        winner = service.fight(squad_a,squad_b)

def main():
    while True:
        custom()
        ans = input("Do you want to create new fight? (Y/N) ")
        if ans.upper() == "N":
            break
    print("Thank you for playing the game, let's look at some build-in fights:")
    first_presentaion()
    print("\nEnd of first presentation\n")
    second_presentation()


if __name__=="__main__":
    main()
