#ランダムな数値や文字列を得るためにrandomモジュールをインポートする
import random
#ディレイを生み出す為にtimeモジュールをインポートする
import time

#キャラのステ値を保持する変数を宣言(初期化)する

strength = 0
brains = 0
stamina = 0
wisdom = 0
constitutuion = 0
dexterity = 0
speed = 0

answer = ""

#能力リスト
skill = ["早食い","貯金","投資","ダッシュ","法律",]
#名前リスト
myoji = ["笹川","高木","西川","堀江","鈴木",]
namae = ["Daisuke","良治","良助","五右衛門","リンカーン",]

#導入テキスト

print("さぁ、キャラをポーンするぞ")

#ユーザに質問し答えさせてそれを表示
#input()関数でユーザの入力を受け付ける
#upper()関数でユーザの回答を大文字化する事で処理を減らす

print("「Y」か「N」で入力してください")

answer = input()
answer = answer.upper()

#回答Yをチェックするwhileループ
#このループは変数answerの値がYでない限り続け
#ユーザがYを入力したときだけループを抜け続きのプログラムが実行される。

while answer != "Y":
    print("間違えています\nもう一度入力してください。")
    print("YかNか入力")
    answer = input()
    answer = answer.upper()

print("確認完了しました\nでは、始めましょう")
#ここまでのまとめ、ステ値を生成、ユーザに質問して特定の文字を入力させるまで、同じ処理を繰り返すプログラムの完成
print("名前をランダム化している")
#time.sleep()関数で三秒停止
for i in range(3):
    print(".....")
    time.sleep(3)

print("マテ")
print("")

#名前のランダム化
#二つの名前のリストからそれぞれひとつ選ぶ
#それらを繋げて変数に代入

japanese_name = random.choice(myoji) + " " + random.choice(namae)
print("キャラの名前はこれだ！！")
print(japanese_name)

print("")
print("このキャラのスキルはこれです\n生成中.....\n")

for i in range(2):
    print(".....")
    time.sleep(3)

print(".....")

#リストskillからランダムに選択
#変数kettei_skillに代入

kettei_skill = random.choice(skill)

#kettei_skillとテキストを表示

print("このキャラのスキルは",kettei_skill,"です")
print("")

#最後にキャラのステ値をランダムに生成してそれをユーザに示す。
print("最後はキャラのステ値だ！\n")

for i in range(3):
    print(".....")
    time.sleep(3)
#以下の変数にランダムに新しい値を代入
#新しい値は1から20の範囲とする
strength = random.randint(1,20) 
brains = random.randint(1,20) 
stamina = random.randint(1,20)
wisdom = random.randint(1,20)
constitutuion = random.randint(1,20)
dexterity = random.randint(1,20)
speed = random.randint(1,20)
#ステをユーザに表示
print("お待たせしました\n")
print("筋力:", strength)
print("知力:", brains)
print("持久力:", stamina)
print("判断力:", constitutuion)
print("敏捷力:", dexterity)
print("スピード:", speed)
print("")

#生成された全てのステをユーザに表示
print("キャラクターまとめ")
print("名前", japanese_name)
print("スキル", kettei_skill)
print("ステータス値は以下\n")
print("筋力:", strength)
print("知力:", brains)
print("持久力:", stamina)
print("判断力:", constitutuion)
print("敏捷力:", dexterity)
print("スピード:", speed)
