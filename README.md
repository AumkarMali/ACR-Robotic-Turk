
# ARC: Python & Raspberry Pi Chess Robot

### Introduction & Goal
The acronym stands for Automated Chess Robot, which represents the system's ability to move in three-dimensional space with the assistance of a Chess AI. Users can engage with the system virtually through a built-in graphical user interface (GUI), while the system replicates the board movements in real life. The objective of this extensive project was to integrate my knowledge of data structures and algorithms (DSA) and game theory algorithms with my understanding of electromechanical systems.

## Minimax w/Alpha Beta Pruning Explanation
The concept of the minimax algorithm is to maximize a specified player's score in any two-player game. In this context, the score refers to an  which will be discussed in detail below.

Currently, the program controls the black pieces, while the user controls the white pieces. The user will first make a move on the board. Subsequently, the chess library will generate a list of possible moves that black can make and randomly select one from that list (this serves as a placeholder of sorts).

`moves = list(board.generate_legal_moves())`

`best_move = random.choice(moves) if moves else None`


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
