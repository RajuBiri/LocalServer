import pygame 
from network import Network
from player import Player

win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Client")


def redrawWindow(win, player, player2):

    win.fill((0,0,0))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main(): 
    run = True
    n = Network()
    p = n.getP()

    clock = pygame.time.Clock()

    while run:
        p2 = n.send(p)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False 
                pygame.quit()

        p.move()
        redrawWindow(win, p, p2)

        clock.tick(60)

main()