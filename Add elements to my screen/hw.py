import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame Screen")

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    pygame.draw.rect(screen, red, (50, 50, 100, 75))

    font = pygame.font.Font(None, 36)
    text_surface = font.render("Hello Pygame!", True, blue)
    screen.blit(text_surface, (200, 100))

    pygame.display.flip()

pygame.quit()