ValueErrorに対処する例外処理の例
try-except-else-finally文の使用
try:
    pin = int(input("pinを入力してください: "))
except valueerror:
    print("数値だけ入力してください")
else: 
    print("あなたの入力:", pin)
#エラー処理のコツ:コメントアウトして一つ一つの書き直す。
#原因がわかったらコメントアウトした行を削除する。
