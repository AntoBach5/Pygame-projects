import pygame

def main():
    pygame.init()
    
    screen_width = 500
    screen_height = 500
    
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    pygame.display.set_caption("Move with 'arrow keys' and 'WASD' keys")
    
    colours = {
        "red": pygame.Color("red"),
        "green": pygame.Color("green"),
        "blue": pygame.Color("blue"),
        "yellow": pygame.Color("yellow"),
        "cyan": pygame.Color("cyan"),
    }
    
    current_colour = colours["cyan"]
    
    x, y = 30, 30
    sprite_width, sprite_height = 60, 60
    
    x2, y2 = 400, 400
    sprite_width2, sprite_height2 = 60, 60
    
    clock = pygame.time.Clock()
   
    done = False
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_RIGHT]: x += 15
            if pressed[pygame.K_LEFT]: x -= 15
            if pressed[pygame.K_UP]: y -= 15
            if pressed[pygame.K_DOWN]: y += 15
            
            if pressed[pygame.K_d]: x2 += 15
            if pressed[pygame.K_a]: x2 -= 15
            if pressed[pygame.K_w]: y2 -= 15
            if pressed[pygame.K_s]: y2 += 15
            
            x = min(max(0, x), screen_width - sprite_width)
            y = min(max(0, y), screen_height - sprite_height)
            
            if x == 0:
                current_colour = colours["red"]
            elif x == screen_width - sprite_width:
                current_colour = colours["green"]
            elif y == 0:
                current_colour = colours["blue"]
            elif y == screen_height - sprite_height:
                current_colour = colours["yellow"]
            else:
                current_colour = colours["cyan"]
            
            x2 = min(max(0, x2), screen_width - sprite_width2)
            y2 = min(max(0, y2), screen_height - sprite_height2)
                        
            if x2 == 0:
                current_colour2 = colours["red"]
            elif x2 == screen_width - sprite_width2:
                current_colour2 = colours["green"]
            elif y2 == 0:
                current_colour2 = colours["blue"]
            elif y2 == screen_height - sprite_height2:
                current_colour2 = colours["yellow"]
            else:
                current_colour2 = colours["cyan"]
            
            screen.fill((200, 200, 200))
            pygame.draw.rect(screen, current_colour, pygame.Rect(x, y, sprite_width, sprite_height))
            pygame.draw.rect(screen, current_colour2, pygame.Rect(x2, y2, sprite_width2, sprite_height2), 3)
            
            pygame.display.flip()
            clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()