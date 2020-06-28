import pygame
import sys
from settings import Settings

class Frogger:
    """ Main Game """



    def __init__(self):
        """ initialize our game variables """
       
        # initialize game
        pygame.init()

        self.settings = Settings()

        # create screen
        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))

        # set caption
        pygame.display.set_caption("CLONE")



    def run_game(self):
        """ main loop """
        while True:
            self._check_events()
            
            # update the screen
            self._update_screen()
            



    def _check_events(self):
        """ check for events """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)



    def _check_keydown_events(self, event):
        """ check for and respond to player input """
        if event.key == pygame.K_q:
            sys.exit()



    def _update_screen(self):
        """ things to be update """

        # set the window background color
        self.screen.fill(self.settings.bg_color)

        # draw a new screen
        pygame.display.flip()



if __name__ == '__main__':
    frogger = Frogger()
    frogger.run_game()