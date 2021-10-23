import copy
from hero import Hero, Goals
from hero_data import Attributes, WeaponsObject, weapons_pool


out_of_box_squads = {
    'Ninja Turtles': Goals.EAT,
    'The Avengers': Goals.REVENGE,
    'The X-Men': Goals.PEACE
}
def create_heros_pool():
    spiderman_att = Attributes(aviation=False,strength=6.3,agility=8,popularity=9)
    spiderman = Hero("Spider-Man", 8.5, spiderman_att)
    spiderman.set_weapons(WeaponsObject([weapons_pool['Web-Shooter']]))
    spiderman.set_goals([Goals.BETTER, Goals.LAUGH, Goals.REST, Goals.PEACE])

    wonderwoman = Hero("Wonder Woman",7.2, Attributes(aviation=False,strength=5.4,agility=7,popularity=8))
    wonderwoman.set_weapons(WeaponsObject([weapons_pool['Fireproof-Bracelet'],weapons_pool['Shield']]))
    wonderwoman.set_goals([Goals.BETTER,Goals.LAUGH])

    batman = Hero("Batman", 8.2, Attributes(aviation=True,strength=6.4,agility=5,popularity=9))
    batman.set_weapons(WeaponsObject([weapons_pool['Batarang']]))
    batman.set_goals([Goals.BETTER,Goals.KILL,Goals.DESTROY,Goals.PEACE])

    ironman = Hero("Iron Man", 9.12, Attributes(aviation=False,strength=9.4,agility=6,popularity=4))
    ironman.set_weapons(WeaponsObject([weapons_pool['Armor-Suit']]))
    ironman.set_goals([Goals.KILL,Goals.BETTER,Goals.DESTROY,Goals.REVENGE,Goals.SAVE,Goals.EARTHQUAKE])

    captainamerica = Hero("Captain America", 5, Attributes(aviation=False,strength=7.4,agility=8,popularity=4))
    captainamerica.set_weapons(WeaponsObject([weapons_pool['Armor-Suit'], weapons_pool['Shield']]))
    captainamerica.set_goals([Goals.BETTER,Goals.DESTROY,Goals.REST,Goals.REVENGE,Goals.SAVE])

    aquaman = Hero("Aquaman", 4.5, Attributes(aviation=False,strength=4.5,agility=5,popularity=3))
    aquaman.set_weapons(WeaponsObject([weapons_pool['Trident of Poseidon']]))
    aquaman.set_goals([Goals.KILL,Goals.BETTER,Goals.LAUGH,Goals.PEACE,Goals.TSUNAMI])

    hulk = Hero("Hulk", 6.9, Attributes(aviation=False,strength=8.9,agility=4,popularity=6))
    hulk.set_goals([Goals.KILL,Goals.DESTROY,Goals.REVENGE,Goals.SAVE])

    groot = Hero("Groot", 5, Attributes(aviation=False,strength=4,agility=8.3,popularity=3))
    groot.set_goals([Goals.KILL,Goals.BETTER,Goals.LAUGH])

    ninja_weapons = WeaponsObject([weapons_pool['Ninjato']])
    ninja_attributes = Attributes(aviation=False, strength=6.5, agility=1, popularity=5)
    NINJA_POWER = 7
    leonardo = Hero("Leonardo", NINJA_POWER, copy.copy(ninja_attributes))
    leonardo.set_weapons(copy.copy(ninja_weapons))
    leonardo.set_goals([Goals.EAT, Goals.KILL])
    refael = Hero("Refael", NINJA_POWER, copy.copy(ninja_attributes))
    refael.set_weapons(copy.copy(ninja_weapons))
    refael.set_goals([Goals.EAT])
    donatelo = Hero("Donatelo", NINJA_POWER, copy.copy(ninja_attributes))
    donatelo.set_weapons(copy.copy(ninja_weapons))
    donatelo.set_goals([Goals.EAT])
    michaelangelo = Hero("Michaelangelo", NINJA_POWER, copy.copy(ninja_attributes))
    michaelangelo.set_weapons(copy.copy(ninja_weapons))
    michaelangelo.set_goals([Goals.EAT])

    deadpool = Hero("Deadpool", 8.3, Attributes(aviation=False,strength=8,agility=9,popularity=4))
    deadpool.set_weapons(WeaponsObject([weapons_pool['Ninjato'],weapons_pool['Sword']]))
    deadpool.set_goals([Goals.KILL,Goals.DESTROY,Goals.REST])

    return [spiderman,wonderwoman,batman,ironman,captainamerica,aquaman,
              hulk,groot,leonardo,refael,donatelo,michaelangelo,deadpool]