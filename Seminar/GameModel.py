import random
from tkinter import PhotoImage
from SoundManager import SoundManager
import pygame
pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
pygame.mixer.init()


class GameModel:
    def __init__(self, controller):
        """
        initialize Game model variables
        """
        self.controller = controller
        self.soundManger = SoundManager()
        self.l1 = ["goat", "car", "goat"]
        random.shuffle(self.l1)
        self.ci = self.l1.index("car")
        self.l2 = []  # indices that got the goat
        self.stage = 0
        self.wins = 0
        self.losses = 0
        self.sim_changedoor = 0
        self.firstChoiceIndex = 0

        self.lastGameFlag = False;

        self.goat_photo = PhotoImage(file="images/goat.png")
        self.car_photo = PhotoImage(file="images/car.png")
        self.door_photo = PhotoImage(file="images/door.png")

        for i in range(3):
            self.controller.btn_change_image(i, self.door_photo)

    def door_selection(self, door_index):
        """
        Algorithm for the manual game option in the program, determined what happens each round.
        :param door_index: index that determined what door the player picked each round
        :return: None
        """
        if self.stage == 2:
            self.reset_game()
            self.soundManger.goat.stop()
            self.soundManger.win.stop()
            self.soundManger.lose.stop()
            return
        if self.stage == 1:
            # self.controller.delete_btn_letChoiceToPC()
            if door_index == self.l2[0]:
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
            if self.firstChoiceIndex == door_index:
                self.controller.change_doorlbl(door_index, "First Choice\nSecond Choice")
            else:
                self.controller.change_doorlbl(door_index, "Second Choice")
            self.controller.stats_change_lbl(self.wins, self.losses)
            # print("ratio: ", self.wins/self.losses)
            return
        if self.stage == 0:
            if self.lastGameFlag:
                self.controller.btn_reset_game()
                self.lastGameFlag = False
                self.controller.change_scale(700, 500)
            self.soundManger.click.play()
            for i in range(len(self.l1)):
                if i != self.ci and i != door_index:
                    self.l2.append(i)
            if self.l2 == 2:
                random.shuffle(self.l2)
            self.controller.toplbl_change_lbl("Do you want to keep your choice or change it?")
            self.controller.btn_change_image(self.l2[0], self.goat_photo)
            self.controller.btn_change_lbl(self.l2[0], "goat")
            self.controller.change_doorlbl(door_index, "First Choice")
            self.controller.change_doorlbl(self.l2[0], "There is a goat here")
            self.soundManger.goat.play()
            self.stage += 1
            self.firstChoiceIndex = door_index
            # self.controller.letPC_do_thechoice()

    def door_selection_simulation(self, door_index):
        """
        Algorithm for the automatic game option in the program, determined what happens each round.
        :param door_index: index that determined what door the simulation picked each round
        :return: None
        """
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
            self.lastGameFlag = True
            for i in range(len(self.l1)):
                if i != self.ci and i != door_index:
                    self.l2.append(i)
            # if len(self.l2) == 2:
            #     random.shuffle(self.l2)
            self.stage += 1

    def reset_game(self):
        """
        Reset game variables and UI.
        :return: None
        """
        self.l1 = ["goat", "car", "goat"]
        random.shuffle(self.l1)
        self.ci = self.l1.index("car")
        self.l2 = []  # indices that got the goat
        self.controller.btn_reset_lbls()
        for i in range(3):
            self.controller.btn_change_image(i, self.door_photo)
        for i in range(3):
            self.controller.change_doorlbl(i, "")
        self.stage = 0

    def reset_stats(self):
        """
        Reset statistics.
        :return: None
        """
        self.reset_game()
        self.wins = 0
        self.losses = 0
        self.sim_changedoor = 0
        self.controller.stats_change_lbl_simulate(0, 0, 0)

    def reset_game_simulate(self):
        """
        Reset game simulation.
        :return: None
        """
        self.l1 = ["goat", "car", "goat"]
        random.shuffle(self.l1)
        self.ci = self.l1.index("car")
        self.l2 = []  # indices that got the goat
        self.stage = 0

    def simulate(self, iterations):
        for i in range(iterations):
            choice = random.randint(0, 2)
            self.door_selection(choice)
            while True:
                choice = random.randint(0, 2)
                if choice != self.l2[0]:
                    self.door_selection(choice)
                    break
            self.door_selection(choice)

    def simulateWithNoChange(self, iterations):
        """
        Simulation with the computer not changing his first selection
        :param iterations: how many iterations
        :return: None
        """
        for i in range(iterations):
            choice = random.randint(0, 2)
            self.door_selection_simulation(choice)
            self.door_selection_simulation(choice)
            self.door_selection_simulation(choice)
        self.controller.stats_change_lbl_simulate(self.wins, self.losses, 0)

    def simulateWithChange(self, iterations):
        """
        Simulation with the computer changing his first selection
        :param iterations: how many iterations
        :return: None
        """
        for i in range(iterations):
            choice = random.randint(0, 2)
            self.door_selection_simulation(choice)
            for j in range(3):
                if j != choice and j != self.l2[0]:
                    choice = j
                    break
            self.door_selection_simulation(choice)
            self.door_selection_simulation(choice)
        self.controller.stats_change_lbl_simulate(self.wins, self.losses, iterations)

    def simulateWithRandChange(self, iterations):
        """
        Simulation with the computer changing or not changing its first selection randomly
        :param iterations: how many iterations
        :return: None
        """
        for i in range(iterations):
            choice = random.randint(0, 2)
            self.door_selection_simulation(choice)
            if random.choice([True, False]):
                self.sim_changedoor += 1
                for j in range(3):
                    if j != choice and j != self.l2[0]:
                        choice = j
                        break
            self.door_selection_simulation(choice)
            self.door_selection_simulation(choice)
        self.controller.stats_change_lbl_simulate(self.wins, self.losses, self.sim_changedoor)