#START
import pygame
import random


COLOR_CHANGE = pygame.USEREVENT + 1

def main():
    pygame.init()
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('two sprites with color change event')

    colors = {
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'blue': pygame.Color('blue'),
        'yellow': pygame.Color('yellow'),
        'white': pygame.Color('white')
    }
    color_list = list(colors.values())

    
    sprite1 = pygame.Rect(30, 30, 60, 60)
    sprite2 = pygame.Rect(200, 200, 60, 60)

    color1 = colors['white']
    color2 = colors['white']

    clock = pygame.time.Clock()

    
    pygame.time.set_timer(COLOR_CHANGE, 2000)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == COLOR_CHANGE:
                
                color1 = random.choice(color_list)
                color2 = random.choice(color_list)

        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_LEFT]: sprite1.x -= 3
        if pressed[pygame.K_RIGHT]: sprite1.x += 3
        if pressed[pygame.K_UP]: sprite1.y -= 3
        if pressed[pygame.K_DOWN]: sprite1.y += 3

        
        if pressed[pygame.K_a]: sprite2.x -= 3
        if pressed[pygame.K_d]: sprite2.x += 3
        if pressed[pygame.K_w]: sprite2.y -= 3
        if pressed[pygame.K_s]: sprite2.y += 3

       
        for sprite in [sprite1, sprite2]:
            sprite.x = min(max(0, sprite.x), screen_width - sprite.width)
            sprite.y = min(max(0, sprite.y), screen_height - sprite.height)

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, color1, sprite1)
        pygame.draw.rect(screen, color2, sprite2)
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()


if __name__ == "__main__":
    main()
#END