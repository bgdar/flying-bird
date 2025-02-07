import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Dimensi layar utama
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Popup Sederhana")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Font
font = pygame.font.Font(None, 36)

# Fungsi untuk membuat popup
def show_popup(screen, message):
    # Ukuran popup
    popup_width = 400
    popup_height = 200

    # Posisi popup
    popup_x = (SCREEN_WIDTH - popup_width) // 2
    popup_y = (SCREEN_HEIGHT - popup_height) // 2

    # Gambar background popup
    popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)
    pygame.draw.rect(screen, GRAY, popup_rect)
    pygame.draw.rect(screen, BLACK, popup_rect, 2)

    # Tampilkan pesan
    text_surface = font.render(message, True, BLACK)
    text_rect = text_surface.get_rect(center=popup_rect.center)
    screen.blit(text_surface, text_rect)

    # Tombol "Close"
    close_button_rect = pygame.Rect(popup_x + popup_width - 100, popup_y + popup_height - 50, 80, 30)
    pygame.draw.rect(screen, RED, close_button_rect)
    close_text = font.render("Close", True, WHITE)
    close_text_rect = close_text.get_rect(center=close_button_rect.center)
    screen.blit(close_text, close_text_rect)

    return close_button_rect

# Loop utama
running = True
showing_popup = False
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if showing_popup:
                # Cek jika tombol "Close" ditekan
                if close_button.collidepoint(event.pos):
                    showing_popup = False
            else:
                # Klik kiri untuk menampilkan popup
                showing_popup = True

    if showing_popup:
        close_button = show_popup(screen, "Ini adalah popup!")

    pygame.display.flip()

pygame.quit()
sys.exit()
