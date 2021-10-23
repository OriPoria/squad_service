# Squad Service
Create squads of heros and make a fight between 2 squads

## How to use
First there is an interface for the user to create 2 squads, with any number of 
new heros that you want. The object of the type of the fight is default.
Pay attention that you cannot insert 2 squads with the same name.
We assume that user enters valid values, as requested.
After that you played with your own values, you get a demonstration of the 
out-of-the-box values in the program, with built-in heros, and 3 ways to divide 
them into squads.
## Structure explanation
Service class has an interface of type Fight-Type that has the method "fight" 
and there are 2 implementations of this interface- OneVsOne fight and AllVsAll.
Squads contain list of heros, and they can be in-active or in rest.
Hero can be live or dead. It can be injured, and while its injured degree is 
less than 100 it is alive. It Has an object of attributes that it hold its
fight abilities and popularity rating that defines if it is good or bad.
During the fight it can become good or bad, depends who it is and who it killed.
Hero also holds an optional weapon object. We used flyweight DP, and the weapon
object of each hero holds a reference to the weapons pool.