checking = True
while checking:
    try:
        pin = int(input("PINを入力してください: "))
    except ValueError:
        print("数値だけ入力してください")
    else: 
        print("あなたの入力:", pin)
        checking = False
