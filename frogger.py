import pygame
import sys
import random
from settings import Settings
from player import Player
from enemy import Enemy

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

        self.player = Player(self)

         # enemy group
        self.enemys = pygame.sprite.Group()


        self.clock = pygame.time.Clock()

        self._create_enemys()



    def run_game(self):
        """ main loop """
        while True:
            self.clock.tick(60)
            self._check_events()
            self._update_enemy()
            # update the screen
            self._update_screen()



    def _check_events(self):
        """ check for events """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)



    def _check_keydown_events(self, event):
        """ check for and respond to player input """
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.player.move_forward()
        elif event.key == pygame.K_DOWN:
            self.player.move_backward()



    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.player.check_position()



    def _create_enemys(self):
        """ creates amount of enemys """
        enemy = Enemy(self)

        enemy_width, enemy_height = enemy.rect.size

        for row_number in range(1, 3):
            self._create_enemy(row_number)

        
    def _create_enemy(self, row_number):
        """ creats enemy sprite and location """
        enemy = Enemy(self)
        # added the random speed calulation at the creation of the individual enemy 
        # duh why the F did i not think of that 
        enemy.speed = random.randint(2, 5)
        enemy.y = row_number * 100
        # speed
        enemy.x = self.settings.enemy_direction * self.settings.enemy_speed + random.randint(20, 200)
        enemy.rect.x = enemy.x
        enemy.rect.y = enemy.y
        self.enemys.add(enemy)

    def _update_enemy(self):
        """ enemy update """
        self.enemys.update()
        self._check_enemy_edges()

    def _check_enemy_edges(self):
        for enemy in self.enemys.sprites():
            if enemy.check_edges():
                  self._change_enemy_direction()

    def _update_screen(self):
        """ things to be update """

        # set the window background color
        self.screen.fill(self.settings.bg_color)

        # display player
        self.player.blitme()

        # draw enemies
        self.enemys.draw(self.screen)


        # draw a new screen
        pygame.display.flip()



if __name__ == '__main__':
    frogger = Frogger()
    frogger.run_game()