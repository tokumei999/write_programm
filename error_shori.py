#ValueErrorに対処する例外処理の例
#try-except-else-finally文の使用
try:
    pin = int(input("PINを入力してください: "))
except ValueError:
    print("数値だけ入力してください")
else: 
    print("あなたの入力:", pin)
finally:
    print("もう終わりましたか？")
