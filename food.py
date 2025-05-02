import pygame
import random
from settings import *

def rastgele_yem(yilan):
    kolon = GENISLIK // KARE_BOYUTU
    satir = YUKSEKLIK // KARE_BOYUTU
    while True:
        x = random.randint(0, kolon - 1) * KARE_BOYUTU
        y = random.randint(0, satir - 1) * KARE_BOYUTU
        if (x, y) not in yilan:
            return x, y

def yem_ciz(ekran, yem):
    pygame.draw.rect(ekran, KIRMIZI, (*yem, KARE_BOYUTU, KARE_BOYUTU))
