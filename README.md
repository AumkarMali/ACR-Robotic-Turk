
# ARC: Python & Raspberry Pi Chess Robot

### Introduction & Goal
The acronym stands for Automated Chess Robot, which represents the system's ability to move in three-dimensional space with the assistance of a Chess AI. Users can engage with the system virtually through a built-in graphical user interface (GUI), while the system replicates the board movements in real life. The objective of this extensive project was to integrate my knowledge of data structures and algorithms (DSA) and game theory algorithms with my understanding of electromechanical systems.

## Minimax w/Alpha Beta Pruning Explanation
The concept of the minimax algorithm is to maximize a specified player's score in any two-player game. In this context, the score refers to an  which will be discussed in detail below.

Currently, the program controls the black pieces, while the user controls the white pieces. The user will first make a move on the board. Subsequently, the chess library will generate a list of possible moves that black can make and randomly select one from that list (this serves as a placeholder of sorts).

`moves = list(board.generate_legal_moves())`
`best_move = random.choice(moves) if moves else None`

The function is then recursively called with parameters indicating that it is the next player's turn and decrementing the depth, which is the number of recursions (or future moves) that are going to be done for every possible scenario. Eventually, the depth will be 0, and the evaluation function will be returned, indicating the score of the program's move decision. That score will be compared to a local minimum value (-INFINITY) throughout the iterations of all possible moves, so the program knows what the best move to make is by the end of its recursions. It is important to note that the outer call will explore a certain move and return a score for that path. The outer call will then take the score returned from this path and compare it with scores from other paths. Each recursive call operates on its own state of the board after a move has been pushed. When you call pop, it removes the last move, so all inner calls will not affect the outer calls or other inner calls. This ensures that each recursive exploration is independent.

#### Alpha-Beta Pruning

Pruning refers to the process of stopping the evaluation of certain branches in the game tree. This happens when we determine that continuing to explore those branches cannot possibly influence the final decision about which move to make. If the maximizing player finds that their best guaranteed score (alpha) is greater than or equal to what the minimizing player could allow (beta), they can safely prune the branch. Conversely, if the minimizing player finds that they can guarantee a score that is lower than or equal to what the maximizing player can achieve (alpha), they can also prune.

    
##GUI

Tkinter library was used to create a chess board that mimics the real-life chess board that the robot plays on, and allows users to input their moves. The `draw_board()` function iterates through the board setup from the chess library and adds the pieces to each ssquare of the board after each move. 

![Description of the image](https://ibb.co/mb2dqt1)


### Robotic Arm

Movement to specific squares on the chess board are defined in controlMovements.json:


```json
  {
    "a1": [190, 185, 17],
    "a2": [186, 175, 13],
    "a3": [183, 166, 9],
    "a4": [181, 158, 7],
    "a5": [179, 150, 6],
    "a6": [175, 142, 7],
    "a7": [167, 134, 6],
    "a8": [165, 126, 11],
    "b1": [193, 182, 16],
    "b2": [192, 174, 9],
    "b3": [191, 164, 9],
    "b4": [188, 156, 7],
    "b5": [187, 146, 7],
    "b6": [184, 139, 7],
    "b7": [181, 129, 11],
    ...
}
```

Values can be changes based on size of board used. For testing, chess board of size 30.5cm x 30.5 cm was used.
