# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Cassidy", color="#c8ffc8")
define j = Character("Jessica", color="#c8ffc8")


# The game starts here.

label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene prettybackground

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    c "You've created a new Ren'Py game."

    c "Once you add a story, pictures, and music, you can release it to the world!"

    "Sylvie" "Hi there! How was class?"

    "Me" "Good..."

    "I can't bring myself to admit that it all went in one ear and out the other."

    "Me" "Are you going home now? Wanna walk back with me?"

    menu:

        "It's a videogame.":
            jump game

        "It's an interactive book.":
            jump book

    label game:

        c "It's a kind of videogame you can play on your computer or a console."

        jump marry

    label book:

        c "It's like an interactive book that you can read on a computer or a console."

        jump marry

    label marry:

        "And so, we become a visual novel creating duo."

    # This ends the game.

    return
