import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.buttons = []
        self.canvas = tk.Canvas(master, width=300, height=300)
        self.canvas.pack()
        self.turn = 'X'
        self.winner = None

        for i in range(3):
            self.buttons.append([])
            for j in range(3):
                button = tk.Button(master, text="", width=10, height=3, command=lambda i=i, j=j: self.click(i, j))
                self.canvas.create_window(100 + j * 100, 100 + i * 100, window=button)
                self.buttons[i].append(button)

        self.reset_button = tk.Button(master, text="Reset", width=10, height=3, command=self.reset)
        self.canvas.create_window(100, 500, window=self.reset_button)

    def click(self, i, j):
        if self.buttons[i][j]['text'] or self.winner:
            return

        self.buttons[i][j]['text'] = self.turn
        self.check_winner()
        self.turn = 'O' if self.turn == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if self.check_row(i) or self.check_column(i):
                return

        if self.check_diagonal():
            return

        if all(button['text'] for row in self.buttons for button in row):
            self.declare_winner("It's a tie!")

    def check_row(self, row):
        first_button = self.buttons[row][0]['text']
        return all(button['text'] == first_button for button in self.buttons[row]) and first_button

    def check_column(self, column):
        first_button = self.buttons[0][column]['text']
        return all(button['text'] == first_button for button in self.buttons if button is self.buttons[column][0]) and first_button

    def check_diagonal(self):
        first_button = self.buttons[1][1]['text']
        if all(button['text'] == first_button for button in (self.buttons[i][i] for i in range(3)))):
            return True
        if all(button['text'] == first_button for button in (self.buttons[i][2 - i] for i in range(3)))):
            return True
        return False

    def declare_winner(self, message):
        self.winner = message
        messagebox.showinfo("Winner", message)

    def reset(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ""
        self.winner = None

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()