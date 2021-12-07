import sys
import time
from typing import List, Optional


class Event:
    def __init__(self, text: List[str], choices: List[str],
                 next_events: Optional[List['Event']], parent: Optional['Event']):
        self.text = text
        self.choices = choices
        self.next_events = next_events
        self.parent = parent

    def play(self):
        print("* ----------------- *")
        for line in self.text:
            time.sleep(0.4)
            print(line)
        print()

        print(f"Choices: ", end="")
        for idx, choice in enumerate(self.choices):
            print(f"         {idx}; {choice}")
        print()

        if not self.choices:
            input("press [enter] to exit")
            sys.exit()

        choice = 1232
        while 0 <= choice < len(self.choices):
            choice = input("Your choice: ")

            if not choice.isdigit():
                print("~enter a number~")
                choice = 1232
            else:
                choice = int(choice)

        self.next_events[choice].play()


intro = ["You have boarded an airplane just like any other time.",
         "It takes off, no problem.",
         "As you fly over a group of islands, you hear your captain speaking:",
         "\"Dear passengers, I regret to inform you, but the plane ",
         "is having unexpected difficulties concerning three out of four engines.",
         "This may be the best time to call your family.\"",
         "As if on cue, there is a sudden bang, as one of the engines rips itself to shreds.",
         "The plane starts to dip towards the ground ..",
         "", "GOAL: escape the island", ""]

# TODO link all events after all are declared, add pictures
# TODO: decompose logic and events into separate files


waking_up = Event(["You wake up.",
                                "It is quiet, it seems you are the only survivor.",
                                "You notice that your arm is bleeding.",
                                "If you do not stop the bleeding, you may bleed out.",
                                "You see a glowing hot piece of metal, and a first-aid kit nearby"],
                               ["Cauterize the wound with the hot piece of metal",
                                "Patch it up using the first aid kit"], [], None)

fainting_and_dying = Event(["As you press the piece of metal against the wound,",
                                "the pain turns your mind blank and you lose consciousness.",
                                "The wound was not yet sealed properly.",
                                "You have died .."], [], None, None)

bandaging = Event(["You bandage your arm, it seems to have helped tremendously.",
                     "What now?"],
                    ["Explore the island along the shore",
                     "Explore the island - head inland"], [], None)

its_getting_dark = Event(["So far you have found nothing of interest.",
                    "It is getting dark very fast, and you see a glimmer of light in the distance.",
                    "Or is it your mind playing tricks?"],
                   ["Set up a shelter for the night",
                    "Go towards the light"], [], None)

making_shelter = Event(["You wake up in your shelter,",
                          "but you notice that you seem to be missing a kidney.",
                          "There is a line of stitches just where your kidney should have been,",
                          "and it hurts quite a bit.",
                          "You notice footprints in the soft soil."],
                         ["Follow the footprints",
                          "Do not follow the footprints, go in a different direction"], [], None)

following_footprints = Event(["You follow the footprints for quite a while.",
                         "Finally, you notice a large field of what seems like marijuana, tall as a person.",
                         "There are guards patrolling the edges of the field.",
                         "Behind the field there are several buildings, and one as big as a plane hangar"],
                        ["Sneak by the guards into the field",
                         "Pacify a guard and take his equipment"], [], None)

pacify_guard = Event(["You ambush one of the patrolling guards.",
                           "In the struggle you get shot several times as you have no training",
                           "You have died .."], [], [], None)

sneaks_in = Event(["You sneak into the field when no one can see you.",
                       "The wound, where your kidney was, starts to hurt quite considerably."],
                      ["Make a joint and continue",
                       "Do not make a joint and continue"], [], None)

no_joint = Event(["You choose not to make a joint.",
                          "The spiking pain grows in intensity,",
                          "to the point where you are not able to suppress a scream.",
                          "You hear barking of dogs, it gets closer and closer by the second.",
                          "You are devoured by a pack of hounds.",
                          "You have died .."], [], [], None)

makes_joint = Event(["You decide to roll a joint from the plants around you.",
                        "The pain fades away, as if it was never there.",
                        "From there you continue into the nearest building.",
                        "It seems to be a dressing room for the mercenaries working there.",
                        "There are several sets of extra uniforms and other gear"],
                       ["Dress as a guard",
                        "Do not dress a guard, continue as you are now"], [], None)

doesnt_change_clothes = Event(["As you try to exit the room, another guard sees you.",
                        "You are executed.",
                        "You have died .."], [], [], None)

changes_clothes = Event(["You dress up as a guard. You fit in quite well.",
                      "As you take a look around, a man orders you",
                      "to execute a slave that has not fulfilled his quota.",
                      "He looks to be the chief around here."],
                     ["Comply", "Refuse, give alternate options."], [], None)

refuses = Event(["You have chosen to refuse the order you have been given",
                         "and you give alternate solutions.",
                         "You are executed on basis of disobedience",
                         "You have died .."], [], [], None)

complies = Event(["You have complied with the order, executing the slave.",
                       "You are given a pass to go home for the weekend directly by the chief.",
                       "YOU HAVE WON", "",
                       "~but at what price?"], [], [], None)

follows_the_light= Event(["You decide to follow the shimmering light in the distance.",
                        "On the way, you stumble across a patch of magic mushrooms."],
                       ["Eat some",
                        "Leave them be"], [], None)

doesnt_eat_shroom = Event(["As you get closer to the light, there seem to be some buildings there.",
                          "On what looks like a small runway is a small plane,",
                          "it doesn't look like it is in the best condition."
                          "Several people are strolling about"],
                         ["Sneak onto the plane and hide",
                          "Ask one of the people there for help"], [], None)

asks_for_help = Event(["You decide to ask one of the people there for help.",
                         "They look like mercenaries and take you to their headquarters.",
                         "You are questioned and ultimately shot on basis of",
                         "being a spy or working with the government.",
                         "You have died .."], [], [], None)

infiltrate_plane = Event(["You decide to infiltrate the plane.",
                             "It goes without problems, and you hide among the cargo of plastic-wrapped packages.",
                             "Soon enough, the plane takes off.",
                             "Several minutes after takeoff you smell smoke.",
                             "The plane starts to dip towards the ground .."], [], [], None)  # ->preberie_sa_z_lietadla

eats_shroom = Event(["You take and eat half a basket worth of mushrooms.", "",
                        "You have entered the world of fantasy and wonder.",
                        "You see a fat dragon to your left and a skinny griffin to your right"],
                       ["Go towards the dragon",
                        "Go towards the griffin"], [], None)

goes_to_griffin = Event(["You decide to go towards the griffin.",
                          "It looks very skinny, as if it hasn't eaten in quite some time.",
                          "You are eaten by the griffin.",
                          "You have died .."], [], [], None)

goes_to_dragon = Event(["You decide to go towards the dragon.",
                       "The dragon tells you that he will eat you unless you answer his riddle correctly.",
                       "<If you had five mangoes and two bananas in one hand and two mangoes and four bananas",
                       "in the other hand, what would you have?>"],
                      ["Very large hands",
                       "Seven mangoes and six bananas"], [], None)

counts_it = Event(["You have given your answer.",
                    "The dragon looks displeased by your answer.",
                    "You are eaten by the dragon",
                    "You have died .."], [], [], None)

correct_answer = Event(["You have given your answer.",
                         "The dragon looks pleased by your answer and lets you go onward.",
                         "Soon, a pixie approaches you.",
                         "She offers you some pixie dust. ",
                         "She claims it will teleport you home. Will you accept?"],
                        ["Accept", "Decline"], [], None)

doesnt_take_pixie_dust = Event(["You decline the offfer.",
                              "As soon as you do, the pixie and all other fantastical beasts",
                              "around you start to disappear.",
                              "", "You are surrounded by a tribe of indigenous people."],
                             ["Surrender",
                              "Try to escape"], [], None)

tries_to_escape_tribesmen = Event(["You try to escape the tribe.",
                                "There is just too many of them, and your struggle is meaningless.",
                                "You tried to run, and according to the local custom, you are eaten.",
                                "You have died .."], [], [], None)

doesnt_try_to_escape = Event(["You have surrendered to the tribe.",
                           "You are crowned their king, according to the local custom.",
                           "You soon realize that the tribe has some customs that are a bit controversial."],
                          ["Try to reform their customs",
                           "Leave the customs as they are"], [], None)

doesnt_change_customs = Event(["You have decided not to change their customs.",
                          "During full moon you are offered to their gods as a sacrifice.",
                          "You have died .."], [""], [], None)

changes_customs = Event(["You have changed their traditions, but it was not easy.",
                        "You are to remain their king for the rest of your life.",
                        "YOU HAVE PARTIALLY WON"], [], [], None)

takes_pixie_dust = Event(["As you take the pixie dust, two roads appear before you.",
                            "One looks like a road of death and heads underground.",
                            "The other is a road made of rainbow and stretches into the sky"], [""], [], None)

death_road = Event(["You have chosen the road of death.",
                     "As you step on it, you die.",
                     "You have died .."], [], [], None)

rainbow_road = Event(["You approach the rainbow road.",
                      "As you get closer, you notice that Death is blocking your path.",
                      "It offers you a black hole flavored ice-cream"],
                     ["Accept",
                      "Ask for gluten-free ice-cream cone"], [], None)

asks_for_glutenfree = Event(["You ask Death for gluten-free ice-cream cone.",
                                "Death grabs his scythe",
                                "You notice that your head is not connected to your body anymore.",
                                "You have died .."], [], [], None)

accepts_icecream = Event(["As you accept the ice-cream, it starts to change shape and expand,",
                         " morphing into a fabulous unicorn."],
                        ["Mount the unicorn",
                         "Say <eew, I dont like unicorns!>"], [], None)

doesnt_like_unicorns = Event(["As you say that, your chest is impaled by the unicorn.",
                             "You are now a decoration on the unicorn's head.",
                             "You have died .."], [], [], None)

mounts_the_unicorn = Event(["You mount the unicorn.",
                               "You take off on the rainbow road towards a brighter future.",
                               "YOU HAVE WON"], [], [], None)

for i in intro:
    print(i)
    time.sleep(0.4)

preberie_sa_z_lietadla.play()
