import random
from tkinter import PhotoImage
import matplotlib as mp
import numpy as np

class GameModel:
    def __init__(self, controller):
        self.controller = controller

        self.l1 = ["goat", "car", "goat"]
        random.shuffle(self.l1)
        self.ci = self.l1.index("car")
        self.l2 = []  # indices that got the goat
        self.stage = 0
        self.wins = 0
        self.losses = 0

        self.goat_photo = PhotoImage(file="goat2.png")
        self.car_photo = PhotoImage(file="car.png")
        self.door_photo = PhotoImage(file="door.png")

        for i in range(3):
            self.controller.btn_change_image(i, self.door_photo)

    def door_selection(self, door_index):

        if self.stage == 2:
            self.stage = 0
            self.reset_game()
            return

        if self.stage == 1:
            if door_index == self.l2[0]:
                print("You cant choose goat in number: ", self.l2[0])
                return
            elif door_index == self.ci:
                self.controller.toplbl_change_lbl("You Win the car, tap any door to play again")
                self.controller.btn_change_image(self.ci, self.car_photo)
                self.wins += 1
            else:
                self.controller.toplbl_change_lbl("You choose the goat again, you lose, tap any door to play again")
                self.controller.btn_change_image(door_index, self.goat_photo)
                self.losses += 1

            self.stage += 1

            self.controller.stats_change_lbl(self.wins, self.losses)
            # print("ratio: ", self.wins/self.losses)
            return
        if self.stage == 0:
            for i in range(len(self.l1)):
                if i != self.ci and i != door_index:
                    self.l2.append(i)
            if self.l2 == 2:
                random.shuffle(self.l2)
            self.controller.toplbl_change_lbl("There is a goat in: {door}\nDo you want to keep your choice or change it?".format(door=self.l2[0]))
            self.controller.btn_change_image(self.l2[0], self.goat_photo)
            self.controller.btn_change_lbl(self.l2[0], "goat")
            self.stage += 1

    def reset_game(self):
        self.l1 = ["goat", "car", "goat"]
        random.shuffle(self.l1)
        self.ci = self.l1.index("car")
        self.l2 = []  # indices that got the goat
        self.controller.btn_reset_lbls()
        for i in range(3):
            self.controller.btn_change_image(i, self.door_photo)

    def simulate(self):
        for i in range(100):
            self.door_selection()
