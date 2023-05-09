import random
#テンプレートとなるstatusクラスを定義
#クラスの最初の文字は大文字
class Status:
    #クラスのインスタンスを初期化し属性をセット
    #コンストラクターメソッド __init__()
    def __init__(self):
        self.charactor_name = name
        self.strength = strength
        self.brains = brains
        self.stamina = stamina
        self.wisdom = wisdom
        self.constitution = constitution
        self.dexterity = dexterity
        self.speed = speed

#名前、スキル、ステータスの自動生成と表示
name = ""
skill = ""

strength = random.randint(1, 100)
brains = random.randint(1, 100)
stamina = random.randint(1, 100)
wisdom = random.randint(1, 100)
constitution = random.randint(1, 100)
dexterity = random.randint(1,100)
speed = random.randint(1, 100)
#名前のリストを定義
myoji = ["鈴木","小林","加藤"]
namae = ["健三","幸子","一郎"]
#スキルのリストを定義
first_skill = ["法律","交渉","実験"]
second_skill = ["ピアノ","バイオリン","ギター"]
#名前とスキルの表示をユーザに伝えてから名前とスキルを生成、表示
print("名前とスキルとステータスを自動的に決めます")
name = random.choice(myoji) + " " + random.choice(namae)
print("あなたの名前は",name,"です")
skill = random.choice(first_skill) + " " + random.choice(second_skill)
print("あなたのスキルは",skill,"の二つです")

#StatusのサブクラスBonus_statusの生成
class Bonus_status(Status):
    def __init__(self):
        print("ボーナスステータスです！")
        Status.__init__(self)
        self.speed = self.speed + 20
#StatusのサブクラスSaikyo_statusの生成
class Saikyo_status(Status):
    def __init__(self):
        print("最強ステータスです")
        Status.__init__(self)
        self.strength = self.strength + 999
        self.brains = self.brains + 999
        self.stamina = self.stamina + 999
        self.wisdom = self.wisdom + 999
        self.constitution = self.constitution + 999
        self.dexterity = self.dexterity + 999
        self.speed = self.speed + 999

#Statusオブジェクトの生成
#オブジェクトの最初の文字は小文字でいい
#selfイコールオブジェクト名?
status0 = Status() 
print("以下はステータス値です\n")
print("筋力:" ,status0.strength)
print("知力:" ,status0.brains)
print("持久力:" ,status0.stamina)
print("判断力:" ,status0.constitution)
print("耐久性:" ,status0.dexterity)
print("スピード:" ,status0.speed)
print("")

#Bonus_statusのオブジェクトの生成
status1 = Bonus_status()
print("以下はステータス値です\n")
print("筋力:" ,status1.strength)
print("知力:" ,status1.brains)
print("持久力:" ,status1.stamina)
print("判断力:" ,status1.constitution)
print("耐久性:" ,status1.dexterity)
print("スピード:" ,status1.speed)
print("")

#Saikyo_statusのオブジェクトの生成
status2 = Saikyo_status()
print("以下はステータス値です\n")
print("筋力:" ,status2.strength)
print("知力:" ,status2.brains)
print("持久力:" ,status2.stamina)
print("判断力:" ,status2.constitution)
print("耐久性:" ,status2.dexterity)
print("スピード:" ,status2.speed)
print("")
