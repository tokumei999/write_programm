#すべて大文字の文字列

test_oomoji = "TESICAN"

print("大文字ですか")
#変数の文字列チェック
print(test_oomoji.isupper())
print(test_oomoji.islower())
print(test_oomoji.isalpha())
print(test_oomoji.isnumeric())
print(test_oomoji.isspace())
#len パスワードとかに使う。越えたらだめとかね。
print(len(test_oomoji))

