import pygame
from constants import *
from player import *
from asteroidfield import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroids.containers = (asteroids,updatable,drawable)

    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        dt = clock.tick(60)/1000

        #here is where the player values are being updated every frame
        updatable.update(dt)
        
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
