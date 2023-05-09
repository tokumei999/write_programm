#リストは変数と同じ型を扱える。また変数と違って一つのリストで複数のデータを含むことができる。
list_no_list = ["お料理","お買い物"]#文字列を扱っているのでダブルクオーテーションで囲んでいる
icecream = ["バニラ","チョコ","ソーダ"]
alpha = ["B","A","C"]
repeat = ["A","A","A"]
plus1 = ["kawaii","cute","tanosii"]
plus2 = ["kanashii","warai","naki"]
#リストの全体表示
print(list_no_list)
#インデックス番号を指定してリストの要素を表示させる
#また,の後にスペース入れる。なぜなら見やすいからだ(「は」がダブルクオーテーションの左側に置かれていたまぬけはここです)
print(list_no_list[0])
print(list_no_list[0], "はインデックス番号0番にあります")
print(list_no_list[1], "はインデックス番号1番にあります")
#先にテキストを表示する事もできる
print("インデックス番号0番にあるものは", list_no_list[0])
print("インデックス番号1番にあるものは", list_no_list[1])
#*を使うとリスト全体を表示させることが可能
print("これがリストに書かれている全てです・・・。", *list_no_list)
#removeメソッド、delメソッド、appendメソッド、insertメソッドの使い方
#削除
list_no_list.remove("お料理")
print(list_no_list)
#リストの最後に追加
list_no_list.append("しおり")
print(list_no_list)
#どのインデックス番号に追加するか指定して追加
list_no_list.insert(0, "お酒")
print(list_no_list)
#インデックス番号を指定して削除
del list_no_list[0]
print(list_no_list)
#メソッドを試す
#全体確認
print(*icecream)
#リストの最後または指定した値を取得し削除
#インデックス番号指定。文字列は無理。
print(icecream.pop(2))
print(*icecream)
print(*icecream)
#順番を逆にする
icecream.reverse()
print(*icecream)
#もう一つの方法はlist.sortでこれは文字列が対象で、アルファベット順に並べ替える。
print(*alpha)
alpha.sort()
print(*alpha)
#list.count()は与えられた値がリストに現れる回数を数える。
#print(())の書き方で使う。
print(repeat.count("A"))
#リスト同士の足し算
plus1.extend(plus2)
print(*plus1)
#これでplus1はplus2の要素が追加された。
#リストのコピー　左がコピー先で既に登録されたリストで同じ名前があると上書きされるので注意。右がコピー元
icecream2 = icecream
print(*icecream2)
#特定の要素がインデックス番号で何番目にあるか探したい場合
print(icecream2.index("チョコ"))
#リストの要素全部削除。
list_no_list.clear()
print(list_no_list)
