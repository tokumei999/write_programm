#ファイルを開く
#同名ファイルが存在しているとそれを上書きしてしまうのです。
new_file = open("createdfile.txt", "w")
#ファイルに書き込み
#.writeなのか
new_file.write("Pythonのプログラムで新しいファイルを作成しました\n")
new_file.write("二行目です\n")
#close()関数でファイルをとじて保存する
new_file.close()
#xモードを使うと既に同名ファイルがある場合失敗してエラーを出す。
#作成したcreatedfile.txtを開く
created_file = open("createdfile.txt", "r")
# ファイル内容の読み込み
print(created_file.read())
