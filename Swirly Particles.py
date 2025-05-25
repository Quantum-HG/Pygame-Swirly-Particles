'''MIT License

Copyright (c) 2025 Harsh Gupta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

import random
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
Clock = pygame.time.Clock()
vec = pygame.Vector2


class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, dir_vec):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.color = (random.choice([0, 255]), random.choice([0, 255]), random.choice([0, 255]))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=pos)
        self.dir = dir_vec
        self.angle = 0
        self.last_time = pygame.time.get_ticks()
        self.kill_time_ms = 900

    def update(self):
        self.angle = (self.angle + 0.1) % 360
        self.dir.rotate_ip(self.angle)
        self.rect.center += self.dir
        now = pygame.time.get_ticks()
        if now - self.last_time > self.kill_time_ms:
            self.kill()


grp = pygame.sprite.Group()
while True:
    screen.fill('black')
    vector = vec(pygame.mouse.get_pos() - vec(0, 300))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if pygame.mouse.get_pressed()[0]:
        for i in range(20):
            grp.add(Particle(pygame.mouse.get_pos(), vec(random.randrange(-4, 4), random.randrange(-4, 4))))

    grp.update()
    grp.draw(screen)

    pygame.display.update()
    Clock.tick(60)
