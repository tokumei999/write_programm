#pythonでファイルの取り扱うときは恐らくはRPAみたいに、手順通りファイルを開かせて人がやる処理を自動化する場合に使えるのでは？twitter開いて、おはようツイートしてfacebookでも同じことするならその処理をするファイルを一つずつ用意してpythonファイルの操作をするパイソンファイルを作っておいて、実行すればいいからな。
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

#xモードを使うと既に同名ファイルがある場合失敗してエラーを出す。
#作成したcreatedfile.txtを開く
created_file = open("createdfile.txt", "r")
# ファイル内容の読み込み
#print(created_file.read())
#同じファイルでやるのね。。。別のファイルでreadlineメソッドを使用していたらネームエラーでた。
print(created_file.readline())
#二行目を読み込み
print(created_file.readline())
#下のreadline「s」メソッドを使用するとファイル内のすべての行をリストとして読み込むよ。
#print(created_file.readlines())
#close()関数を忘れずに。
new_file.close()
