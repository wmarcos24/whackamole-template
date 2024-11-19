import pygame
import random

from pygame import MOUSEBUTTONDOWN


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole = (0,0)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            mole = mole
            screen.fill("light green")

            for i in range(20):
                pygame.draw.line(screen, "purple", (i*32,0), (i*32, 512))

            for i in range(16):
                pygame.draw.line(screen, "purple", (0,i*32), (640,i*32))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole[0], mole[1])))

            pygame.display.flip()
            clock.tick(60)

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0] // 32
                y = event.pos[1] // 32

                if x == mole[0]//32 and y == mole[1]//32:
                    mole = (random.randrange(0, 19)*32, random.randrange(0, 15)*32)
                    screen.blit(screen, screen.get_rect(topleft=(mole[0], mole[1])))
                pygame.display.update()




    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
