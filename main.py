import pygame
import time
import random
import os
from typing import Optional

pygame.init()
pygame.font.init()

FONT = pygame.font.SysFont("commiscans", 40)
WIDTH, HEIGHT = 1000,750

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space fight")

BG = pygame.transform.scale(pygame.image.load("./Assets/space.png"),(WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)
RED=(255,0,0)
YELLOW = (255,255,0)

BORDER = pygame.Rect(WIDTH//2 - 5,0,10,HEIGHT)

FPS = 60
SHIPS_VELOCIT = 4
BULLET_VELOCITY = 8
MAX_BULLETS = 3



SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

RED_HIT = pygame.USEREVENT + 1 
YELLOW_HIT = pygame.USEREVENT + 2 

RED_CRIT = pygame.USEREVENT + 3 
YELLOW_CRIT = pygame.USEREVENT + 4 

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.png')),(WIDTH,HEIGHT))


YELLOW_SPACESHIP_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets','spaceship_yellow.png')),(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
RED_SPACESHIP_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets','spaceship_red.png')),(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))    


RED_SPACESHIP_IMAGE = pygame.transform.rotate(RED_SPACESHIP_IMAGE,90)
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(YELLOW_SPACESHIP_IMAGE,270)

# def space_ship_angle_yellow(angle_yellow):
    

# print(YELLOW_SPACESHIP_IMAGE)

def draw_window(red,yellow,red_bullets,yellow_bullets,hp):
    display_duration = 3000
    # duration = True
    
    # Vykreslení bagroundy 
    WIN.blit(SPACE,(0,0))
    # Vykreslení dělící čáry
    pygame.draw.rect(WIN,BLACK,BORDER)
    # Vykrelsení červené lodi
    WIN.blit(RED_SPACESHIP_IMAGE,(red.x,red.y))
    # Vykreslení žluté lodi
    WIN.blit(YELLOW_SPACESHIP_IMAGE,(yellow.x,yellow.y))
    # vykreslení hp červené lodi
    hp_red_text = FONT.render(f"Red HP:{hp[0]}",1,"white")
    WIN.blit(hp_red_text,(10,10))
    # vykreslení hp žlute lodi
    hp_yellow_text = FONT.render(f"Yellow HP:{hp[1]}",1,"white")
    WIN.blit(hp_yellow_text,(800,10))
    
    # if red_critic is not None and pygame.time.get_ticks() - start_time_red < 3000:
    #     critic_text_red = FONT.render(f"{red_critic}",1,"white")
    #     WIN.blit(critic_text_red,(400,60))
    # if yellow_critic is not None and pygame.time.get_ticks() - start_time_yellow < 3000:
    #     critic_text_yellow = FONT.render(f"{yellow_critic}",1,"white")
    #     WIN.blit(critic_text_yellow,(400,60))
    
    # if red_critic is not None:
    #     red_crit_hit = FONT.render(f"{red_critic}",1,"white")
    #     WIN.blit(red_crit_hit,(10,60))
    # if yellow_critic is not None:    
    #     yellow_crit_hit = FONT.render(f"{yellow_critic}",1,"white")
    #     WIN.blit(yellow_crit_hit,(700,60))
    
    # vykreslení červené střely
    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)
    
    #vykrelsení žluté střely 
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)
        
    pygame.display.update()
 
 
def draw_text(text):
    
   
    critic_text = FONT.render(f"{text}",1,"white")
    WIN.blit(critic_text,(400,60))
    
            
        
    pygame.display.update()
    pygame.time.delay(1000)
    
def red_handle_movement(keys,red):
        
        if keys[pygame.K_a] and red.x - SHIPS_VELOCIT > 0:
            red.x -= SHIPS_VELOCIT   
        if keys[pygame.K_d] and red.x + SHIPS_VELOCIT + red.width/2 < BORDER.x:
            red.x += SHIPS_VELOCIT    
        if keys[pygame.K_w] and red.y - SHIPS_VELOCIT > 0:
            red.y -= SHIPS_VELOCIT    
        if keys[pygame.K_s] and red.y + SHIPS_VELOCIT + red.width < HEIGHT:
            red.y += SHIPS_VELOCIT  
            
def yellow_handle_movement(keys,yellow,):
        
        if keys[pygame.K_LEFT]and yellow.x - SHIPS_VELOCIT > BORDER.x:
            yellow.x -= SHIPS_VELOCIT
            # angle_yellow +=1
            # space_ship_angle_yellow(angle_yellow)
            # angle_yellow += 1
            # pygame.transform.rotate(YELLOW_SPACESHIP_IMAGE,angle_yellow)   
        if keys[pygame.K_RIGHT]and yellow.x + SHIPS_VELOCIT + yellow.width/2 < WIDTH:
            yellow.x += SHIPS_VELOCIT    
        if keys[pygame.K_UP]and yellow.y - SHIPS_VELOCIT > 0:
            yellow.y -= SHIPS_VELOCIT    
        if keys[pygame.K_DOWN]and yellow.y + SHIPS_VELOCIT + yellow.width < HEIGHT:
            yellow.y += SHIPS_VELOCIT  
            
def handle_bullets(red_bullets,yellow_bullets,yellow,red,hp):
    for bullet in red_bullets:
        bullet.x +=BULLET_VELOCITY
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
            random_number = random.randint(0,10)
            hp[1] -= random_number
            
            if random_number == 10:
                pygame.event.post(pygame.event.Event(YELLOW_CRIT))
                hp[1] -=20
                print(random_number)
                
            if hp[1] <= 0:
                break
            
        elif bullet.x > WIDTH:
            red_bullets.remove(bullet)
            
            
    for bullet in yellow_bullets:
        bullet.x -=BULLET_VELOCITY
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
            
            random_number = random.randint(0,10)
            hp[0] -= random_number
            
            if random_number == 10:
                pygame.event.post(pygame.event.Event(RED_CRIT))
                hp[0] -= 20
                print(random_number)
                
            if hp[0] <= 0:
                break

        elif bullet.x < 0:
            yellow_bullets.remove(bullet)   
             

    
def show_menu():
    run = True
    while run:
        WIN.fill((0, 0, 0))  # Černé pozadí
        title_text = FONT.render("Menu", True, "white")
        start_text = FONT.render("1. Nová hra", True, "white")
        quit_text = FONT.render("2. Konec", True, "white")

        WIN.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))
        WIN.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, 200))
        WIN.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, 300))

        pygame.display.update()
    
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Klávesa "1" pro novou hru
                    main()
                    
                if event.key == pygame.K_2:  # Klávesa "2" pro konec
                    run = False
                    exit()




def main():
    red = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    
    # yellow_spaceship_image = pygame.transform.scale(pygame.image.load(os.path.join('Assets','spaceship_yellow.png')),(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
    # red_spaceship_image = pygame.transform.scale(pygame.image.load(os.path.join('Assets','spaceship_red.png')),(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))   
    
    # angle_yellow = -270
    # angle_red = -90
    
    # yellow_spaceship_image = pygame.transform.rotate(yellow_spaceship_image,angle_red)
    # red_spaceship_image = pygame.transform.rotate(red_spaceship_image,angle_yellow)
    
    red_bullets = []
    yellow_bullets = []
    hp = [100,100]
    
    start_time = None
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x+red.width, red.y + red.height//2 -2,10,5)
                    red_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x, yellow.y + yellow.height//2-2,10,5)
                    yellow_bullets.append(bullet)
                    
            if hp[0] <= 0:
                win_text = FONT.render("Yellow win",1,"white") 
                WIN.blit(win_text, (WIDTH/2 - win_text.get_width()/2, HEIGHT/2 - win_text.get_height()/2))
                pygame.display.update()
                pygame.time.delay(3000)
                show_menu()
                break
            
            if hp[1] <= 0:
                win_text = FONT.render("Red win",1,"white") 
                WIN.blit(win_text, (WIDTH/2 - win_text.get_width()/2, HEIGHT/2 - win_text.get_height()/2))
                pygame.display.update()
                pygame.time.delay(3000)
                show_menu()
                break
            
            if event.type == RED_CRIT:
                    # start_time_red = pygame.time.get_ticks()
                    red_critic = "Red got critic!!"
                    draw_text(red_critic)
                    # print(red_critic)
                    
                    
            if event.type == YELLOW_CRIT:
                    # start_time_yellow = pygame.time.get_ticks()
                    yellow_critic = "Yellow got critic!!"
                    draw_text(yellow_critic)
                    # print(yellow_critic)
                    

            
               
        # print(red_bullets,yellow_bullets)
        keys = pygame.key.get_pressed()
        # space_ship_angle_yellow(angle_yellow)
        yellow_handle_movement(keys,yellow)
        red_handle_movement(keys,red)
        
        handle_bullets(red_bullets,yellow_bullets,red,yellow,hp)
        
        # if handle_bullets(red_bullets,yellow_bullets,red,yellow,hp) == "Yellow got Critical hit!!":
        #     yellow_critical = "Yellow got Critical hit!!"
        #     return yellow_critical
            
        draw_window(red,yellow,red_bullets,yellow_bullets,hp)
            
    pygame.quit()
    
    
if __name__ == "__main__":
    show_menu()
    
    
