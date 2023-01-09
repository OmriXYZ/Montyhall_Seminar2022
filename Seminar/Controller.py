import tkinter as tk
from GameModel import GameModel
from GameView import GameView
import StatisticPlot


class Controller():
    def __init__(self):
        """
        Initialize the controller in the MVC model, controller has the view and model as variables.
        """
        self.root = tk.Tk()
        self.plotStat = StatisticPlot.plotStat(self.root)
        self.view = GameView(self.root, self)
        self.model = GameModel(self)
        # Pass to view links on root frame and controller object

        self.root.mainloop()

    def btn1_click(self):
        """
        Start manual game is player press the first door
        :return: None
        """
        self.model.door_selection(0)

    def btn2_click(self):
        """
        Start manual game is player press the second door
        :return: None
        """
        self.model.door_selection(1)

    def btn3_click(self):
        """
        Start manual game is player press the third door
        :return: None
        """
        self.model.door_selection(2)

    def btn_change_lbl(self, index, str):
        """
        Change the label of the door that correspond with the index variable.
        :param index: index that correspond with the door label.
        :param str: what the label should say.
        :return: None
        """
        self.view.btns[index]["text"] = str

    def toplbl_change_lbl(self, str):
        """
        Changing the top label that in-charge of the instructions for the player
        :param str: What the label should say.
        """
        self.view.toplbl["text"] = str

    def stats_change_lbl(self, wins, losses):
        """
        Changing the statistics base on the win/loses

        :param wins: Total wins.
        :param losses: Total loses.
        :var winrate: Winrate percentage.
        :var sumstats: Total games.
        """
        sumstats = wins + losses
        winrate = (wins / sumstats) * 100 if sumstats != 0 else 0

        self.view.winslbl["text"] = "Wins: {wins}".format(wins=wins)
        self.view.losseslbl["text"] = "Losses: {losses}".format(losses=losses)
        self.view.winratelbl["text"] = "Win Rate: {winrate}%".format(winrate=round(winrate, 2))
        self.view.totalgames["text"] = "Total games played: {sumstats}".format(sumstats=sumstats)

    def stats_change_lbl_simulate(self, wins, losses, changedoor):
        """
        Changing labels when simulating games

        :param wins: how many wins in that simulation.
        :param losses: how many losses in that simulation.
        :param changedoor: how many times the door changes.
        :return: None
        """
        self.stats_change_lbl(wins, losses)
        self.view.changedoorlbl["text"] = f"The door changed randomly: {changedoor} times".format(changedoor=changedoor)
        self.plotStat.update(wins, losses)
        self.plotStat.showPlot(self.root)

    def btn_change_image(self, index, photo):
        """
        Change the photo of the door bases of the game.

        :param index: index of the door that needs to be changed.
        :param photo: what photo the door should change to.
        :return: None.
        """
        self.view.btns[index].config(image=photo)

    def btn_reset_lbls(self):
        """
        reset all the buttons

        :return: None
        """
        for i, btn in enumerate(self.view.btns):
            btn["text"] = i
        self.view.toplbl["text"] = "Pick one of three doors"

    def simulate(self, changedoor, iter):
        """
        Handles the simulation button.

        :param changedoor: radio button selection.
        :param iter: How many iterations the simulation should make.
        :return: None
        """
        try:
            iter = int(iter)
        except ValueError:
            self.view.change_exceptionlbl('Iterations needs to be an integer')
            return
        if iter > 1000000 or iter <= 0:
            self.view.change_exceptionlbl('Iterations needs to be in range from 1 to 1,000,000')
            return
        self.btn_reset_game()
        self.change_scale(1200, 500)
        if changedoor == 0:
            self.model.simulateWithChange(iter)
        elif changedoor == 1:
            self.model.simulateWithNoChange(iter)
        else:
            self.model.simulateWithRandChange(iter)

    def btn_reset_game(self):
        """
        Handles the reset button press.

        :return: None
        """
        self.model.reset_stats()
        self.view.change_exceptionlbl('')

    def change_doorlbl(self, i, str):
        """
        Changing a certain door label.

        :param i: What label should be change.
        :param str: What the label should say.
        :return: None
        """
        self.view.doorlbls[i]["text"] = str

    def change_scale(self, width, height):
        """
        Changing the window's size.

        :param width: New window's width
        :param height: New window's height
        :return: None.
        """
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(align_str)