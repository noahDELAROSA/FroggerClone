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
      
        

        self.x = float(self.rect.x)

    def check_edges(self):
        """ make sure player is in the screen bounds """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= 400 or self.rect.left <= 0:
            return True
            

    def update(self, direction):
        """ update the enemy position """
        print(self.x)
        self.x += (self.settings.enemy_speed * direction)
        self.rect.x = self.x