import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")  # 背景画像Surface
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")  # こうかとん画像Surface
    kk_img = pg.transform.flip(kk_img, True, False)  # こうかとんを左右反転
    kk_rct = kk_img.get_rect()  # こうかとんRectを取得する
    kk_rct.topleft = (300, 200)  # 初期位置設定
    tmr = 0
    bg_speed = 3  # 背景の速度

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_lst = pg.key.get_pressed()
        
        # 初期の移動量
        dx, dy = -bg_speed, 0  # 何も押さない場合は背景と同じ速度で左に流れる
        
        if key_lst[pg.K_RIGHT]:  # 右矢印キーを押した場合
            dx = +3  # 右に進む
        if key_lst[pg.K_UP]:  # 上矢印キーを押した場合
            dy = -3
        if key_lst[pg.K_DOWN]:  # 下矢印キーを押した場合
            dy = +3

        # こうかとんの位置を更新,move_ipを1回にする
        kk_rct.move_ip(dx, dy)

        # 背景とこうかとんを描画
        x = -(tmr * bg_speed % 3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_img2, [x+4800, 0])
        screen.blit(kk_img, kk_rct)  # screen Surfaceにこうかとんを描画
        pg.display.update()
        tmr += 1
        clock.tick(200)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
