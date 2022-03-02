import pygame
import math
from planet import Planet

pygame.init()
# WINDOW SETUP
WIDTH, HEIGHT = 800, 800
WIN_SIZE = (WIDTH, HEIGHT)
WIN = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption("Planet Simulation")

# physically accurate in order from the sun
# mass of each planet in kg
SUN_MASS = 1.989e30
MERCURY_MASS = 3.285e23
VENUS_MASS = 4.867e24
EARTH_MASS = 5.972e24
MARS_MASS = 6.39e23
MOON_MASS = 7.342*10e22

# velocity of each planet in m/s
MERCURY_VELOCITY = 47.36e3
VENUS_VELOCITY = 35.02e3
EARTH_VELOCITY = 29.78e3
MARS_VELOCITY = 24.1e3
MOON_VELOCITY = 1.022e3

# colors in rgb
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
LIGHT_GRAY = (136, 136, 136)
DARK_GRAY = (80, 78, 81)


def main():
    run = True
    clock = pygame.time.Clock()  # to limit how many times a second our game will refresh

    # planets
    sun = Planet(0, 0, 30, YELLOW, SUN_MASS)
    sun.sun = True

    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GRAY, MERCURY_MASS)
    mercury.y_vel = -MERCURY_VELOCITY

    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, VENUS_MASS)
    venus.y_vel = -VENUS_VELOCITY

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, EARTH_MASS)
    earth.earth = True
    earth.y_vel = EARTH_VELOCITY

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, MARS_MASS)
    mars.y_vel = MARS_VELOCITY
    #
    # moon = Planet(-1 * Planet.AU, 10, 10, LIGHT_GRAY, MOON_MASS)
    # moon.y_vel = MOON_VELOCITY

    planets = [sun, mercury, venus, earth, mars]
    while run:
        clock.tick(60)  # limited to "60" Hz
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
