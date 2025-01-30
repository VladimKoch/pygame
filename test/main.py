import pygame
import math

# Inicializace Pygame
pygame.init()

# Nastavení obrazovky
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Otáčení a pohyb objektu")

# Nastavení barev
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Nastavení FPS
clock = pygame.time.Clock()

# Vlastnosti objektu
x, y = WIDTH // 2, HEIGHT // 2  # Výchozí pozice
angle = 0                       # Výchozí úhel
speed = 5                       # Rychlost pohybu

# Hlavní smyčka
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Získání stavu kláves
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle -= 5  # Otočení doleva
    if keys[pygame.K_RIGHT]:
        angle += 5  # Otočení doprava
    if keys[pygame.K_UP]:
        # Výpočet pohybu na základě úhlu
        x += speed * math.cos(math.radians(angle))
        y -= speed * math.sin(math.radians(angle))

    # Vymazání obrazovky
    screen.fill(WHITE)

    # Vykreslení objektu (např. kruh)
    rotated_surface = pygame.Surface((50, 50), pygame.SRCALPHA)
    pygame.draw.polygon(rotated_surface, BLUE, [(25, 0), (0, 50), (50, 50)])  # Trojúhelník
    rotated_surface = pygame.transform.rotate(rotated_surface, -angle)  # Rotace
    rect = rotated_surface.get_rect(center=(x, y))  # Přepočítání středu
    screen.blit(rotated_surface, rect.topleft)

    # Aktualizace obrazovky
    pygame.display.flip()

    # Nastavení FPS
    clock.tick(60)

pygame.quit()