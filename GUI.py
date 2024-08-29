import tkinter as tk
from string import whitespace
from tkinter import PhotoImage
import chess
import threading

board = chess.Board()

win = tk.Tk()
win.geometry("700x700")
win.title('ACR mainframe')

#Get the current screen width and height
canvas = tk.Canvas(win, width=700, height=700)
canvas.pack(fill=tk.BOTH, expand=True)


pieceImages = {
    'white_pawn': PhotoImage(file=r"pieces-png/white-pawn.png"),
    'white_bishop': PhotoImage(file=r"pieces-png/white-bishop.png"),
    'white_rook': PhotoImage(file=r"pieces-png/white-rook.png"),
    'white_king': PhotoImage(file=r"pieces-png/white-king.png"),
    'white_queen': PhotoImage(file=r"pieces-png/white-queen.png"),
    'white_knight': PhotoImage(file=r"pieces-png/white-knight.png"),
    'black_pawn': PhotoImage(file=r"pieces-png/black-pawn.png"),
    'black_bishop': PhotoImage(file=r"pieces-png/black-bishop.png"),
    'black_rook': PhotoImage(file=r"pieces-png/black-rook.png"),
    'black_king': PhotoImage(file=r"pieces-png/black-king.png"),
    'black_queen': PhotoImage(file=r"pieces-png/black-queen.png"),
    'black_knight': PhotoImage(file=r"pieces-png/black-knight.png"),
}
boardColumns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

#Create grid of squares and pieces
def draw_board(board):
    for row in range(8):
        for col in range(8):

            if (row + col) % 2 == 0:
                fill_color = '#61390b'
            else:
                fill_color = '#411903'

            canvas.create_rectangle(col*87.5, row*87.5, 87.5 + col*87.5, 87.5 + row*87.5, fill=fill_color)

            squareCheck = chess.parse_square(boardColumns[col] + str(8 - row))
            occupy = board.piece_at(squareCheck)

            if str(occupy) == 'r':
                canvas.create_image(43.75 + 87.5 * col, 43.75 + 87.5 * row, anchor=tk.CENTER,
                                    image=pieceImages['black_rook'])
            elif str(occupy) == 'q':
                canvas.create_image(43.75 + 87.5 * col, 43.75 + 87.5 * row, anchor=tk.CENTER,
                                    image=pieceImages['black_queen'])
            elif str(occupy) == 'k':
                canvas.create_image(43.75 + 87.5 * col, 43.75 + 87.5 * row, anchor=tk.CENTER,
                                    image=pieceImages['black_king'])
            elif str(occupy) == 'n':
                canvas.create_image(43.75 + 87.5 * col, 43.75 + 87.5 * row, anchor=tk.CENTER,
                                    image=pieceImages['black_knight'])
            elif str(occupy) == 'p':
                canvas.create_image(43.75 + 87.5 * col, 43.75 + 87.5 * row, anchor=tk.CENTER,
                                    image=pieceImages['black_pawn'])
            elif str(occupy) == 'b':
                canvas.create_image(43.75 + 87.5 * col, 43.75 + 87.5 * row, anchor=tk.CENTER,
                                    image=pieceImages['black_bishop'])
            elif str(occupy) == 'R':
                canvas.create_image(43.75 + 87.5 * col, 43.75 + 87.5 * row, anchor=tk.CENTER,
                                    image=pieceImages['white_rook'])
            elif str(occupy) == 'Q':
                canvas.create_image(43.75 + 87.5 * col, 43.75 + 87.5 * row, anchor=tk.CENTER,
                                    image=pieceImages['white_queen'])
            elif str(occupy) == 'K':
                canvas.create_image(43.75 + 87.5 * col, 43.75 + 87.5 * row, anchor=tk.CENTER,
                                    image=pieceImages['white_king'])
            elif str(occupy) == 'N':
                canvas.create_image(43.75 + 87.5 * col, 43.75 + 87.5 * row, anchor=tk.CENTER,
                                    image=pieceImages['white_knight'])
            elif str(occupy) == 'P':
                canvas.create_image(43.75 + 87.5 * col, 43.75 + 87.5 * row, anchor=tk.CENTER,
                                    image=pieceImages['white_pawn'])
            elif str(occupy) == 'B':
                canvas.create_image(43.75 + 87.5 * col, 43.75 + 87.5 * row, anchor=tk.CENTER,
                                    image=pieceImages['white_bishop'])


draw_board(board)
determinedMove = ''

def waitCompMove():
    while True:
        with open('save_move.txt', 'r') as file:
            file.readline()  # Skip first line
            computerMove = file.readline().strip()  # Use strip() to remove any leading/trailing whitespace

            if computerMove != '':
                return computerMove


def on_click(event):
    global determinedMove

    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    x, y = event.x, event.y

    col = int(x // 87.5)
    row = 8 - int(y // 87.5)

    determinedMove += (columns[col] + str(row))

    if len(determinedMove) == 4:
        try:
            board.push_uci(determinedMove)

            with open("save_move.txt", "a") as file:
                file.write(determinedMove + "\n")
            determinedMove = ''

            # Use threading.Event to synchronize threads
            update_event = threading.Event()

            def update_after_move():
                draw_board(board)
                update_event.set()  # Signal that the update is complete

            def check_computer_move():
                update_event.wait()  # Wait until the board update is complete
                cm = waitCompMove()
                if cm:
                    board.push_uci(cm)
                    win.after(0, lambda: draw_board(board))
                    with open('save_move.txt', 'r+') as file:
                        file.truncate(0)

            # Run update and computer move checking in separate threads
            threading.Thread(target=update_after_move).start()
            threading.Thread(target=check_computer_move).start()

        except ValueError:
            print('\n', "Invalid move")
            determinedMove = ''

canvas.bind("<Button-1>", on_click)
win.mainloop()