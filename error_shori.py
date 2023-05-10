checking = True
while checking:
    #一行目と二行目で変数が実行されている間は以下の処理を行え
    #そしてcheking = Falseでプログラムを終了。
    try:
        pin = int(input("PINを入力してください"))#整数のみ、入力を受け付けるint(input())
        print("あなたの入力:", pin)
        checking = False
    except ValueError:
        print("数値だけ入力してください")
#pythonはexceptを実行するとプログラムを終了する。
