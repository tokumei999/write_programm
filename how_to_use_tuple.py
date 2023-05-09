#f文字列またはフォーマット済み文字列リテラル
#%演算子も、f文字列もどちらも文字列内に変数を埋め込むために使用される。構文と使い方が異なるだけです。古いほうが%演算子です。
name = "gou"
age = 15
print(f"私の名前は{name}です。年齢は{age}です")
kaimono_name = "apple"
kaukazu = 10
print("%sを買ってきてください" % kaimono_name)
print("%s個買ってきてください" % kaukazu)
#タプルです。タプルでセットした値は変更できません。sorted()を使ったり工夫して見た目上は変更できます。
shopping_name = ("パソコン","電子工作用具","フィギュア",)
print(shopping_name)
print(shopping_name[2])
#タプルの要素とテキストを繋げる方法
print("絶対に" , shopping_name[0],"買う")
#+で繋げるほうが表示がきれい。右のテキストがスペース押した感じになるが。。。
print("かわいい" + shopping_name[2],"欲しい")
#スライスする方法。タプルの一部を切り取る。コロンの前は数値がどこから始まるのかを示す。あとはその手前で終わることを示す。だから、0:3は0個目から始まり二個目で終わることを示す。
print(shopping_name[0:3])
#タプルをひとまとめにする
clouthes = ("Pコート","スモッズ","パーカー","ランニングウェア",)
color = ("ブラック","イエロー","ホワイト","レッド",)
#タプルの合成。上のタプルは残っているしその要素の順番も変わっていない事に注意
clouthes_and_color = clouthes + color
print(clouthes_and_color)
#タプルは連結演算子だけではなく、乗算演算子も利用できる。+だけではなく*も使えるよって事。
print(clouthes * 2)
#特定の要素だけを繰り返させるやり方も可能
print(clouthes[1] * 2)
#タプルにもその要素を操作する関数がある。min(),max()も使える
shopping_price = (100,200,120,150,340)
print(min(shopping_price))
print(max(shopping_price))
#len()をタプルに使うとタプルに含まれる要素の数を返す
print(len(clouthes))
print(min(shopping_price))
#sorted()関数を使う。これは実際にはソートされた出力を返すだけで因数として与えられたタプルを実際にソートするわけではない。タプルはイミュータブル(不変)です。また、ソートはアルファベット順になる。日本語だと文字コード順になる。数値にももちろん使える
barabara_number = (111,32,42,12,1,3000)
print(sorted(barabara_number))#sorted入れ忘れた
print(sum(barabara_number))
#変数やリストなどほかのデータ構造もタプル化するtuple()関数を使う
priceless_list = ["努力","友情","勝利"]
tuple(priceless_list)
print(priceless_list)
long_hair = "ロングヘアー"
tuple(long_hair)
print(long_hair)
#タプルは大切なグループを保存したりするのに有効だけど削除したいときもある。
#1.コメントアウト　確実ではない
#2.タプルを参照しているコードを削除、修正してからタプルを削除する。タプル全体を削除する方法はあるけどタプルの項目は削除することはできません。
#del文を利用する。
jakuten = ("鱗","心臓","かかと")
print(jakuten)
del jakuten
#この下のprintを使用するとエラーが出るよ。削除されたjakutenを参照しているからな。
#print(jakuten)
phrase = ("す","も","も","も","も","も","も","も","も","も","も",)
#phrase = tuple("す","も","も","も","も","も","も","も","も","も","も",)でも文字列をタプルに変えることも可能です。
#もが何回タプルに登場するかあを数えてその結果を表示
print("何回\"も\"がでた？")
print(phrase.count("も"))
print("\"す\"は？")
print(phrase.count("す"))
#演算子inを使うとタプル内の要素を検索することができます。inはタプルに要素が含まれているかどうかをチェックしてブール値を返す
print("ん" in phrase)
print("す" in phrase)

