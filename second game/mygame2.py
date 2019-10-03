from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    pass

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suckt at this.",
        "Your Mom would be proud... if she were smarter.",
        "Such a looser",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        The Mauzi's from Plant Gurr-Aeehh-Gurr have invaded
        your space ship and killed your entire crew.
        You are the last Surviving member of the Boss-Bitch-Alliance
        and your last mission is to get the vacuum cleaner
        bom from the Weapon's Armory of the ship, put it to
        the bridge where whe Mauzi's sleep, so that they run away.

        You're running down the central corridor to the Weapon's Armory
        when a Mauzi jumps out, black shiny fur, skin coloured
        jellybeans, big pony nose and puuuuh....smelly breath
        ....it 'Gurrs', is angry and is blocking the door to Armory.
        It is also to pull a claw to kill you. """))


    action = input("> ")

    if action == "help":
        #help_list = [
        #"fight",
        #"smooth",
        #"touch butthole"
        #]
        #print("help_list")
        return 'central_corridor'

    elif action == "fight":
        print(dedent("""
            You are trying to fight with the Gurr-Mauzi.
            But you were not able to know, that she hasn't
            just black shiny fuur, she has also a Black Belt
            in Mauz-Fu. You have no chance! """))
        return 'death'

    elif action == "smooth":
        print(dedent("""
            Nice try, but its not the Gurr-Gurr-Buoy from the
            last game. The Gurr-Mauzi makes exactly the same
            sounds, looks exactly the same and likes the same thing.
            But this time you gonna loose with smoothing
            in fact of her very bad smelly breath!!!"""))
        return 'death'

    elif action == "touch butthole":
        print(dedent("""
            Sure...you 'dont' like this.  But it seems
            that the Gurr-Mauzi is getting smooth.
            Seem's that she fall a sleep, so you can jump
            to the Weapon Armory door. """))
        return 'weapon_armory'

    else:
        print("DOES NOT COMPUTE")
        return 'central_corridor'

class WeaponArmory(Scene):
### here i need to continue with the WeaponArmory room
    def enter(self):
        print(dedent("""You jump into the Weapon Armory. You scan the room and
            oh no! These is a bomb! it counts.... you need to enter the 6-digit
            code. Remember... the code is the date of the greatest treasure
            in the world."""
            ))
        code = "051188"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 3:
            print("BZZZZEEEDDDD")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                """))
            return 'death'






### this creates the map of the game
class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'WeaponArmory': WeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
