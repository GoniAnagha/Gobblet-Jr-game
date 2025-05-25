# Gobblet-Jr-Game

### How to Run
- Download and run the Python script using:  
  `python3 gobblet.py`  
  *(Make sure Python 3 is installed before running the script)*

- This opens a GUI displaying:
  - An empty 3x3 board.
  - Gobblet pieces for each player.
  - The current player's turn shown at the bottom of the GUI.

---

### Game Interface Details
- Pieces on the board are represented as:
  - **S** — Small piece
  - **M** — Medium piece
  - **L** — Large piece  
  (To improve clarity during gameplay)

- Player actions:
  - Click on a piece on your side (only your pieces) or on the board to select a source piece.
  - Then click on any board cell to move/place the piece.

- Invalid moves:
  - The board state remains unchanged if an invalid move is made.

- After every move:
  - The pieces left with the player (not on the board) are updated and displayed.

- Game end:
  - After a win or draw, the status is displayed at the bottom of the GUI.
  - Click "Restart" to start a new game.

---

### Game Rules
- The 3x3 game is a generalization of tic-tac-toe:
  - The goal is to get three in a row of your color (vertical, horizontal, or diagonal).
  - Piece size does **not** affect winning.

- Each player (red or yellow) starts with 6 pieces:  
  2 large, 2 medium, and 2 small.

- On each turn, a player can either:
  - Place a new piece on the board, or
  - Move a piece already on the board (from anywhere to anywhere different).

- A piece can be placed or moved to:
  - An empty space, or
  - On top of a smaller piece already on the board ("gobbling" it).

- Smaller pieces can belong to either player and may themselves have gobbled pieces previously.

- Only visible pieces can be moved and count toward winning. Gobbled pieces remain on the board hidden.

- Moving a piece exposes any pieces it gobbled (they become visible again).

- If moving a piece exposes a winning sequence for the opponent (and the destination does not cover one of those winning pieces), the opponent wins — even if the move creates a winning sequence for the moving player.

- Players must move a piece if they touch it. If the piece cannot be moved, the player forfeits.  
  *(Note: This particular rule is **not** enforced in this version)*

---

### Important Notes
- Since this is a basic version, **player details are not tracked or verified**.  
- The program only checks whose turn it is and restricts interaction to the corresponding player’s side; however, it does not verify the actual identity of the player. In other words, it does not confirm whether the person interacting on a player’s side is the same player or someone else. This applies to both the 1st and 2nd player sides.
- Whoever plays first is considered Player 1, so please remember which player you are before starting the game.  
- Advanced features like user login, player profiles, and strict player verification are not included.

---
