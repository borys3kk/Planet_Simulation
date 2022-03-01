import pygame


class Planet:
    AU = 149.6e6 * 1000  # astronomical unit
    G = 6.67428e-11
    SCALE = 220 / AU
    TIMESTEP = 3600 * 24  # 1 day in seconds
    WIDTH = HEIGHT = 800

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + self.WIDTH // 2
        y = self.y * self.SCALE + self.HEIGHT // 2
        pygame.draw.circle(win, self.color, (x, y), self.radius)
