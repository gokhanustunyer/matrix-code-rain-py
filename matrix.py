from tkinter import *
import random

letterLst = "	Γ	Δ	Ζ	Η	Θ	Ι	Κ	Λ	Μ	Ν	Ξ	Ο	Π	Ρ	Σ	Τ	Υ	Φ	Χ	Ψ	Ωα	β	γ	δ	ε	ζ	η	θ	ι	κ	λ	μ	ν	ξ	ο	π	ρ	σς	τ	υ	φ	χ	ψ	ω"
letterLst = letterLst.split()

WIDTH = 1366
HEIGHT = 768
SPACE_SIZE = 25
FONT_SIZE = 18
RAIN_SPEED = 40
SPAWN_COULMN_RATE = 80
FONT_FACE = "matrixcodenfi"
LINE_DISTANCE = int(FONT_SIZE / 3)

selectedCoordinates = []

colors = ['#00ff00', '#00ea00', '#00da00', '#00ca00', '#00ba00', '#00aa00', '#009a00', '#008a00', '#007a00', '#006a00',
          '#005a00', '#004a00', '#003a00', '#002a00', '#001a00', '#000000']


class LetterLine:
    def __init__(self):
        self.letterLine = []
        self.isFinished = False

        self.coord_y = random.randint(0, HEIGHT / 2 - 240)

        self.setStartCoords()

    def setStartCoords(self):
        self.coord_x = random.randint(0,int(WIDTH/LINE_DISTANCE-1)) * LINE_DISTANCE
        self.coord_y = random.randint(0,int((HEIGHT/4)/LINE_DISTANCE-1)) * LINE_DISTANCE

    def createLetterLine(self, count):
        letter = canvas.create_text(self.coord_x, self.coord_y, text=random.choice(letterLst), fill='#ffffff',
                                  font=f"{FONT_FACE} {FONT_SIZE}")

        self.letterLine.insert(0, letter)
        self.coord_y += SPACE_SIZE

        for i in range(count, 0, -1):
            canvas.itemconfigure(self.letterLine[i], fill=colors[i - 1])

        if len(self.letterLine) - 15 > HEIGHT / FONT_SIZE:
            for j in self.letterLine:
                canvas.delete(j)
                self.isFinished = True
            return

def selectLineLenght():
    count = 0
    words = LetterLine()
    createRain(words, count)

def createRain(words, count):
    words.createLetterLine(count)

    if count < len(colors) and not words.isFinished:
        count += 1
        root.after(RAIN_SPEED, createRain, words, count)
    elif not words.isFinished:
        root.after(RAIN_SPEED, createRain, words, count)
    else:
        return

def runFucn():
    selectLineLenght()
    root.after(SPAWN_COULMN_RATE, runFucn)

root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('Matrix Rain')
root.config(bg='black')

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
canvas.pack()

runFucn()

root.mainloop()