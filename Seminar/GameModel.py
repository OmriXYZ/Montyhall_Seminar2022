import random
from tkinter import PhotoImage
from SoundManager import SoundManager
import pygame
from pygame.mixer import Sound
pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
pygame.mixer.init()


class GameModel:
    def __init__(self, controller):
        self.controller = controller
        self.soundManger = SoundManager()
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
            self.reset_game()
            self.soundManger.goat.stop()
            self.soundManger.win.stop()
            self.soundManger.lose.stop()
            return
        if self.stage == 1:
            if door_index == self.l2[0]:
                print("You cant choose goat in number: ", self.l2[0])
                return
            elif door_index == self.ci:
                self.soundManger.click.play()
                self.controller.toplbl_change_lbl("You Win the car, tap any door to play again")
                self.controller.btn_change_image(self.ci, self.car_photo)
                self.wins += 1
                self.soundManger.win.play()
            else:
                self.soundManger.click.play()
                self.controller.toplbl_change_lbl("You choose the goat again, you lose, tap any door to play again")
                self.controller.btn_change_image(door_index, self.goat_photo)
                self.losses += 1
                self.soundManger.lose.play()

            self.stage += 1

            self.controller.stats_change_lbl(self.wins, self.losses)
            # print("ratio: ", self.wins/self.losses)
            return
        if self.stage == 0:
            self.soundManger.click.play()
            for i in range(len(self.l1)):
                if i != self.ci and i != door_index:
                    self.l2.append(i)
            if self.l2 == 2:
                random.shuffle(self.l2)
            self.controller.toplbl_change_lbl("There is a goat in: {door}\nDo you want to keep your choice or change it?".format(door=self.l2[0]))
            self.controller.btn_change_image(self.l2[0], self.goat_photo)
            self.controller.btn_change_lbl(self.l2[0], "goat")
            self.soundManger.goat.play()
            self.stage += 1
            self.controller.letPC_do_thechoice()

    def door_selection_simulation(self, door_index):
        if self.stage == 2:
            self.reset_game_simulate()
            return
        if self.stage == 1:
            if door_index == self.ci:
                self.wins += 1
            else:
                self.losses += 1
            self.stage += 1
            return
        if self.stage == 0:
            for i in range(len(self.l1)):
                if i != self.ci and i != door_index:
                    self.l2.append(i)
            # if len(self.l2) == 2:
            #     random.shuffle(self.l2)
            self.stage += 1

    def reset_game(self):
        self.l1 = ["goat", "car", "goat"]
        random.shuffle(self.l1)
        self.ci = self.l1.index("car")
        self.l2 = []  # indices that got the goat
        self.controller.btn_reset_lbls()
        for i in range(3):
            self.controller.btn_change_image(i, self.door_photo)
        self.stage = 0

    def reset_stats(self):
        self.reset_game()
        self.wins = 0
        self.losses = 0
        self.controller.stats_change_lbl(0, 0)

    def reset_game_simulate(self):
        self.l1 = ["goat", "car", "goat"]
        random.shuffle(self.l1)
        self.ci = self.l1.index("car")
        self.l2 = []  # indices that got the goat
        self.stage = 0

    def simulate(self, iterations):
        for i in range(iterations):
            choice = random.randint(0, 2)
            self.door_selection(choice)
            while (True):
                choice = random.randint(0, 2)
                if (choice != self.l2[0]):
                    self.door_selection(choice)
                    break
            self.door_selection(choice)

    def simulateWithNoChange(self, iterations):
        for i in range(iterations):
            choice = random.randint(0, 2)
            self.door_selection_simulation(choice)
            self.door_selection_simulation(choice)
            self.door_selection_simulation(choice)
        self.controller.stats_change_lbl(self.wins, self.losses)

    def simulateWithChange(self, iterations):
        for i in range(iterations):
            choice = random.randint(0, 2)
            self.door_selection_simulation(choice)
            for j in range(3):
                if j != choice and j != self.l2[0]:
                    choice = j
                    break
            self.door_selection_simulation(choice)
            self.door_selection_simulation(choice)
        self.controller.stats_change_lbl(self.wins, self.losses)

    def simulateWithRandChange(self, iterations):
        for i in range(iterations):
            choice = random.randint(0, 2)
            self.door_selection_simulation(choice)
            if random.choice([True, False]):
                for j in range(3):
                    if j != choice and j != self.l2[0]:
                        choice = j
                        break
            self.door_selection_simulation(choice)
            self.door_selection_simulation(choice)
        self.controller.stats_change_lbl(self.wins, self.losses)

    def safeRandChoose(self):
        choice = random.randint(0, 2)
        while choice == self.l2[0]:
            choice = random.randint(0, 2)
        self.door_selection(choice)