from game import YilanOyunu

if __name__ == "__main__":
    yilanOyun = YilanOyunu()

    # Ana döngü
    while True:
        yilanOyun.ana_menu()
        skor = yilanOyun.oyun()
        yilanOyun.oyun_bitti(skor)

