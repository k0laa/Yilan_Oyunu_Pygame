import pygame
from settings import *

pygame.font.init()
FONT = pygame.font.Font(None, 36)


def skor_goster(ekran, skor, ortala=False):
    skor_yazi = FONT.render(f"Skor: {skor}", True, BEYAZ)  # Yazı rengi
    if ortala:
        ekran.blit(skor_yazi, (GENISLIK // 2 - skor_yazi.get_width() // 2, 10))
    else:
        ekran.blit(skor_yazi, (10, 10))


def baslik_goster(ekran, yazi):
    baslik = FONT.render(yazi, True, BEYAZ)  # Yazı rengi
    ekran.blit(baslik, (GENISLIK // 2 - baslik.get_width() // 2, 80))


def buton_goster(ekran, rect, yazi, x, y, renk=MAVI):
    buton_renk = renk
    buton_yazi = FONT.render(yazi, True, BEYAZ)  # Yazı rengi
    buton_rect = pygame.Rect(x - rect[0] / 2, y - rect[1] / 2, rect[0], rect[1])
    pygame.draw.rect(ekran, buton_renk, buton_rect, border_radius=5)  # Yuvarlatılmış kenarlar
    pygame.draw.rect(ekran, GRI, buton_rect, 2, border_radius=5)  # Kenar çizgisi
    ekran.blit(buton_yazi, (x - buton_yazi.get_width() // 2, y - buton_yazi.get_height() // 2))
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if buton_rect.collidepoint(mouse_pos) and mouse_click[0]:
        return True
    return False

def hiz_goster(ekran , hiz):
    hiz_yazi = FONT.render(f"Hız: {hiz}", True, BEYAZ)  # Yazı rengi
    ekran.blit(hiz_yazi, (GENISLIK - hiz_yazi.get_width() - 10, 10))

