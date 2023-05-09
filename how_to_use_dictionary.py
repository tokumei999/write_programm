#辞書は対応関係を使う。キーを値に対応つける事だ。keyが左でvaluesが右
character = {"jonh":"貯金","marin":"暗算"}
#全部表示
print(character)
#特定の要素を表示するにはprint(辞書["要素"])
print(character["marin"])
#キー(左側)だけを全部表示
print(character.keys())
#値(右側)だけ全部表示
print(character.values())
#キーと値の両方を表示したい場合
print(character.items())
#辞書のメソッドはデータを比較したり辞書内にどのようなデータがあるかを確認したりする必要がある場合に便利です。
#辞書内の要素を表示する別の方法
#for文を使って辞書の要素を表示
for key, value in character.items():
    print("キーは",key,"で,値は",value)
#辞書はタプルと異なり、値(キーではない)を変更可能
#characterにキーkaoriとして値30を追加
character["kaori"] = 30
print(character)
#キーの値の更新する必要があるときは次のように更新するか、updateメソッドを使う
character["kaori"] = 31
print(character)
#updateメソッド
character.update({"satoshi":"研究"})
print(character)
#del文を使ってキーと値のペアを削除する
#例えば物語の過程でsatoshiが死亡した場合の処理
#del character["satoshi"]
#print(character)
#del文を使って辞書ごと削除する方法
#セーラームーンの最終回みたいにみんな死ぬときにする処理方法

#del character
#print(character)

#printを利用して表示しようとすると既に削除されているからエラーを吐き出す。
#辞書内の全てのキーと値のペアを削除したいが、辞書ごと削除したくない場合
#みんな死んだけど、物語はまだ続いている場合はこれ
#辞書charaの生成
chara = {"satoshi": "superpower", "kaori": "料理", "hoshi": "野球"}
print(chara)
chara.clear()
print(chara)
