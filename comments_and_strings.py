#学んだことをドキュメント化しておく。
#変数の中に数値を入れるならa = 2 でダブルクオーテーションで囲まなければOK
#文字列計算
first_name = "Kinnikun"
last_name = "Nakayama"

print(first_name + last_name)
#英語の名前は中央にスペースある。どうやるか。
#中央にダブルクオーテーションを作りその中でスペースを押す。そのほかの方法は変数で定義した文字列の中でスペースを押せばいい。first_nameなら右側のダブルクオーテーション左側にスペースを打てばいいし、last_nameなら左側のダブルクオーテーションの右側に打てばいい。
print(first_name + " " + last_name)


#ブロックラインコメント
#これはコードのセクションを説明するのに一行以上費やされる場合用いられる。
#書いた日付、著者の名前をドキュメント化する場合にも使用可能である

#ああ、あとコードをコメント化して使えないようにする-コメントアウト-方法もある。

#複数行の文字列
print("""
        自由に書けますよ。
        はい\tはい\tはい\t
Naze\nNaze\nNaze\n
        """)
#登場人物風あるいは英語のアポストロフィを扱う場合
#\' \"
print("\"おい、どうなっているんだ？\"")
print("I\'m so great")
