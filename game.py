import tkinter as tk
from tkinter import messagebox
import random

# Constants
BOARD_SIZE = 10
SQUARE_SIZE = 50
PLAYER_COLORS = ["#FF6F61", "#6B5B95", "#88B04B", "#FFA500"]  # Modern colors
NUM_PLAYERS = 2  # Can be adjusted up to 4

# Define snakes and ladders
snakes = {
    16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78
}
ladders = {
    1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100
}

# Players
players = [{"position": 0, "token": None} for _ in range(NUM_PLAYERS)]
current_player = 0
game_over = False
steps_remaining = 0

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to move the player step-by-step
def move_player(player, steps):
    global game_over, steps_remaining
    steps_remaining = steps
    animate_move(player)

def animate_move(player):
    global game_over, steps_remaining
    if steps_remaining > 0:
        players[player]["position"] += 1
        steps_remaining -= 1

        # Check if the player lands exactly on a snake or ladder at the final step
        if steps_remaining == 0:
            if players[player]["position"] in snakes:
                players[player]["position"] = snakes[players[player]["position"]]
            elif players[player]["position"] in ladders:
                players[player]["position"] = ladders[players[player]["position"]]

        # Ensure the player does not exceed 100
        if players[player]["position"] > 100:
            players[player]["position"] -= 1  # Revert if player exceeds 100

        # Check if the player has won
        if players[player]["position"] == 100:
            messagebox.showinfo("Game Over", f"Player {player + 1} wins!")
            game_over = True

        update_board()
        if not game_over and steps_remaining > 0:
            root.after(200, animate_move, player)  # Smoother animation with shorter delay
        elif not game_over:
            switch_player()

def switch_player():
    global current_player
    current_player = (current_player + 1) % NUM_PLAYERS
    status_label.config(text=f"Player {current_player + 1}'s turn")

# Function to update the board
def update_board():
    for i, player in enumerate(players):
        row, col = get_row_col(player["position"])
        if player["token"]:
            # Smoothly move the token
            x1 = col * SQUARE_SIZE + 10
            y1 = row * SQUARE_SIZE + 10
            x2 = col * SQUARE_SIZE + 40
            y2 = row * SQUARE_SIZE + 40
            canvas.coords(player["token"], x1, y1, x2, y2)
    status_label.config(text=f"Player {current_player + 1}'s turn")

# Function to get row and column from position
def get_row_col(position):
    if position == 0:
        return BOARD_SIZE - 1, 0
    row = (position - 1) // BOARD_SIZE
    col = (position - 1) % BOARD_SIZE
    if row % 2 != 0:
        col = BOARD_SIZE - 1 - col
    return BOARD_SIZE - 1 - row, col

# Function to handle the roll button click
def on_roll():
    global game_over
    if not game_over:
        steps = roll_dice()
        dice_label.config(text=f"Dice: {steps}")
        move_player(current_player, steps)

# Function to restart the game
def on_restart():
    global players, current_player, game_over
    for player in players:
        player["position"] = 0
    current_player = 0
    game_over = False
    update_board()
    dice_label.config(text="Dice: 0")

# Function to exit the game
def on_exit():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Snake and Ladders Game")
root.configure(bg="#F0F0F0")  # Light gray background

# Create canvas for the board
canvas = tk.Canvas(root, width=BOARD_SIZE * SQUARE_SIZE, height=BOARD_SIZE * SQUARE_SIZE, bg="#FFFFFF", bd=0, highlightthickness=0)
canvas.pack(pady=20)

# Draw the board with rounded corners and gradients
for row in range(BOARD_SIZE):
    for col in range(BOARD_SIZE):
        x1, y1 = col * SQUARE_SIZE, row * SQUARE_SIZE
        x2, y2 = x1 + SQUARE_SIZE, y1 + SQUARE_SIZE
        color = "#E0E0E0" if (row + col) % 2 == 0 else "#F5F5F5"  # Light gray and white
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#CCCCCC", width=2)
        position = (BOARD_SIZE - 1 - row) * BOARD_SIZE + (col if (BOARD_SIZE - 1 - row) % 2 == 0 else BOARD_SIZE - 1 - col) + 1
        canvas.create_text(x1 + SQUARE_SIZE // 2, y1 + SQUARE_SIZE // 2, text=str(position), font=("Arial", 10), fill="#333333")

# Draw snakes and ladders with smooth lines
for start, end in snakes.items():
    row1, col1 = get_row_col(start)
    row2, col2 = get_row_col(end)
    canvas.create_line(col1 * SQUARE_SIZE + SQUARE_SIZE // 2, row1 * SQUARE_SIZE + SQUARE_SIZE // 2,
                       col2 * SQUARE_SIZE + SQUARE_SIZE // 2, row2 * SQUARE_SIZE + SQUARE_SIZE // 2, fill="#FF6F61", width=4, smooth=True)
for start, end in ladders.items():
    row1, col1 = get_row_col(start)
    row2, col2 = get_row_col(end)
    canvas.create_line(col1 * SQUARE_SIZE + SQUARE_SIZE // 2, row1 * SQUARE_SIZE + SQUARE_SIZE // 2,
                       col2 * SQUARE_SIZE + SQUARE_SIZE // 2, row2 * SQUARE_SIZE + SQUARE_SIZE // 2, fill="#88B04B", width=4, smooth=True)

# Create player tokens with rounded shapes
for i, player in enumerate(players):
    row, col = get_row_col(player["position"])
    player["token"] = canvas.create_oval(
        col * SQUARE_SIZE + 10,  # x1
        row * SQUARE_SIZE + 10,  # y1
        col * SQUARE_SIZE + 40,  # x2
        row * SQUARE_SIZE + 40,  # y2
        fill=PLAYER_COLORS[i], outline="#333333", width=2
    )

# Create status panel with modern fonts
status_label = tk.Label(root, text="Player 1's turn", font=("Helvetica", 16, "bold"), bg="#F0F0F0", fg="#333333")
status_label.pack(pady=10)

dice_label = tk.Label(root, text="Dice: 0", font=("Helvetica", 14), bg="#F0F0F0", fg="#333333")
dice_label.pack(pady=10)

# Create buttons with rounded corners and modern colors
button_frame = tk.Frame(root, bg="#F0F0F0")
button_frame.pack(pady=10)

roll_button = tk.Button(button_frame, text="Roll Dice", command=on_roll, font=("Helvetica", 14), bg="#6B5B95", fg="white", bd=0, padx=20, pady=10, relief="flat")
roll_button.pack(side=tk.LEFT, padx=10)

restart_button = tk.Button(button_frame, text="Restart Game", command=on_restart, font=("Helvetica", 14), bg="#FF6F61", fg="white", bd=0, padx=20, pady=10, relief="flat")
restart_button.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(button_frame, text="Exit Game", command=on_exit, font=("Helvetica", 14), bg="#333333", fg="white", bd=0, padx=20, pady=10, relief="flat")
exit_button.pack(side=tk.LEFT, padx=10)

# Start the game
update_board()
root.mainloop()