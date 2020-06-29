import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """ enemy class """

    def __init__(self, frogger):
        """ init enemy """
        super().__init__()
        self.screen = frogger.screen
        self.settings = frogger.settings
        # load our image
        self.image = pygame.image.load('assets/enemy_ship.png')
        # enemy rect
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.enemy_direction = 1
        # add enemy speed here so that it is stored with individual enemies 
        self.speed = 1

        self.x = float(self.rect.x)

    def check_edges(self):
        """ make sure player is in the screen bounds """
        screen_rect = self.screen.get_rect()
        # make it so that the enemy direction is being set and not multiplied on 
        if self.rect.right >= self.screen_rect.right:
            self.enemy_direction = -1
        elif self.rect.left <= 0:
            self.enemy_direction = 1
            

    def update(self):
        """ update the enemy position """
        self.x += (self.speed * self.enemy_direction)
        self.rect.x = self.x