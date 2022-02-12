# cse210_jumper_game
Jumper game for CSE210

## Jumper
Are you good at solving puzzles then Jumper is a good game for you to play.The game play for this game is simple.A puzzle is a randomly chosen word which a player guesses the letters of the secret puzzle.The game has 5 lives and if a player guesses the letters correctly the secret puzzle word is revealed and you win with a display message showing you won. If you guess the letters wrong ,the lines on the parachute are cut until you are left with none and it will be game over with you lose message displaying on the screen.If you also guess wrong you lose lives and if you lose all lives it will be gameover.

## Getting started

---
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 jumper
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the Jumper folder and click the "run" button.

## Project Structure

---

The project files and folders are organized as follows:

```
root                    (project root folder)
+-- jumper               (source code for game)
  +-- game              (specific classes)
    +-- matcher.py        (class called by director.py)
    +-- sketcher.py      (classes called by director.py and matcher.py)
    +-- terminal.py     (classes called by director.py and sketcher.py)
    +-- director.py     (Class called by main.py)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```
## Required Technologies

---

- Python 3.8.0

## Authors

---

- McNeill Chimuka Chimuka
- Miguel Angel Condori
- Emediong Henry Edet
- Mary Ann Overson
- Miguel Secades Garcia




