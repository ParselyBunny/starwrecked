# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    def robin_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/voice1.mp3", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def fridai_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/voice2.mp3", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")


define r = Character("Robin", callback=robin_beep)
define f = Character("FrIDAI", callback=fridai_beep)

image robin:
    "robin-default"

image robin smile:
    "robin-smile"

# The game starts here.

label start:

    

    scene bg beach
    pause 3
    show robin at right with dissolve
    pause 2

    r "Ugh..."
    r "I survived the crash?"
    r "Where am I? What planet is this?"
    r "FrIDAI? Your circuits still ticking?"

    f "..."
    f "--__--____---____"
    f "Central core reboot successful. Damage levels: critical."

    show robin smile
    r "There you are, you bucket of bolts!"
    show robin
    r "What happened? Why'd we crash?"

    f "Unknown. I have lost access to 99 per cent of my data storage."   
    return
