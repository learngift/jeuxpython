from constant import *

class Hostile_Shoot:
    def __init__(self, ship, player):
        self.x = ship.x + 32
        self.y = ship.y + 32
        self.angle = math.atan2(player.y-self.y, player.x-self.x)

    def update(self):
        self.x += 5 * math.cos(self.angle)
        self.y += 5 * math.sin(self.angle)

    def on_screen(self):
        return (0 < self.x < WIDTH) and (0 < self.y < HEIGHT)