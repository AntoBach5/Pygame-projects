import pygame, random, time
pygame.init()

RESPAWN_EVENT = pygame.USEREVENT + 1
RED_LIGHT_EVENT = pygame.USEREVENT + 2
YELLOW_LIGHT_EVENT = pygame.USEREVENT + 3
GREEN_LIGHT_EVENT = pygame.USEREVENT + 4

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Traffic Light Simulation")

#Traffic lights colors:
RED = pygame.Color("red")
YELLOW = pygame.Color("yellow")
GREEN = pygame.Color("green")

ROAD_COLOR = (80, 80, 80)

#Cars color options:
LIGHT_BLUE = pygame.Color("lightblue")
LIGHT_GREEN = pygame.Color("lightgreen")
PURPLE = pygame.Color("purple")
BLUE = pygame.Color("blue")
ORANGE = pygame.Color("orange")

#Sprite class representing moving object
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        
        #Sprite rectangle and color filling it
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        #Sprite rectangle for knowing the position and colission of the sprite
        self.rect = self.image.get_rect()
        
    def update(self):
        #move_ip = move in place, moves the rectangle by the velocity
        self.rect.move_ip(self.velocity)
        boundry_hit = False
            
        if self.rect.bottom >= 500:
            boundry_hit = True
        
        #Calls/orders the event of changing color
        if boundry_hit:
            pygame.event.post(pygame.event.Event(RESPAWN_EVENT))
    
    #Color changing action        
    def change_color(self):
        self.image.fill(random.choice([PURPLE, LIGHT_BLUE, LIGHT_GREEN, BLUE, ORANGE]))

all_sprites_group = pygame.sprite.Group()

car_starting_position = (100, 0)

#initial positioning of the sprite
Car1 = Sprite(BLUE, 40, 30)
Car1.rect.x = car_starting_position[0]
Car1.rect.y = car_starting_position[1]
Car1.velocity = [0, 5]
all_sprites_group.add(Car1)

red_value = False
yellow_value = False
green_value = False

#Initial image design
screen.fill((ROAD_COLOR))
pygame.draw.rect(screen, (255, 255, 255), (50, 307, 170, 10))
STOP_LINE_Y = 307

pygame.draw.circle(screen, RED, (400, 150), 50, 3)

text = pygame.font.Font(None, 36).render("Use A, S, D", True, pygame.Color("green"))
text_zone = text.get_rect(center=(screen_width // 2, screen_height // 8))

pygame.draw.circle(screen, YELLOW, (400, 255), 50, 3)
pygame.draw.circle(screen, GREEN, (400, 360), 50, 3)
pygame.display.update()

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                pygame.event.post(pygame.event.Event(RED_LIGHT_EVENT))
            elif event.key == pygame.K_s:
                pygame.event.post(pygame.event.Event(YELLOW_LIGHT_EVENT))
            elif event.key == pygame.K_d:
                pygame.event.post(pygame.event.Event(GREEN_LIGHT_EVENT)) 
            
        elif event.type == RESPAWN_EVENT:
            Car1.rect.x = car_starting_position[0]
            Car1.rect.y = car_starting_position[1]
            Car1.change_color()
            
        elif event.type == RED_LIGHT_EVENT:
            red_value = True
            yellow_value = False
            green_value = False
        elif event.type == YELLOW_LIGHT_EVENT:
            red_value = False
            yellow_value = True
            green_value = False
        elif event.type == GREEN_LIGHT_EVENT:
            red_value = False
            yellow_value = False
            green_value = True
            
    if red_value:
        if Car1.rect.bottom < STOP_LINE_Y:
            Car1.velocity = [0, 5]
        elif Car1.rect.bottom >= STOP_LINE_Y and Car1.rect.top < STOP_LINE_Y:
            Car1.rect.bottom = STOP_LINE_Y
            Car1.velocity = [0, 0]
    elif yellow_value:
        Car1.velocity = [0, 2]
    elif green_value:
        Car1.velocity = [0, 5]
    
    all_sprites_group.update()
    screen.fill(ROAD_COLOR)
    all_sprites_group.draw(screen)
    pygame.draw.rect(screen, (255, 255, 255), (50, 307, 170, 10))

    if red_value == True: 
        pygame.draw.circle(screen, RED, (400, 150), 50)
        Car1.velocity = [0, 0]
    else: pygame.draw.circle(screen, RED, (400, 150), 50, 3)
    if yellow_value == True: 
        pygame.draw.circle(screen, YELLOW, (400, 255), 50)
        Car1.velocity = [0, 2]
    else: pygame.draw.circle(screen, YELLOW, (400, 255), 50, 3)
    if green_value == True: 
        pygame.draw.circle(screen, GREEN, (400, 360), 50)
        Car1.velocity = [0, 5]
    else: pygame.draw.circle(screen, GREEN, (400, 360), 50, 3)
    
    screen.blit(text, text_zone)
    pygame.display.flip()
    clock.tick(50)
    
    
pygame.quit()