import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot



def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    # player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # asteroids
    Asteroid.containers = (asteroids, updatable, drawable)
    # asteroid field
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    # shot
    Shot.containers = (shots, updatable, drawable)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for drawablee in drawable:
            drawablee.draw(screen)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
