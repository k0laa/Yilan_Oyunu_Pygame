import pygame
import sys
from settings import *
from snake import *
from food import *

# Pygame başlat
pygame.init()

# Ayarlar
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Yılan Oyunu")
saat = pygame.time.Clock()

# Başlangıç
yilan = [(90, 90), (80, 90), (70, 90)]
yon = (KARE_BOYUTU, 0)
yeni_yon = yon
yem = rastgele_yem(yilan)

# Oyun döngüsü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            yeni_yon = yeni_yon_guncelle(event.key, yon)

    yon = yeni_yon
    bas, yilan = yilan_hareket(yilan, yon, GENISLIK, YUKSEKLIK)

    if bas == yem:
        yem = rastgele_yem(yilan)
    else:
        yilan.pop()

    if bas in yilan[1:]:
        pygame.quit()
        sys.exit()

    ekran.fill(SIYAH)
    yilan_ciz(ekran, yilan)
    yem_ciz(ekran, yem)
    pygame.display.update()
    saat.tick(FPS)
