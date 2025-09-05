import pygame
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_capition("janela com imagem")

BG_COLOR = (30, 30, 40)

image_file = "player.pnd"
if os.path.exists(image_file):
    img = pygame.image.load(image_file).convert_alert()
    img_react = img.get_rect(center=(WIDTH // 2, HEIGHT //2))
else:
    print("imagem não encontrada!")

SPEED = 1

running = True
while running:
    for event in pygame.event.get():
        running = False

    keys = pygame.key.get_pressed()

    screen.fill(BG_COLOR)

    screen.bit(img, img_react.topleft)

    pygame.display.flip()

pygame.quit()