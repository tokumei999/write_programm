import pygame

#赤、緑、青の値を表すタプルの生成
#後でscreenを青で描写
color_blue = (0,0,255)
color_pink = (255,200,200)
color_green = (0, 255, 0)
color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_yellow = (255, 255, 0)
color_red = (255,0,0)

#pythonモジュールを初期化
pygame.init()

#800 * 600pixelのサーフェスscreenを生成
screen = pygame.display.set_mode((600,600),0,32)

#ウィンドウのタイトルを決定する
pygame.display.set_caption("The Folie Blue Sky")
#サーフェス、画面screenに青を描写
screen.fill(color_blue)
#画像の領域を表す矩形sidekickを生成
sidekick = pygame.Rect(200,200,200,200)
#画像を読み込んでサーフェスを生成
my_icon = pygame.image.load("donutpoppa.jpg")
#サイズを縮めた新しいサーフェスを生成
thumnail_size = pygame.transform.scale(my_icon, (200, 200))
#テキストを描写する為のフォントを生成
my_font = pygame.font.SysFont(None, 40)
#テキストの書かれた,サーフェスfirst_textを生成
first_text = my_font.render("This dog was pulled from Google.There is no particular reason.", True, color_red, color_blue)
#サーフェスの領域を表す矩形first_text_rectを取得し位置を設定
first_text_rect = first_text.get_rect()
first_text_rect.left = 100
first_text_rect.top = 75
#サーフェスscreenのfirst_text_rectの位置にサーフェスfirst_textを描写
screen.blit(first_text, first_text_rect)
#サーフェスscreenのsidekickの位置にサーフェスthumbnail_iconを表示
#screen.bilt(thumnail_size,sidekick)
screen.blit(thumnail_size,sidekick)
pygame.draw.circle(screen, color_red, (330, 475), 15, 1)
pygame.draw.circle(screen, color_yellow, (375, 475), 15, 0)
pygame.draw.circle(screen, color_pink, (420, 475), 20, 10)
pygame.draw.rect(screen, color_yellow, (455, 475, 20, 20), 4)
pygame.draw.line(screen, color_red, (300, 500), (500,500), 1)
pygame.draw.line(screen, color_yellow, (300, 515), (500, 515),1)
pygame.draw.line(screen, color_red, (300, 530), (500, 530), 1)

#画面を更新する(実際に描写する)
pygame.display.update()
#gameが実行中かどうかを表す変数を宣言
running = True

#ユーザが終了操作をするまでゲームを実行し続けるループを生成
#終了動作をすると変数runningの値がFalseになりゲーム終了

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                bark_text = my_font.render("Bark", True, color_red, color_blue) 
                bark_text_rect = bark_text.get_rect() 
                bark_text_rect.left = 300 
                bark_text_rect.top = 175 
                screen.blit(bark_text, bark_text_rect)
                pygame.display.update()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_b:
                bark_text = my_font.render("Bark", True, color_red, color_blue) 
                bark_text_rect = bark_text.get_rect() 
                bark_text_rect.left = 300 
                bark_text_rect.top = 175 
                screen.blit(bark_text, bark_text_rect)
                pygame.display.update()

pygame.quit()
