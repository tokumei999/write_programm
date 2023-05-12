#pythonでファイルの取り扱うときは恐らくはRPAみたいに、手順通りファイルを開かせて人がやる処理を自動化する場合に使えるのでは？twitter開いて、おはようツイートして閉じてfacebookでも同じことするならその処理をするパイソンファイルを一つずつ用意してパイソンファイルを操作をするパイソンファイルを作っておいて、一回だけ実行すればいいからな。
#ファイルを開く
#同名ファイルが存在しているとそれを上書きしてしまうのです。
new_file = open("createdfile.txt", "w")
#ファイルに書き込み
#.writeなのか
new_file.write("Pythonのプログラムで新しいファイルを作成しました\n")
new_file.write("二行目です\n")
#close()関数でファイルをとじて保存する
new_file.close()

#ここで一つの作業が終わったと捉える
#ダメだ。わからん。こんがらがっている
#ファイルを作成して書き込み、閉じるそして追加の書き込みを行う場合
#createdfile = open("createdfile.txt", "r")
#print(createdfile.readline())
#print(createdfile.readline())
#問題の追記モード
#adding_to_file = open("createdfile.txt", "a")

#うまく追加できない。なぜ？
#adding_to_file.write = ("テキストの続きです\n")

#adding_to_file.close()

#adding_to_file = open("createdfile.txt", "r")
#print(createdfile.readline())
#adding_to_file.close()

#print("ファイルに追加のテキストがあるかどうか\n")
#print("ファイルに追加のテキストがあるかどうか\n")
#appended_file = open("createdfile.txt", "r")
#appended_file.close() 



















#xモードを使うと既に同名ファイルがある場合失敗してエラーを出す。
#作成したcreatedfile.txtを開く
#created_file = open("createdfile.txt", "r")
# ファイル内容の読み込み
#print(created_file.read())
#同じファイルでやるのね。。。別のファイルでreadlineメソッドを使用していたらネームエラーでた。
#print(created_file.readline())
#二行目を読み込み
#print(created_file.readline())
#下のreadline「s」メソッドを使用するとファイル内のすべての行をリストとして読み込むよ。
#print(created_file.readlines())
#close()関数を忘れずに。
#new_file.close()

#注意すべきファイルの読み書きの仕方。
#以下でやると上書きされてしまう。
#ファイルを作成・開く、書き込む、閉じる。そして開く、書き込む。閉じる。でやると依然書き込んだ内容がふっとぶ。
#new_file = open("CreatedFile.txt", "w")
#new_file.write = ("一行目です\n")
#new_file.write = ("二行目です\n")

#new_file.close()#ここテキストで間違ってましたね。。。

#adding_to_file = open("CreatedFile.txt", "w")

#adding_to_file.write("テキストの続きです\n")

#adding_to_file.close()
#たしかめてみてね。

#ダメだ。わからん。こんがらがっている
#ファイルを作成して書き込み、閉じるそして追加の書き込みを行う場合

#new_file = open("createdfile.txt", "w")
#new_file.write = ("一行目です\n")
#new_file.write = ("二行目です\n")

#new_file.close()#ここテキストで間違ってましたね。。。
#作成したファイルを開く・
#createdfile = open("createdfile.txt", "r")

#print("オリジナルは以下のテキスト")
#print(createdfile.read())
#print(createdfile.readline())
#print(createdfile.readline())
#new_file.close()

#adding_to_file = open("CreatedFile.txt", "a")
#adding_to_file.write = open("テキストの続きです\n")

#adding_to_file.close()

#for line in appended_file:
#    print(line)
#append_file.close()
#new_file.close()
