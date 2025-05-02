import sys
from snake import *
from food import *
from ui import *

# Pygame başlat
pygame.init()

# Ayarlar
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Yılan Oyunu")
saat = pygame.time.Clock()
FPS = 10


def oyun():
    # Başlangıç
    yilan = [(90, 90), (80, 90), (70, 90)]
    yon = (KARE_BOYUTU, 0)
    yeni_yon = yon
    yem = rastgele_yem(yilan)
    skor = 0
    hizlanma_kontrol = 0

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
            skor += 1
        else:
            yilan.pop()

        if bas in yilan[1:]:
            return skor  # Ölüm ekranına skor döndür

        if hizlanma_kontrol + 5 == skor:
            global FPS
            FPS += 5
            hizlanma_kontrol = skor

        ekran.fill(SIYAH)
        yilan_ciz(ekran, yilan)
        yem_ciz(ekran, yem)
        skor_goster(ekran, skor)
        hiz_goster(ekran, FPS)
        pygame.display.update()
        saat.tick(FPS)


def ana_menu():
    while True:
        ekran.fill(SIYAH)  # Arka plan rengi
        baslik_goster(ekran, "Yılan Oyunu")
        if buton_goster(ekran, (100, 50), "Başla", GENISLIK // 2, YUKSEKLIK // 2, renk=MAVI):
            return
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def oyun_bitti(skor):
    while True:
        ekran.fill(SIYAH)  # Arka plan rengi
        baslik_goster(ekran, "Oyun Bitti")
        skor_goster(ekran, skor, ortala=True)
        if buton_goster(ekran, (160, 40), "Tekrar Oyna", GENISLIK // 2, YUKSEKLIK // 2, renk=MAVI):
            return
        if buton_goster(ekran, (100, 40), "Çıkış", GENISLIK // 2, YUKSEKLIK // 2 + 50, renk=KIRMIZI):
            pygame.quit()
            sys.exit()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


# Ana döngü
while True:
    ana_menu()
    skor = oyun()
    oyun_bitti(skor)
