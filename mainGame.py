from cgitb import text
from doctest import BLANKLINE_MARKER
import enum
import pygame
from pyparsing import DebugExceptionAction

pygame.init()

class Simbol:
    def __init__(self, color, posX, posY, screen, text):
        self.color = color
        self.pos = {
            'x': posX,
            'y': posY
        }

        font = pygame.font.Font("FreeSans.ttf", 32)
        self.text = font.render(text, True, self.color)
        self.screen = screen

    def drawSimbol(self):
        self.screen.blit(self.text, (self.pos['x'], self.pos['y'])) 


def main():
    X = 800
    Y = 500
    RUN  = True
    screen = pygame.display.set_mode((X, Y))

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    text = Simbol(BLACK, 100, 100, screen, "demo")

    clock = pygame.time.Clock()

    while RUN:
        
        clock.tick(30)
        screen.fill(WHITE)

        text.drawSimbol()
        
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                RUN = False

    pygame.display.flip()

if __name__ == "__main__":
    main()
