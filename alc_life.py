import random
my_allowance = random.randint(1,100)
drink =50 
new_drink = 25 
#お酒が買えるかどうかチェックして表示
if my_allowance >= drink:
    print("お酒は買えます")
    print("追加のお酒はどうですか？")
#ここで新しいお酒が買えるかどうかチェックして表示する
    if my_allowance >= new_drink:
        print("追加のお酒持ってきます")
#ここの処理は実質if my allowance >= drink and my_allowance >= new_drinkと同じです。
#else。コード階層に注意
    else:
        print("お金が無いので追加のお酒は買えません")
#両方の条件が満たされなかった場合
else:
    print("どちらのお酒も買えないようですね")
