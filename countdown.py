print("さぁ、10秒前だ\n")

for i in range(5,0,-1):
    if i == 5:
        print("はい五秒前でーす")
        continue
    if i == 4:
        print("あと四秒ですぞ")
        continue
    if i == 3:
        print("三秒！三秒前！")
        continue
    if i == 2:
        print("二秒だってアカン！！")
        continue
    if i == 1:
        print("あっ。")
        continue
    print(i)
