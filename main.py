import pygame
import random
import sys

# Pygame başlat
pygame.init()

# Renkler
SIYAH = (0, 0, 0)
YESIL = (0, 255, 0)
KIRMIZI = (255, 0, 0)

# Ayarlar
KARE_BOYUTU = 10
GENISLIK = 400
YUKSEKLIK = 400
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Yılan Oyunu")
saat = pygame.time.Clock()
FPS = 10

# Başlangıç
yilan = [(90, 90), (80, 90), (70, 90)]
yon = (KARE_BOYUTU, 0)
yeni_yon = yon

# Yem
def rastgele_yem():
    kolon = GENISLIK // KARE_BOYUTU
    satir = YUKSEKLIK // KARE_BOYUTU
    while True:
        x = random.randint(0, kolon - 1) * KARE_BOYUTU
        y = random.randint(0, satir - 1) * KARE_BOYUTU
        if (x, y) not in yilan:
            return x, y

yem = rastgele_yem()

def yilan_ciz():
    for parca in yilan:
        pygame.draw.rect(ekran, YESIL, (*parca, KARE_BOYUTU, KARE_BOYUTU))

# Oyun döngüsü
while True:
    # Yön güncellemesini sadece bir kez yap
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and yon != (0, KARE_BOYUTU):
                yeni_yon = (0, -KARE_BOYUTU)
            elif event.key == pygame.K_DOWN and yon != (0, -KARE_BOYUTU):
                yeni_yon = (0, KARE_BOYUTU)
            elif event.key == pygame.K_LEFT and yon != (KARE_BOYUTU, 0):
                yeni_yon = (-KARE_BOYUTU, 0)
            elif event.key == pygame.K_RIGHT and yon != (-KARE_BOYUTU, 0):
                yeni_yon = (KARE_BOYUTU, 0)

    yon = yeni_yon

    bas_x = (yilan[0][0] + yon[0]) % GENISLIK
    bas_y = (yilan[0][1] + yon[1]) % YUKSEKLIK
    bas = (bas_x, bas_y)
    yilan.insert(0, bas)

    if bas == yem:
        yem = rastgele_yem()
    else:
        yilan.pop()

    if bas in yilan[1:]:
        pygame.quit()
        sys.exit()

    ekran.fill(SIYAH)
    yilan_ciz()
    pygame.draw.rect(ekran, KIRMIZI, (*yem, KARE_BOYUTU, KARE_BOYUTU))
    pygame.display.update()
    saat.tick(FPS)
