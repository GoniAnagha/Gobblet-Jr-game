"""
This code is used create a gobblet junior game using pygame library in python.
It is not a CLI rather it uses mouse clicking to play the game.
It can be played only on one laptop by running this code.
1st player pieces are on left side and 2nd player pieces are on right side 
"""
import pygame
BOARD_SIZE = 600  # Size of the 3x3 board
SIDE_PANEL = 150  # Space for available pieces on each side
width, height = BOARD_SIZE + 2 * SIDE_PANEL, BOARD_SIZE
white = (255, 255, 255)
line_color = (0, 0, 0)
FPS = 30

# Initialize Pygame
pygame.init() # noqa: E1101
screen = pygame.display.set_mode((width, height + 100), 0, 32)
pygame.display.set_caption("Gobblet Game")
CLOCK = pygame.time.Clock()

# Game State
XO = "1st player"
WINNER = None
DRAW = False
board = [[[] for _ in range(3)] for _ in range(3)]  # Stack-based board

# Available Pieces (Each player has 2 of each size)
player_pieces = {
    "1st player": {"Small": 2, "Medium": 2, "Large": 2},
    "2nd player": {"Small": 2, "Medium": 2, "Large": 2}
}

# Selected Piece for Movement
SELECTED_PIECE = None
SELECTED_SOURCE = None  # (row, col) if from board, "left"/"right" if from the side


def draw_board():
    """"
    This function used to display condition of board modifying it as per game
    """
    screen.fill(white)

    # Draw 3x3 Grid (Centered)
    start_x, start_y = SIDE_PANEL, 0
    cell_size = BOARD_SIZE // 3

    # Draw vertical lines
    for i in range(1, 3):
        pygame.draw.line(screen, line_color, (start_x + i * cell_size, start_y),
                     (start_x + i * cell_size, start_y + BOARD_SIZE), 7)

    # Draw horizontal lines
    for i in range(1, 3):
        pygame.draw.line(screen, line_color, (start_x, start_y + i * cell_size),
                     (start_x + BOARD_SIZE, start_y + i * cell_size), 7)

    draw_pieces()
    draw_status()
    pygame.display.update()

def select_piece_from_board(row, col):
    """"
    Function to detect selection of piece on board as source based on mouse click
    """
    global SELECTED_PIECE, SELECTED_SOURCE

    if board[row][col] and board[row][col][-1][1] == XO:
        SELECTED_PIECE = board[row][col][-1]  # Top piece
        SELECTED_SOURCE = (row, col)  # Source position
def draw_pieces():
    """
    Function to display remaining pieces with each player
    and displaying topmost pieces on each cell hiding the below ones
    """
    y_positions = [150, 200, 250]
    sizes = ["Small", "Medium", "Large"]

    # Define font
    label_font = pygame.font.Font(None, 30)  # Font for player labels
    piece_font = pygame.font.Font(None, 25)  # Font for pieces

    # Display player labels
    text1 = label_font.render("1st Player", True, (0, 0, 255))
    text2 = label_font.render("2nd Player", True, (255, 0, 0))
    screen.blit(text1, (20, 100))   # Place above the pieces
    screen.blit(text2, (width - 130, 100))

    # Display remaining pieces for each player
    for i, size in enumerate(sizes):
        if player_pieces["1st player"][size] > 0:
            text = piece_font.render(
                f"{size} x{player_pieces['1st player'][size]}",
                True,
                (0, 0, 255)
            )
            screen.blit(text, (20, y_positions[i]))

        if player_pieces["2nd player"][size] > 0:
            text = piece_font.render(
                f"{size} x{player_pieces['2nd player'][size]}",
                True,
                (255, 0, 0)
            )
            screen.blit(text, (width - 130, y_positions[i]))

    # Draw pieces on the board
    for row in range(3):
        for col in range(3):
            if board[row][col]:
                piece, player = board[row][col][-1]  # Get top piece
                text = pygame.font.Font(None, 40).render(piece[0], True,
                (0, 0, 255) if player == "1st player" else (255, 0, 0))
                center_x = SIDE_PANEL + col * BOARD_SIZE // 3 + BOARD_SIZE // 3 // 3
                center_y = row * BOARD_SIZE // 3 + BOARD_SIZE // 3 // 3
                screen.blit(text, (center_x, center_y))

def draw_status():
    """
    Function to display the present condition of board
    whose turn (1st or 2nd player)
    if somebody won or for a draw condition
    """
    global WINNER, DRAW
    message = (
        f"{XO}'s Turn" if not WINNER else ("Game Draw!" if DRAW 
        else f"{WINNER} Wins! Click here to Restart")
    )
    font = pygame.font.Font(None, 40)
    text = font.render(message, True, (255, 255, 255))
    screen.fill((0, 0, 0), (0, height + 25, width, 100))  # Clear bottom area
    text_rect = text.get_rect(center=(width / 2, height + 50))
    screen.blit(text, text_rect)
    pygame.display.update()


def get_top_piece_color(row, col):
    """
    Function to get topmost piece in every cell 
    """
    if board[row][col]:
        _, player = board[row][col][-1]
        return "blue" if player == "1st player" else "red"
    return None

def check_winner():
    """
    Function to check for winning condition and draw condition
    """
    global WINNER, DRAW
    winning_lines = []

    # Check rows, columns, and diagonals
    for i in range(3):
        winning_lines.append([get_top_piece_color(i, j) for j in range(3)])  # Rows
        winning_lines.append([get_top_piece_color(j, i) for j in range(3)])  # Columns

    winning_lines.append([get_top_piece_color(i, i) for i in range(3)])  # Main diagonal
    winning_lines.append([get_top_piece_color(i, 2 - i) for i in range(3)])  # Anti-diagonal

    blue_wins = any(line == ["blue"] * 3 for line in winning_lines)
    red_wins = any(line == ["red"] * 3 for line in winning_lines)

    if blue_wins and red_wins:
        DRAW = True
        WINNER = None
    elif blue_wins:
        WINNER = "1st player"
    elif red_wins:
        WINNER = "2nd player"

def reset_game():
    """
    Function to reset the game board and pieces 
    after win or draw
    """
    global board, XO, WINNER, DRAW, SELECTED_PIECE, SELECTED_SOURCE, player_pieces

    # Reset the board (3x3 grid with empty lists)
    board = [[[] for _ in range(3)] for _ in range(3)]

    # Reset available pieces
    player_pieces = {
        "1st player": {"Small": 2, "Medium": 2, "Large": 2},
        "2nd player": {"Small": 2, "Medium": 2, "Large": 2}
    }

    # Reset game state
    XO = "1st player"
    WINNER = None
    DRAW = False
    SELECTED_PIECE = None
    SELECTED_SOURCE = None

    # ReDRAW the board
    draw_board()

def click_event():
    """
    Function to detect mouse click and perform required operation
    """
    global SELECTED_PIECE, SELECTED_SOURCE, XO
    if WINNER or DRAW:
        reset_game()
        return

    x, y = pygame.mouse.get_pos()

    # Check if clicking on a player's side (piece selection)
    if x < SIDE_PANEL:  # Left side (Player 1)
        select_piece_from_side("1st player", y)
        return
    if x > BOARD_SIZE + SIDE_PANEL:  # Right side (Player 2)
        select_piece_from_side("2nd player", y)
        return

    row, col = y // (BOARD_SIZE // 3), (x - SIDE_PANEL) // (BOARD_SIZE // 3)

    if SELECTED_PIECE:
        move_piece(row, col)
    else:
        select_piece_from_board(row, col)


def select_piece_from_side(player, y):
    """
    Function to detect a selection of piece (that is outside board) as source
    """
    global SELECTED_PIECE, SELECTED_SOURCE

    if player != XO:
        return

    piece = None
    if 150 <= y < 200:
        piece = "Small"
    elif 200 <= y < 250:
        piece = "Medium"
    elif 250 <= y < 300:
        piece = "Large"

    if piece and player_pieces[player][piece] > 0:
        SELECTED_PIECE = (piece, player)
        SELECTED_SOURCE = "left" if player == "1st player" else "right"


def move_piece(row, col):
    """
    Function to move pieces according to source and destination
    """
    global SELECTED_PIECE, SELECTED_SOURCE, XO

    piece, player = SELECTED_PIECE
    size_order = {"Small": 1, "Medium": 2, "Large": 3}

    # Check if the move is valid
    if board[row][col]:
        top_piece, _ = board[row][col][-1]
        if size_order[piece] <= size_order[top_piece]:
            SELECTED_PIECE = None
            SELECTED_SOURCE = None
            return  # Invalid move, do nothing
    # If selected piece was from the side, decrement the count
    if SELECTED_SOURCE in ["left", "right"]:
        player_pieces[player][piece] -= 1
    # If selected piece was from the board, remove it from its original position
    elif isinstance(SELECTED_SOURCE, tuple):
        board[SELECTED_SOURCE[0]][SELECTED_SOURCE[1]].pop()

    # Place the piece at the new location
    board[row][col].append(SELECTED_PIECE)

    check_winner()
    if not WINNER and not DRAW:
        XO = "2nd player" if XO == "1st player" else "1st player"

    SELECTED_PIECE = None
    SELECTED_SOURCE = None
    draw_board()

# Start the game
draw_board()
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:# noqa: E1101
            RUNNING = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # noqa: E1101
            click_event()

pygame.quit() # noqa: E1101
