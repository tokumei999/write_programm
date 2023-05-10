#ValueErrorに対処する例外処理の例
#try-except-else-finally文の使用
#try:
#    pin = int(input("pinを入力してください: "))
#except valueerror:
#    print("数値だけ入力してください")
#else: 
#    print("あなたの入力:", pin)
#finally:
#    print("もう終わりましたか？")
character_name = "Tsubasa"
character_name2 = "Carl"
if character_name == "Tsubasa":
    raise Exception("ははは")
