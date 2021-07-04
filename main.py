import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")  # Game Window name

Vel = 5  # Velocity
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TILESIZE = 32


class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, TILESIZE, TILESIZE)
        self.color = WHITE
        self.key_pressed = pygame.key.get_pressed()

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.color, self.rect)

    def movement(self):
        if self.key_pressed[pygame.K_LEFT]:
            self.x -= Vel

player = Player(WIDTH / 2, HEIGHT / 2)

'''

testbox = pygame.Rect(WIDTH/2, HEIGHT/2, TILESIZE, TILESIZE)

def movement(key_pressed, testbox):
    if key_pressed[pygame.K_LEFT] and not key_pressed[pygame.K_UP] and not key_pressed[pygame.K_DOWN]:
        testbox.x -= Vel
    if key_pressed[pygame.K_RIGHT] and not key_pressed[pygame.K_UP] and not key_pressed[pygame.K_DOWN]:
        testbox.x += Vel
    if key_pressed[pygame.K_UP] and not key_pressed[pygame.K_LEFT] and not key_pressed[pygame.K_RIGHT]:
        testbox.y -= Vel
    if key_pressed[pygame.K_DOWN] and not key_pressed[pygame.K_LEFT] and not key_pressed[pygame.K_RIGHT]:
        testbox.y += Vel

'''

def main():
    # game clock
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key_pressed = pygame.key.get_pressed()
        WIN.fill(BLACK)
        player.draw(WIN)
        player.movement()
        #pygame.draw.rect(WIN, WHITE, testbox)
        #movement(key_pressed, testbox)
        pygame.display.update()

    pygame.quit()
    sys.exit()


# this checks the name of the file and lets the interpreter know that the main function
# should only be run if this is the main file and not being imported
if __name__ == "__main__":
    main()
