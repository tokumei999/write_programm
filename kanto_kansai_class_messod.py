class Todo_Huken:
    #クラスの中身=メソッドの定義 def メソッド名
    #クラスの下にモジュールがありますね。
    def kanto(self):
        print("Tokyo,Kanagawa,Ibaraki,Chiba,Tochigi,Saitama,Gunma")
    #クラスは二つ以上のメソッドを定義することも可能
    def kansai(self):
        print("Oosaka,Kyoto,Hyogo,Nara,shiga,wakayama")
#変数を定義、そしてクラスに変数を代入かな。
#変数.モジュール名()
#正式な説明
#オブジェクト(クラスのインスタンス)(恐らく左)を作るには変数を宣言して値をセット(右)するのと同様にインスタンスを初期化(生成)しなければなりません。
chiiki = Todo_Huken()
#オブジェクトの生成
chiiki.kanto()
chiiki.kansai()
