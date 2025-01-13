import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for thing in updatable:
            thing.update(dt)
        for asteroid in asteroids:
            if asteroid.is_colliding(player_1):
                print("Game over")
                sys.exit()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()