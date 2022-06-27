import sys
from tracemalloc import start
import pygame
from settings import *

pygame.init()
vec=pygame.math.Vector2


class App:
    def __init__(self):
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock=pygame.time.Clock()
        self.running=True
        self.intro='intro'
        self.state='start'

    def run(self):
        while self.running:
            if self.state=='inttro':
                self.start_events()
                self.start_update()
                self.start_draw()
            self.clock.tick(FPS)
            pygame.quit()
            sys.exit()

    def start_events(self):
        for event in pygame.event.get():
            if event.typr==pygame.QUIT:
                self.running=False
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                self.state='playing'
    def start_update(Self):
        pass
    def start_draw(Self):
        self.screen.fill(BLACK)
        pygame.display.update()