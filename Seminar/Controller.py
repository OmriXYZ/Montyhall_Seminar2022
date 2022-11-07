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
        except:
            self.view.change_exceptionlbl('Iterations needs to be an integer')
            raise ValueError('iterations need to be integer')
        if iter > 1000000 or iter <= 0:
            self.view.change_exceptionlbl('Iterations needs to be in range from 1 to 1,000,000')
            raise Exception('iterations must be positive number and less than 1,000,000')
        self.btn_reset_game()
        if changedoor:
            self.model.simulateWithChange(iter)
        else:
            self.model.simulateWithNoChange(iter)

    def simulate_random_choice(self, iter):
        try:
            iter = int(iter)
        except:
            self.view.change_exceptionlbl('Iterations needs to be an integer')
            raise ValueError('iterations need to be integer')
        if iter > 1000000 or iter <= 0:
            self.view.change_exceptionlbl('Iterations needs to be in range from 1 to 1,000,000')
            raise Exception('iterations must be positive number and less than 1,000,000')
        self.btn_reset_game()
        self.model.simulateWithRandChange(iter)

    def btn_reset_game(self):
        self.model.reset_stats()

    def letPC_do_thechoice(self):
        self.view.create_btn_letChoiceToPC(self.root)

    def random_choice_fromview(self):
        self.model.safeRandChoose()