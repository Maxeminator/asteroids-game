import pygame
from constants import *
from circleshape import*
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    
    dt=0

    screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    AsteroidField.containers=(updatable)
    Asteroid.containers=(asteroids,updatable,drawable)
    Player.containers=(updatable,drawable)
    asteroid=Asteroid(SCREEN_WIDTH,SCREEN_HEIGHT,2)
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        updatable.update(dt)

        screen.fill((0,0,0,))

        for draw in drawable:
            draw.draw(screen)

        dt = clock.tick(60)/1000

        pygame.display.flip()
    pygame.quit()
    
if __name__ == "__main__":
    main()