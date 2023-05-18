name = input("名前を教えてください:")
print(f"こんにちは、{name}さん。")

age = input("年齢を教えてください:")
if int(age) < 18:
    print("まだ若いんですね。")
elif int(age) < 65:
    print("まだまだ働き盛りなんですね。")
else:
    print("お元気そうで何よりです。")

hobby = input("趣味を教えてください:") 
if hobby == "読書":
    print(f"{name}さんは読書が趣味なんですね。私も読書が好きです。")
elif hobby == "旅行":
    print(f"{name}さんの趣味は旅行なんですね。羨ましい限りです。")
else:
    print(f"{hobby}は楽しそうな趣味ですね。")
