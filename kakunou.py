#やっぱりパスワードとかに使われるんだろうか。。。
#辞書の作成
passphrase = {"isee":"4953","cul":"6493",}
#setdefault()メソッドを利用してキーと値のペアを追加
new_pass = passphrase.setdefault("fass","5843")
print(new_pass)
print(passphrase)
#setdefault()メソッドを使用して既に存在しているキーの値を取得
kakunin = passphrase.setdefault("chaos","7482")
print(kakunin)
print(passphrase)


