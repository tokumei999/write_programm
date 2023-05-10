#モジュールをインポートして初期化して画像やテキストに使用する色を宣言して画面をセットアップする為の基本的なコードです。
import pygame
#pygameモジュールを初期化
pygame.init()
#赤、緑、青の値を表すタプルの生成
color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_red = (255,0,0)
#サーフェスgame_windowを生成
game_window = pygame.display.set_mode((800,600))
#ウィンドウのタイトルを決定する
pygame.display.set_caption("衝突検出")
#ここまで
#runningがTrueの間プログラムは実行され続け、Falseに変更されるとゲームが終了するようにする。
running = True
#スプライトを保持する二つの変数を宣言
rect1 = pygame.sprite.Sprite()
rect1.rect = pygame.Rect(300, 300, 100, 150)
rect2 = pygame.sprite.Sprite()
rect2.rect = pygame.Rect(100, 100, 100, 150)

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
                rect1.rect.x = rect1.rect.x - 10
        if event.type == pygame.KEYDOWN:
            #右に移動 
            if event.key == pygame.K_RIGHT:
                rect1.rect.x = rect1.rect.x + 10
        if event.type == pygame.KEYDOWN:
            #上に移動
            if event.key == pygame.K_UP:
                rect1.rect.y = rect1.rect.y - 10
        if event.type == pygame.KEYDOWN:
            #下に移動
            if event.key == pygame.K_DOWN:
                rect1.rect.y = rect1.rect.y + 10
#ここまで
#二つのスプライトの衝突をcollide_rect()関数でチェック
#もし衝突していたらrect1のxy座標を変更
#if pygame.sprite.collide_rect(rect1, rect2):
#    rect1.rect.x = 400
#    rect1.rect.y = 400
#上がエラーの原因。インテンドしてない。でも怖いのはしたにエラー判定が出た事。
        if pygame.sprite.collide_rect(rect1, rect2):
            rect1.rect.x = 400
            rect1.rect.y = 400
#画面の右端が衝突していないか確認する
        if rect1.rect.x > 750:
            rect1.rect.x = 740 
            pygame.display.set_caption("You're in conflict")
#画面の左端が衝突していないか確認する
        if rect1.rect.x > 1:
            rect1.rect.x = 10
            pygame.display.set_caption("You're in conflict")
#画面の右端が衝突していないか確認する
        if rect1.rect.y > 550:
            rect1.rect.y = 540 
            pygame.display.set_caption("You're in conflict")
#画面の右端が衝突していないか確認する
        if rect1.rect.y < 1:
            rect1.rect.y = 10 #ここ間違っていた。エラー吐かれずに思った動きをしてもらえないのが一番解決するのが難しそうだ。ロジックエラーってやつ。
            pygame.display.set_caption("You're in conflict")
#ゲームのウィンドウを白く塗りつぶします。
    game_window.fill(color_white)
#黒色の箱を描写
    pygame.draw.rect(game_window, color_black, rect1.rect)
    pygame.draw.rect(game_window, color_red, rect2.rect)
#画面を更新
    pygame.display.update()

pygame.quit()

