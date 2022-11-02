import tkinter as tk
from GameModel import GameModel
from GameView import GameView


class Controller():
    def __init__(self):
        self.root = tk.Tk()
        self.view = GameView(self.root, self)
        self.model = GameModel(self)
        # Pass to view links on root frame and controller object


        self.root.mainloop()

    def btn1_click(self):
        self.model.door_selection(0)

    def btn2_click(self):
        self.model.door_selection(1)

    def btn3_click(self):
        self.model.door_selection(2)

    def btn_change_lbl(self, index, str):
        self.view.btns[index]["text"] = str

    def toplbl_change_lbl(self, str):
        self.view.toplbl["text"] = str

    def stats_change_lbl(self, wins, losses):
        self.view.winslbl["text"] = "wins: {wins}".format(wins = wins)
        self.view.losseslbl["text"] = "losses: {losses}".format(losses = losses)

    def btn_change_image(self, index, photo):
        self.view.btns[index].config(image=photo)

    def btn_reset_lbls(self):
        for i, btn in enumerate(self.view.btns):
            btn["text"] = i
        self.view.toplbl["text"] = "Pick one of three doors"

    def simulate(self, changedoor, iter):
        if changedoor:
            self.model.simulateWithChange(iter)
        else:
            self.model.simulateWithNoChange(iter)