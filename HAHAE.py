# Imprts

import turtle
import time
import random

# Screen

wn = turtle.Screen()
wn.title("TETRIS")
wn.bgcolor("NavajoWhite2")
wn.setup(width=600, height=800)
wn.tracer(0)

# Settings

delay = 0.1

#Functions

class Shape():
    def __init__(self):
        self.x = 5
        self.y = 0
        self.color = random.randint(1, 7)

        square = [[1,1],[1,1]]

        horizontal_line = [[1,1, 1, 1]]

        vertical_line = [[1],[1],[1],[1]]

        left_l = [[1,0,0,0],[1,1,1,1]]

        right_l = [[0,0,0,1],[1,1,1,1]]

        left_s = [[1,1,0],[0,1,1]]

        right_s = [[0,1,1],[1,1,0]]

        t = [[0,1,0],[1,1,1]]

        shapes = [square, horizontal_line, vertical_line, left_l, right_l, left_s, right_s, t]

        self.shape = random.choice(shapes)

        self.height = len(self.shape)
        self.width = len(self.shape[0])

        #print(self.height, self.width)

    def move_left(self, grid):
        if self.x > 0:
            if grid[self.y][self.x - 1] == 0:
                self.erase_shape(grid)
                self.x -= 1
    
    def move_right(self, grid):
        if self.x < 12 - self.width:
            if grid[self.y][self.x + self.width] == 0:
                self.erase_shape(grid)
                self.x += 1

    def draw_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 1:
                    grid[self.y + y][self.x + x] = self.color


    def erase_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                grid[self.y + y][self.x + x] = 0

    def can_move(self, grid):
        result = True
        for x in range(self.width):
            # Check if bottom is a 1
            if(self.shape[self.height-1][x] == 1):
                if(grid[self.y + self.height][self.x + x] != 0):
                    result = False
            print(x, self.height -1, self.y + self.height, self.x + x)

        return result

    def rotate(self, grid):

        # First erase_shape

        self.erase_shape(grid)
        rotated_shape = []
        for x in range(len(self.shape[0])):
            next_row = []
            for y in range(len(self.shape)-1, -1, -1):
                next_row.append(self.shape[y][x])
            rotated_shape.append(next_row)
        right_side = self.x + len(rotated_shape[0])
        if right_side < len(grid[0]):
            self.shape = rotated_shape
            # Update the height and width

            self.height = len(self.shape)
            self.width = len(self.shape[0])


grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Create the drawing pen
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(None)




def draw_grid(pen, grid):
    pen.clear()
    top = 230
    left = -110

    colors = ["black", "lightblue", "blue", "orange", "yellow", "green", "purple", "red"]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x = left + (x * 20)
            screen_y = top - (y * 20)
            color_number = grid[y][x]
            color = colors[color_number]
            pen.color(color)
            pen.goto(screen_x, screen_y)
            pen.stamp()

def check_grid(grid):
        # Check if each row is full
    y = 23
    while y > 0:
        is_full = True
        for x in range(0, 12):
            if grid[y][x] == 0:
                is_full = False
                y -= 1
                break
        if is_full:
            global score
            score += 10
            draw_score(pen, score)
            for copy_y in range(y, 0, -1):
                for copy_x in range(0, 12):
                    grid[copy_y][copy_x] = grid[copy_y-1][copy_x]

def draw_score(pen, score):
    pen.color("white")
    pen.hideturtle()
    pen.goto(-75, 300)
    pen.write("Score: {}".format(score), move=False, align="left", font=("Arial",50, "normal"))
   

shape = Shape()
grid[shape.y][shape.x] = shape.color

# draw_grid(pen, grid)


# On key press's

wn.listen()
wn.onkeypress(lambda: shape.move_left(grid), "a")
wn.onkeypress(lambda: shape.move_right(grid), "d")
wn.onkeypress(lambda: shape.rotate(grid), "r")

# Set the score to 0
score = 0

draw_score(pen, score)

# Main game: loop
while True:
    wn.update()
    draw_score(pen, score)

    # Move the shape
    if shape.y == 23 - shape.height + 1: # + 2
        shape = Shape()
        check_grid(grid)
    elif shape.can_move(grid):
        # Erase the current Shape
        shape.erase_shape(grid)
        # Move the current shape by 1
        shape.y += 1
        # Dras whe shape again
        shape.draw_shape(grid)


    else:
        shape = Shape()
        check_grid(grid)




    # Draw the screen
    draw_grid(pen, grid)
    draw_score(pen, score)
    time.sleep(delay)


wn.mainloop()

