
# Simple turtle racing game with tkinter
import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['cyan', 'green', 'blue', 'orange', 'brown', 'red', 'purple', 'pink', 'yellow', 'black']

def racersNumber():
    pass

def createTurtles(racers):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    turtles = createTurtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
            

def initializeTurtles():
    screen = turtle.Screen()
    screen.setup(WIDTH,  HEIGHT)
    screen.title("Racing Turtles")

def main(colors):
    racers = racersNumber()
    initializeTurtles()
    random.shuffle(COLORS)
    winner = race(colors)
    print("The winner is the turtle with color, {winner}")

if __name__ == "__main__":
    main()