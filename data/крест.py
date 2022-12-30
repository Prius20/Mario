import pygame
from random import randint

a, hue = 100, 100
pygame.init()
pygame.display.set_caption("Куб")
size = w, h = a * 3, a * 3
screen = pygame.display.set_mode(size)
screen.fill("black")
c = (hue % 256, 100, 100)
c = pygame.Color("red")  # hue
pygame.draw.rect(screen, c, (w // 4, h // 2, a, a), 0)
pygame.draw.polygon(screen, pygame.Color("orange"),
                    ((w // 4, h // 2),
                     (w // 4 + a, h // 2),
                     (w // 4 + a + a // 2, h // 2 - a * 1 // 4),
                     (w // 4 + a // 2, h // 2 - a * 1 // 4)), 0)
pygame.draw.polygon(screen, pygame.Color("brown"),
                    ((w // 4 + a, h // 2),
                     (w // 4 + a, h // 2 + a),
                     (w // 4 + a + a // 2, h // 2 - a * 1 // 4 + a),
                     (w // 4 + a + a // 2, h // 2 - a * 1 // 4)), 0)

pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()