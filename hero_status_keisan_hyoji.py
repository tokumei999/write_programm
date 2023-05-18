import random
#このセクションのコードはランダムにヒーローのステータス値を計算する
strength = random.randint(1,20)
brains = random.randint(1,20)
stamina = random.randint(1,20)
wisdom = random.randint(1,20)

#ランダム計算終了

print("あなたのステ:")
print("筋力", strength)
print("知力", brains)
print("持久力", stamina)
print("判断力", wisdom)
