import random

class Settings:
    """ organize game settings """


    def __init__(self):
        """ initialize game settings """
        
        # screen color
        self.bg_color = (20, 50, 90)
        self.screen_width = 400
        self.screen_height = 600

        self.direction_list = [1, -1]

        self.screen_rows = self.screen_height / 12

        self.enemy_speed = 1
        self.enemy_direction = 1 #random.choices(self.direction_list)


        #self.enemy_random_placement = 100