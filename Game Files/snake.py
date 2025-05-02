import pygame
from settings import *


def yilan_ciz(ekran, yilan):
    for parca in yilan:
        pygame.draw.rect(ekran, PASTEL_YESIL, (*parca, KARE_BOYUTU, KARE_BOYUTU))


def yeni_yon_guncelle(tus, mevcut_yon):
    if tus == pygame.K_UP and mevcut_yon != (0, KARE_BOYUTU):
        return (0, -KARE_BOYUTU)
    elif tus == pygame.K_DOWN and mevcut_yon != (0, -KARE_BOYUTU):
        return (0, KARE_BOYUTU)
    elif tus == pygame.K_LEFT and mevcut_yon != (KARE_BOYUTU, 0):
        return (-KARE_BOYUTU, 0)
    elif tus == pygame.K_RIGHT and mevcut_yon != (-KARE_BOYUTU, 0):
        return (KARE_BOYUTU, 0)
    return mevcut_yon


def yilan_hareket(yilan, yon, genislik, yukseklik):
    bas_x = (yilan[0][0] + yon[0]) % genislik
    bas_y = (yilan[0][1] + yon[1]) % yukseklik
    bas = (bas_x, bas_y)
    yilan.insert(0, bas)
    return bas, yilan
