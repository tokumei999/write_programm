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
#キーのリストを生成
keys = ["a","b","c",]
juice = ["bochi","riajuu","howaito"]
#fromkeys()を使用して全てのキーに対して値が0の辞書を作成
new_dict = dict.fromkeys(keys, 0)
juice_name = dict.fromkeys(keys,2)
#新しい辞書の出力
print(new_dict)
print(juice_name)
#リストを作って後から値をつけたくなる時とかに、使うのかもしれない。
#シーケンスから辞書を作りたくなる時ってなんだろう。。。数値の並びから辞書にする。
#パスワードとか扱うとき？覚えやすい名前でシーケンスを登録しておく、パスフレーズみたいなもんに使うのかもしれない。
#jonhiscool = []
#いや、なんか全然違う気してきた。まぁいいか。ともかくキーのリストを作って、それに番号を振りたいときに使う。ああ。ゲームでいえば一軍二軍三軍のやつか。一軍は全部1を割り振って置けばいい。
ichigun = ["kaori","nishimoto","saito"]
nigun = ["kaori","nishimoto","saito"]
sangun = ["kaori","nishimoto","saito"]

ichigun = dict.fromkeys(ichigun, 1)
nigun = dict.fromkeys(nigun, 2)
sangun = dict.fromkeys(sangun, 3)

print(ichigun)
print(nigun)
print(sangun)
#リストの生成
gun = {"香り":"本だ" ,"橘": "橋本"} 
#getメソッドを使用して値を取得
kii = gun.get("橘")
print(kii)#出力:キー一番
#存在しない値をgetメソッドで取得
value = gun.get("ririri")
print(value)#出力none
#popitem()を使用して辞書からキーと値のペアを削除し削除されたペアを返す
#最後に追加されたペア、一番右端のペアから削除される
aitemu = gun.popitem()
print(gun)
#dict.setdefault()　キーが存在するかチェックし存在するならそれをかえす。存在しないなら指定した値をキーに対応付ける
chocho = gun.setdefault(0)
choko = gun.setdefault("ワタシ","SAIKYO")
print(choko)
print(gun)
choko = gun.setdefault("ワタシ","SAIKYO")
print(choko)
#辞書内の値を全部返す
print(gun)
kairu = gun.values()
kaere = gun.update()

