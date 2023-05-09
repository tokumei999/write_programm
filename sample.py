#ii
#辞書を使用して人物情報を格納
person = {
        "name": "John" ,
        "age" : 30 ,
        "gender" : "mail"
}
#辞書から値を取得する
name = person["name"]
print(name)

#辞書に新しいキーと値のペアを追加する
person["height"] = 180
print(person)

#辞書からキーと値のペアを削除する
del person["age"]
print(person)
