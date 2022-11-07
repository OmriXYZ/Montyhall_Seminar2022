import pygame
from pygame.mixer import Sound

pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
pygame.mixer.init()


class SoundManager:
    def __init__(self):
        self.click = Sound("sounds/Mouse-Click.mp3")
        self.goat = Sound("sounds/Goat-screaming-sound-effect.mp3")
        self.lose = Sound("sounds/lose.mp3")
        self.win = Sound("sounds/win.mp3")
        ##self.resets = Sound("sounds/reset.mp3")
        self.choose = Sound("sounds/choose-option.mp3")

        self.click.set_volume(0.3)
        self.goat.set_volume(0.3)
        self.lose.set_volume(0.3)
        self.win.set_volume(0.3)
        self.choose.set_volume(0.3)
