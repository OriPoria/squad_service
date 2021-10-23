from dataclasses import dataclass
from typing import NamedTuple

class WeaponsObject:
    def __init__(self, wl):
        self.weapons_list = wl
    def attack_power(self):
        return sum(w.attack_power for w in self.weapons_list)
    def defense_power(self):
        return sum(w.defense_power for w in self.weapons_list)
    def add_weapon(self,w):
        self.weapons_list.append(w)
    def str_weapon_obj(self):
        result = ""
        for w in self.weapons_list:
            result += f"{w.name}, "
        result = result [:-2]
        return result
class Weapon(NamedTuple):
    name: str
    attack_power: float
    defense_power: float
    transferable: bool

@dataclass
class Attributes:
    aviation: bool
    strength: float
    agility: float
    popularity: int
    def str_att(self):
        return f"Aviation={self.aviation}, Strength={self.strength}, Agility={self.agility}, Popularity={self.popularity}"

shield = Weapon(name="Shield",attack_power=1,defense_power=9.5,transferable=True)
sword = Weapon(name="Sword",attack_power=7,defense_power=2,transferable=True)
webshooter = Weapon(name="Web-Shooter",attack_power=9.5,defense_power=1,transferable=False)
fireproofbracelet = Weapon(name="Fireproof-Bracelet",attack_power=0,defense_power=9.4,transferable=True)
batarang= Weapon(name="Batarang",attack_power=7,defense_power=3.4,transferable=True)
armorsuit = Weapon(name="Armor-Suit",attack_power=1,defense_power=10,transferable=False)
trident = Weapon(name="Trident of Poseidon",attack_power=6.5,defense_power=4,transferable=True)
ninjato = Weapon(name="Ninjato", attack_power=6.7, defense_power=2, transferable=True)
weapons_pool = {
    shield.name: shield,
    sword.name: sword,
    webshooter.name: webshooter,
    fireproofbracelet.name: fireproofbracelet,
    batarang.name: batarang,
    armorsuit.name: armorsuit,
    trident.name: trident,
    ninjato.name: ninjato
}