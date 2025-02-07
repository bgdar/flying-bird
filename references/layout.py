import pygame
import sys

pygame.init()

# Setup Pygame
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Halaman atau Layout")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# State
state = "menu"  # Bisa 'menu', 'game', atau 'credits'

# Fungsi untuk menggambar halaman
def draw_menu():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 36)
    title = font.render("Menu Utama", True, BLACK)
    play_button = font.render("Tekan P untuk Mulai", True, BLUE)
    credits_button = font.render("Tekan C untuk Credits", True, BLUE)
    screen.blit(title, (300, 200))
    screen.blit(play_button, (300, 300))
    screen.blit(credits_button, (300, 350))

def draw_game():
    screen.fill(RED)
    font = pygame.font.Font(None, 36)
    text = font.render("Halaman Permainan", True, WHITE)
    screen.blit(text, (300, 300))

def draw_credits():
    screen.fill(BLUE)
    font = pygame.font.Font(None, 36)
    text = font.render("Halaman Credits", True, WHITE)
    back_button = font.render("Tekan B untuk Kembali", True, WHITE)
    screen.blit(text, (300, 200))
    screen.blit(back_button, (300, 300))

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if state == "menu":
                if event.key == pygame.K_p:  # Tekan P untuk bermain
                    state = "game"
                elif event.key == pygame.K_c:  # Tekan C untuk credits
                    state = "credits"
            elif state == "game":
                if event.key == pygame.K_ESCAPE:  # Tekan ESC untuk kembali ke menu
                    state = "menu"
            elif state == "credits":
                if event.key == pygame.K_b:  # Tekan B untuk kembali
                    state = "menu"

    # Menggambar halaman sesuai state
    if state == "menu":
        draw_menu()
    elif state == "game":
        draw_game()
    elif state == "credits":
        draw_credits()

    # Update layar
    pygame.display.flip()
    clock.tick(60)