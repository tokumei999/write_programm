import random
#テンプレートとなるstatusクラスを定義
#クラスの最初の文字は大文字
class Status:
    #クラスのインスタンスを初期化し属性をセット
    #コンストラクターメソッド __init__()
    def __init__(self):
        self.character_name = name
        self.power = power
        self.strength = strength
        self.brains = brains
        self.stamina = stamina
        self.wisdom = wisdom
        self.constitution = constitution
        self.dexterity = dexterity
        self.speed = speed

name = ""
power = ""

power = random.randint(1, 100)
strength = random.randint(1, 100)
brains = random.randint(1, 100)
stamina = random.randint(1, 100)
wisdom = random.randint(1, 100)
constitution = random.randint(1, 100)
dexterity = random.randint(1,100)
speed = random.randint(1, 100)

#Statusオブジェクトの生成()
#オブジェクトの最初の文字は小文字でいい
#selfイコールオブジェクト名?
all_status = Status() 
print("主人公の名前を入力して下さい\n>")
#ユーザの入力をnameに代入する
all_status.name = input(">")
#生成したオブジェクトとその属性を表示する

print("名前:" ,all_status.name)
print("以下はステータス値です\n")
print("筋力" ,all_status.strength)
print("知力" ,all_status.brains)
print("持久力" ,all_status.stamina)
print("判断力" ,all_status.constitution)
print("耐久性" ,all_status.dexterity)
print("スピード" ,all_status.speed)
print("")
