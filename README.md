
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

## Non-linear Evaluation Function

Scores are calculated by summing up pieces from both the white and black sides of the board, where each piece has a different weight. In addition to this linear method of evaluating each side's boards, a defensive strategy was implemented by searching through the nearest pieces near each player's kings. After finding each of these surrounding pieces and weighing them accordingly, their values are squared, multiplied by a small scalar, and multiplied by another variable called timed kind defense. This variable is incremented after each move the program makes in order to time its defensive behavior near the middle of the game rather than the beginning. Changing the magnitude of this value will vary the effect of the program's defensive behavior, while decrementing it will lead to a highly aggressive program behavior.

![Chess Piece Scoring Example](https://i.ibb.co/W0p9q7w/Screenshot-2024-10-03-024815.png)
    
## GUI

Tkinter library was used to create a chess board that mimics the real-life chess board that the robot plays on, and allows users to input their moves. The `draw_board()` function iterates through the board setup from the chess library and adds the pieces to each ssquare of the board after each move. 


[![Description of the image](https://i.ibb.co/jbQqMGB/Screenshot-2024-09-28-110514.png)](https://ibb.co/mb2dqt1)



## Front-end and back-end communication, subprocesses and threading
In terms of the GUI, a threading event is created and an update function calls the GUI to update the board and then signals that the update is complete by calling `update_event.set()`

Next the computer waits for the users move (after waiting for the board update to complete), which will be displayed in a text file. Once the program gets the users move from this file. This is done through 2 threads that individually update the board, and wait for the users move and react.

The program is run from `run.py`, which individually runs the back-end algorithm and the GUI, ensuring that they can communicate using the text file.

WARNING: These subprocesses, if not manually stopped (e.g., task manager), can take up a lot of memory from the computer.

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

## Circuit Schematic
[![Screenshot](https://i.ibb.co/4T75RhJ/Screenshot-2024-09-28-112310.png)](https://ibb.co/vPHK40D)


## Authors

- [@AumkarMali](https://ibb.co/X4hXB1d)


## Deployment

Download Arduino IDE from https://docs.arduino.cc/software/ide-v1/tutorials/Windows

## Links

➊ Github: https://github.com/AumkarMali/

➋ Youtube: https://www.youtube.com/channel/UC7rhCKur9bF01lV0pNJNkvA

