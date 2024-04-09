import pygame
import vector as v



class Fisk:
      def __init__(self, pos, vel, screen):
            self.screen = screen
            self.pos = pos
            self.vel = vel
            self.playerimg = pygame.image.load('clown-fish')

      def update(self):
            self.pos = self.pos + self.vel


      def draw(self):
            self.screen.blit(self.playerimg, (self.pos.x, self.pos.y))
  


