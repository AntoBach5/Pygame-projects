import pygame
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Flappy bird in nature :)")

background_image = pygame.transform.scale(pygame.image.load("nature_background.jpeg").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))


flappy_bird1 = pygame.transform.scale(pygame.image.load("flappy_bird.png").convert_alpha(), (200, 200))
flappy_zone1 = flappy_bird1.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

flappy_bird2 = pygame.transform.scale(pygame.image.load("flappy_bird.png").convert_alpha(), (200, 200))
flappy_zone2 = flappy_bird2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))

flappy_bird3 = pygame.transform.scale(pygame.image.load("flappy_bird.png").convert_alpha(), (200, 200))
flappy_zone3 = flappy_bird3.get_rect(center=(SCREEN_WIDTH // 4 * 3, SCREEN_HEIGHT // 2))


text = pygame.font.Font(None, 36).render("Flappy Birds 1, 2, & 3!", True, pygame.Color("green"))
text_zone = text.get_rect(center=(SCREEN_WIDTH // 7, SCREEN_HEIGHT // 8))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        surface.blit(background_image, (0, 0))
        
        surface.blit(flappy_bird1, flappy_zone1)
        surface.blit(flappy_bird2, flappy_zone2)
        surface.blit(flappy_bird3, flappy_zone3)
        
        surface.blit(text, text_zone)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    game_loop()