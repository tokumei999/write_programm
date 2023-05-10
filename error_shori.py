try:
    pin = int(input("PINを入力してください"))#整数のみ、入力を受け付けるint(input())
    print("あなたの入力:", pin)
except ValueError:
    print("数値だけ入力してください")
#pythonはexceptを実行するとプログラムを終了する。
