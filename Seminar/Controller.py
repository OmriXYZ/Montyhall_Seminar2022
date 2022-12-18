import tkinter as tk
from GameModel import GameModel
from GameView import GameView
import StatisticPlot


class Controller():
    def __init__(self):
        self.root = tk.Tk()
        self.plotStat = StatisticPlot.plotStat(self.root)
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
        sumstats = wins + losses
        winrate = (wins / sumstats) * 100 if sumstats != 0 else 0

        self.view.winslbl["text"] = "Wins: {wins}".format(wins=wins)
        self.view.losseslbl["text"] = "Losses: {losses}".format(losses=losses)
        self.view.winratelbl["text"] = "Win Rate: {winrate}%".format(winrate=round(winrate, 2))

    def stats_change_lbl_simulate(self, wins, losses, changedoor):
        self.stats_change_lbl(wins, losses)
        self.view.changedoorlbl["text"] = f"The door changed randomly: {changedoor} times".format(changedoor=changedoor)
        self.plotStat.update(wins, losses)
        self.plotStat.showPlot(self.root)

    def btn_change_image(self, index, photo):
        self.view.btns[index].config(image=photo)

    def btn_reset_lbls(self):
        for i, btn in enumerate(self.view.btns):
            btn["text"] = i
        self.view.toplbl["text"] = "Pick one of three doors"

    def simulate(self, changedoor, iter):
        try:
            iter = int(iter)
        except ValueError:
            self.view.change_exceptionlbl('Iterations needs to be an integer')
            return
        if iter > 1000000 or iter <= 0:
            self.view.change_exceptionlbl('Iterations needs to be in range from 1 to 1,000,000')
            return
        self.btn_reset_game()
        if changedoor == 0:
            self.model.simulateWithChange(iter)
        elif changedoor == 1:
            self.model.simulateWithNoChange(iter)
        else:
            self.model.simulateWithRandChange(iter)

    def btn_reset_game(self):
        self.model.reset_stats()
        self.view.change_exceptionlbl('')

    def change_doorlbl(self, i, str):
        self.view.doorlbls[i]["text"] = str