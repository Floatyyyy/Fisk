import vector as v
import fisk as f
import pygame
pygame.init()


screen = pygame.display.set_mode((800, 600))

#Fish
playerimg = pygame.image.load('player.png')
Pos = v.Vector(370, 480)
Vel = v.Vector(0, 0)

f.Fisk(Pos,Vel,screen)

# Update and draw the fish
fish = f.Fisk(Pos, Vel,)
fish.update()     
fish.draw()

running = True
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT():
         running = False

pygame.display.update()

pygame.quit()