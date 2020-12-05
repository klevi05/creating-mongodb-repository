import pymongo


def database_insert(aplikacioni, email, passwordi):

    client = pymongo.MongoClient()
    mydb = client["mydatabase"]
    mycol = mydb["customers"]
    y = {"App": aplikacioni, "Email": email, "Password": passwordi}
    mycol.insert_one(y)


def database_output():
    client = pymongo.MongoClient()
    mydb = client['mydatabase']
    mycol = mydb["customers"]
    find = mycol.find()
    print(list(find))


veprime = input("Give what you what you whant to do: (1)insert a password (2)take the password--")
if int(veprime) == 1:
    app = input("Cilin applikacion deshironi te jepni: ")
    emaili = input("Me cilin email do e lidhni: ")
    password = input('Jepni password qe keni ne kte app: ')
    database_insert(app, emaili, password)
elif int(veprime) == 2:
    database_output()
else:
    print('Vler e pavertet')
