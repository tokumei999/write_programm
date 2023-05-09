#モジュールをインポートして初期化して画像やテキストに使用する色を宣言して画面をセットアップする為の基本的なコードです。
import pygame
import random
#pygameモジュールを初期化
pygame.init()
#赤、緑、青の値を表すタプルの生成
#後でscreenを青で描写
color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_red = (255,0,0)
#サーフェスgame_windowを生成
game_window = pygame.display.set_mode((800,600))
#ウィンドウのタイトルを決定する
pygame.display.set_caption("Box Animation")
#ここまで
#runningがTrueの間プログラムは実行され続け、Falseに変更されるとゲームが終了するようにする。
running = True

move_x = 300
move_y = 300

#ゲームの終了処理。whileとifを組み合わせて作る
while running:#「プログラムが実行される限り」。だから実質ココがゲームの操作処理
    for event in pygame.event.get():#ユーザが特定の入力(event)するまで以下のプログラムを実行せよ
        if event.type == pygame.QUIT:#ユーザがquitボタン(×))を押されたら
            running = False#runningをFalseにしろ。つまりプログラムを終了しなさい。
        if event.type == pygame.KEYDOWN:
            #qボタンが押されたらプログラムを終了
            if event.key == pygame.K_q:
                running = False
            #エスケープボタンが押されたらプログラムを終了
            if event.key == pygame.K_ESCAPE:
                running = False
#ゲームの操作処理
        if event.type == pygame.KEYDOWN:
            #左に移動
            if event.key == pygame.K_LEFT:
                move_x -= 10
        if event.type == pygame.KEYDOWN:
            #右に移動 
            if event.key == pygame.K_RIGHT:
                move_x -+ 10
        if event.type == pygame.KEYDOWN:
            #上に移動
            if event.key == pygame.K_UP:
                move_y -= 10
        if event.type == pygame.KEYDOWN:
            #下に移動
            if event.key == pygame.K_DOWN:
                move_y += 10
#ここまで
#ゲームのウィンドウを白く塗りつぶします。
#先に画面の処理をしてから詰めたほうがよくない？
#後で最初のほうにもっていけばいいか。ともかく動かせるものを作るのが大切。
    game_window.fill(color_white)
#黒色の箱を描写
    pygame.draw.rect(game_window, color_black, [move_x, move_y, 50, 50])
#画面を更新
    pygame.display.update()

pygame.quit()

