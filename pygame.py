import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Maze Game")
wn.setup(700,700)
turtle.register_shape("Thief_left.gif")
turtle.register_shape("Thief_right.gif")
turtle.register_shape("wall.gif")
turtle.register_shape("treasure.gif")
turtle.register_shape("pm_right.gif")
turtle.register_shape("pm_left.gif")

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("wall.gif")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Thief_right.gif")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        if (move_to_x , move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)


    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() -  24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            self.shape("Thief_left.gif")

    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            self.shape("Thief_right.gif")

    def is_collision(self,other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance  = math.sqrt(a**2 + b**2)

        if distance < 5:
            return True
        else:
            return False

class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("treasure.gif")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("pm_left.gif")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x,y)
        self.direction = random.choice(["up","down","left","right"])

    def is_close(self,other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt(a**2 + b**2)

        if distance < 120:
            return True
        else:
            return False

    def move(self):
        wn.tracer(0)
        if self.direction == "up":
            dx = 0
            dy = 24

        elif self.direction == "down":
            dx = 0
            dy = -24

        elif self.direction == "right":
            dx = 24
            dy = 0
            self.shape("pm_right.gif")

        elif self.direction == "left":
            dx = -24
            dy = 0
            self.shape("pm_left.gif")

        else:
            dx = 0
            dy = 0

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() >= self.xcor():
                self.direction = "right"
            if player.ycor() < self.ycor():
                self.direction = "down"
            elif player.xcor() >= self.xcor():
                self.direction = "up"


        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

        else:
            self.direction = random.choice(["up", "down", "left", "right"])
        turtle.ontimer(self.move, t = random.randint(100,300))
        wn.update()

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()


levels = [""]
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXXE         XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "XT      XX  XXX       EXX",
    "XXXXXX  XX  XXXT       XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "X  XXX        XXXX  XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXX",
    "XT               XXXXXXXX",
    "XXXXXXXXXXXX     XXXXX  X",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXXE                    X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX              X",
    "XXE  XXXXXT             X",
    "XX   XXXXXXXXXXXXX  XXXXX",
    "XX     XXXXXXXXXXX  XXXXX",
    "XX          XXXX        X",
    "XXXXT                   X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]
levels.append(level_1)
enemies = []

def setup_maze(level):
    wn.tracer(0)
    for y in range(len(level)):
        for x in range(len(level)):
            character = level[y][x]
            screen_x = -288 + 24*x
            screen_y = 288 - 24*y

            if character == "X":
                pen.goto(screen_x,screen_y)
                walls.append((screen_x,screen_y))
                pen.stamp()

            if character == "P":
                player.goto(screen_x,screen_y)

            if character == "T":
                treasures.append(Treasure(screen_x,screen_y))

            if character == "E":
                enemies.append(Enemy(screen_x,screen_y))
    wn.update()
pen = Pen()
player = Player()
walls = []
treasures = []

setup_maze(levels[1])

turtle.listen()
turtle.onkeypress(player.go_up,"Up")
turtle.onkeypress(player.go_down,"Down")
turtle.onkeypress(player.go_left,"Left")
turtle.onkeypress(player.go_right,"Right")

for enemy in enemies:
    turtle.ontimer(enemy.move, t = 250)

while True:
    wn.tracer(0)
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player Gold : {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)

    for enemy in enemies:
        if player.is_collision(enemy):
            print("Player dies!")

    wn.update()

wn.mainloop()
