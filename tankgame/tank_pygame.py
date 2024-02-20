import pygame
import sys
import math

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

tank_pos = [400, 300]

tank_angle = 0
tank_speed = 2
tank_surface = pygame.Surface((50, 30), pygame.SRCALPHA)  # Use SRCALPHA for transparency support
tank_surface.fill(GREEN)  # Fill the tank's surface with a color
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        tank_angle -= tank_speed
    if keys[pygame.K_RIGHT]:
        tank_angle += tank_speed

    screen.fill(BLACK)
    #tank_surface = pygame.Surface((50, 30))
    tank_surface.fill(GREEN)

    rotated_tank = pygame.transform.rotate(tank_surface, tank_angle)
    rect = rotated_tank.get_rect(center=tank_pos)
    screen.blit(rotated_tank, rect.topleft)

    pygame.display.flip()


    clock.tick(60)

pygame.quit()
sys.exit()
