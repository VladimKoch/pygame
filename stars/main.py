import pygame
import time
import random

pygame.font.init()

WIDTH, HEIGHT = 1000,750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Dodge")
BG =  pygame.transform.scale(pygame.image.load("bgspace.jpg"),(WIDTH,HEIGHT))

# SHIP = pygame.transform.scale(pygame.image.load("rocket.jpg"), (20,20))

PLAYER_WIDTH = 30
PLAYER_HEIGHT = 60
PLAYER_VELOCITY = 5

SHOT_WIDTH = 20
SHOT_HEIGHT = 20
SHOT_VELOCITY = 10

STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VELOCITY = 2

FONT = pygame.font.SysFont("comicsans",30)



def draw(player,elapsed_time,stars):
    WIN.blit(BG,(0,0))
    
    time_text = FONT.render(f"Time: {round(elapsed_time)}s",1,"white")
    WIN.blit(time_text,(10,10))
    
    pygame.draw.rect(WIN,"green",player)
    
    for star in stars:
        pygame.draw.rect(WIN,"white",star)
    
    
    
    pygame.display.update()


    


def main():
    run = True
    
    player = pygame.Rect(500,HEIGHT - PLAYER_HEIGHT,PLAYER_WIDTH,PLAYER_HEIGHT)
    
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    
    star_add_increment = 2000
    star_count = 0
    
    shot = ""
    
    stars = []
    hit = False
    
    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0,WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH,SHOT_HEIGHT)
                stars.append(star)
                
                
            star_add_increment = max(200,star_add_increment - 50)    
            star_count = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >=0:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + player.width <=WIDTH:
            player.x += PLAYER_VELOCITY
        if keys[pygame.K_UP] and player.y - PLAYER_VELOCITY >=0:
            player.y -= PLAYER_VELOCITY
        if keys[pygame.K_DOWN] and player.y + PLAYER_VELOCITY + player.height <=HEIGHT:
            player.y += PLAYER_VELOCITY
        
        
        for star in stars[:]:
            star.y += STAR_VELOCITY
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
            
        if hit:
            lost_text = FONT.render("You Lost! ",1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
            

        
        # print(f"Pozice rectanglu : x={player.x}, y={player.y}")
        draw(player,elapsed_time,stars)
    
    pygame.quit()
if __name__ == "__main__":
    main()
