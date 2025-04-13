import turtle
import random
WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'blue', 'green', 'orange', 'black', 'brown', 'pink', 'purple']

def get_no_of_racers():
    racers = 0
    while True:
        racers = input("Enter the no of racers (2-10)  : ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid input, please enter a real number")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("OOPS!! no. is not in range please try again")


def create_turtles(colors):
    turtles = []
    # Calculate spacing between turtles
    spacing = WIDTH // (len(colors) + 1)
    # Set starting x coordinate
    x_start = -WIDTH//2 + spacing
    
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        # Set position: x varies with spacing, y starts at bottom
        racer.setpos(x_start + i * spacing, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles  # Return the list of turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle racing!!')

# Add this new function for the racing logic
def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            
            # Check if racer has crossed finish line
            if racer.ycor() >= HEIGHT//2 - 20:
                return colors[turtles.index(racer)]

racers = get_no_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]

# Start the race and get the winner
winner = race(colors)
print(f"The winner is the {winner} turtle!")

# Keep the window open until clicked
screen = turtle.Screen()
screen.exitonclick()
