baseball_player_salary = [1000,10000,50000]
print("野球選手の最高年俸はいくらですか？")
print("答え:")
print(max(baseball_player_salary))

print("野球選手の最低年俸はいくらですか？")
print("答え:")
print(min(baseball_player_salary))
#リストを使わなくてもmax,minは用いれる
#また文字列にも用いれるがその場合はアルファベット順に並べ替える事が可能。minはaから近い、maxはzから近い
print("日本人野球選手の最高年俸はいくらですか？")
print("答え:")
print(max(10000,20000,30000))
print("日本人野球選手の最低年俸はいくらですか？")
print("答え:")
print(min(10000,20000,30000))

japanese_baseball_players_payrolls = [500,600,200,400,1000]
print("オーナー、日本人野球選手の今月の給与の合計は以下です")
print("答え:")
print(sum(japanese_baseball_players_payrolls))
