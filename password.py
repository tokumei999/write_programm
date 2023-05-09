password = ""#ユーザに入力させるためにダブルクオーテーションで囲んだだけの変数 書式:password = input()
password_attempt = 0 #イベントが起きるたびにカウントする変数

print("パスワードを入力してください")
#正しいパスワード出ない限りユーザに入力をさせる。またpassword_attemptにパスワードが間違った回数をカウントさせる。
while password != "toorimichi":
    password = input()    
    password = password.lower()
    password_attempt = password_attempt + 1
#正しいパスワードが入力されたらメッセージを出してプログラムが終了する。
#もしpassword_attemptが三回に達したら、つまりユーザが入力に三回間違えたらその事をユーザに表示して伝えて終了する    
    if password == "toorimichi":
        print("正しいパスワード",password,"を確認しました")
    elif password_attempt == 3:
        print("制限回数",password_attempt,"回に達しました")#,で前後を囲む
        break
#間違ったパスワードが入力された場合そのことを伝えるメッセージをユーザに表示する。    
    elif password != "toorimichi": 
        print("パスワードが異なるようです")
