# This file was created by: Aaron
# Code inspired by game dev Chris Bradfield who was inspired by Notch
 
import pygame as pg
from os import path
from settings import *
#importing settings to change colors and sizes of stuff on screen
from sprites import *
from utils import *
#

'''
Why are we making game a class?
why is it capitalized
what is init
what is pass

Data types: boolean, JSON, strings
Input (event): Keyboard, mouse, right click, voice, gyroscoping, location tracking
    
Process: cursor position, position of player, enemy position, aim in FPS, velocity

Output: Graphics, sound(gunfire, jump, walking, haptics)


'''

"Input (events)"
class Game():
    #initate the game, charactars, etc.
    def __init__ (self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        print("game initialized...")
        pg.display.set_caption(TITLE)
        self.running = True
        self.playing = True
        self.clock = pg.time.Clock()

    def load_data(self, map):
        self.game_dir = path.dirname(__file__)
        self.img_dir = path.join(self.game_dir, 'images')
        self.snd_dir = path.join(self.game_dir, 'audio')
        self.map = Map(path.join(self.game_dir, map))

    
    def new(self):
        self.load_data('level1.txt')
        print(self.map.data)
        self.all_sprites = pg.sprite.Group()
        self.all_walls = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()


        for row, tiles in enumerate(self.map.data):
            for col, tile, in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'M':
                    pass
                    
        for row, tiles in enumerate(self.map.data):
            for col, tile, in enumerate(tiles):
                if tile == 'P':
                    Player(self, col, row)
                    
        


    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
 
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def update(self):
        self.all_sprites.update()
    # creates an output for the screen color
    def draw(self):
        #order matters because bottom things are first to be drawn the last things are drawn on top
        #last lines are drwan on top in this method
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
#runs the game
if __name__ == "__main__":
    g = Game()


 
while g.running:
    g.new()
    g.run()


