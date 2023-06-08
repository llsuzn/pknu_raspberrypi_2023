# Pygame 드로잉 에디터
import pygame, sys

width, height = 500, 500
radius = 10
mX, mY = 0, 0

pygame.init()
wnd = pygame.display.set_mode((width,height))
wnd.fill(pygame.Color(255,255,255)) # white
fps = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button ==3:
                wnd.fill(pygame.Color(255,255,255))
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()      

        mX,mY = pygame.mouse.get_pos()
        b = pygame.mouse.get_pressed()
        if b[0] == 1:
            pygame.draw.circle(wnd,pygame.Color(255,0,0),
                               (mX,mY) , radius, radius)
    pygame.display.update()
    fps.tick(30)                