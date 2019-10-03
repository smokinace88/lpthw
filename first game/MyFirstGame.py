import time
from sys import exit

# defines the access to boss-bith Door, if trunk len 2 then it will open
trunk = []
xtrunk = len(trunk)

#definition of boss_bitch_oase
def boss_bitch_oase():
    time.sleep(2)
    print("You opened successfull the Boss-Bitch Door")
    time.sleep(2)
    print("There is some sound.....")
    time.sleep(2)
    print("what is that?")
    time.sleep(2)
    print("Its the Fruity-Boss-bitch!!!! and she is very hungry and grumpy")
    choice = input("> ")
    if "feed" in choice:
        time.sleep(2)
        print("Seems like she get's a better mood and she want's to start the Boss-Bitch Karaoke Show")
        print("which song should she sing ?")
        choice_two = input("> ")
        if "happy" or "Happy" in choice_two:
            time.sleep(2)
            print("Damn right, its a happy ending, you won the game!")
            exit(0)
        else:
            dead("She hate's it!")
    else:
        print("She is getting in Rage mode!")
        time.sleep(2)
        print("She is unstoppable!!!!!")
        dead("She killed you!")




#definition of gurr_gurr_malone
def gurr_gurr_malone():
    print("You are entering Room")
    time.sleep(2)
    print('"Gurr....Gurr...." what is it?')
    time.sleep(2)
    print("Oh no! It's a Gurr-Gurr-Buoy")
    time.sleep(2)
    print("Funfact... she is something like a biporal Pony")
    time.sleep(2)
    print("What do you do? hink: fight or smooth")

    choice = input("> ")
    if "fight" in choice:
        time.sleep(2)
        dead("She is stronger")
    elif "smooth" in choice:
        time.sleep(2)
        print("She likes it, whats next? smooth or run away?")
        choice = input("> ")
        if "smooth" in choice:
            dead('She is getting in Rage-Mode,"I fuck the whole world his mother!!!"')
        else:
            item = "Gurr_Gurr_Shield"
            trunk.append(item)
            time.sleep(2)
            print("She likes the way you are and transforms to a Smoothie-Lussie")
            print(f"You got the {item}")
            beatles_place_two()


    else:
        print("one more chance, choose the correct option")
        gurr_gurr_malone()


#definition of mauzis_showbar
def mauzis_showbar():
    print("You are arriving at Mauzi's Showbar")
    time.sleep(2)
    print('Everywhere is music, you hear "Hey Mauziorita...""')
    time.sleep(2)
    print('But then the Mouse Bear arrives! AAAAEEEEEHH!')
    time.sleep(2)
    print("What now ? You need to find the chickenhearts to satisfy the Mauziorita")
    time.sleep(2)
    print("""Where do you want to yearch ?
    1. Mauztease table ?
    2. Mauz-kini-hall ?
    3. Lovers Shower
    4. Good-Human-Lounge
    5. Mauzibert Bar
    6. Mauzsagge Room""")

    for count in range(5):
        choice = input("> ")
        if choice != "Good-Human-Lounge":
            print("Try one more time")
        else:
            item = "AAAAEEEEEHH_Sword"
            trunk.append(item)
            time.sleep(2)
            print('Mousebear is dancing for you in hear Mauzkini "Hey Mauziorita..."')
            time.sleep(2)
            print("You got the AAAAEEEEEHH_Sword")
            beatles_place_two()
    else:
        dead("Mausebear transforms to Mauzibert and is killing you")




#definition of fall_in_darkness
def fall_in_darkness():
    print("There is loud music")
    time.sleep(2)
    print("Seems like a goal, is it a win ?")
    time.sleep(2)
    dead("It was a trap")


# return to the beatles place after finishing one Room
def beatles_place_two():
    print("You are back at the beatles place")
    time.sleep(2)
    print("Which way now?")
    if "Gurr_Gurr_Shield" not in trunk:
        print("Now go right")
    elif "AAAAEEEEEHH_Sword" not in trunk:
        print("Now go left")
    else:
        print("Open the boss bitch door")
    direction = input("> ")
    if direction == "left":
        mauzis_showbar()
    elif direction == "right":
        gurr_gurr_malone()
    elif direction == "open":
        boss_bitch_oase()
    else:
        beatles_place_two()




#definition of sound direction
def sound_dir():
    print("along the small street is something")
    time.sleep(2)
    print("The Boss-Bitch Door .... sounds a bit like Karaoke")
    time.sleep(2)
    print("from the left you can hear an:'Aaaeeehh!!!'")
    time.sleep(2)
    print("from the right side you hear 'Gurr Gurr'")
    time.sleep(2)
    print("just from the straight you hear Black music, jump to activate")


    choice = input("> ")
    if choice == "straight" and xtrunk == 2:
        boss_bitch_oase()
    elif choice == "straight" and xtrunk == 1:
        print("You need both items")
        sound_dir()
    elif choice == "straight" and xtrunk == 0:
        print("You need a Weapon and a Shield to open the door")
        sound_dir()
    elif "left" in choice:
        mauzis_showbar()
    elif "right" in choice:
        gurr_gurr_malone()
    elif "jump" in choice:
        fall_in_darkness()
    else:
        sound_dir()

#definition of start place
def beatles_place():
    print("You are starting in the middle of the dungeon")
    time.sleep(2)
    print("*")
    time.sleep(2)
    print("**")
    time.sleep(2)
    print("***THE BEATLES PLACE***")
    time.sleep(2)
    sound_dir()

def dead(why):
    print(why, "You fuck'ed it up")
    exit(0)

# definition of start codeblock
def start():
    print("\n\n\n\n...long long time ago...")
    time.sleep(2)
    print("....there was a sinfull Dungeon....")
    time.sleep(2)
    print("...this place was waiting for a hero...")
    time.sleep(2)
    print("...this is your time!\n")
    time.sleep(2)
    beatles_place()


# this block will start the code
start()
