import pymongo


def database_insert(aplikacioni, email, passwordi):

    client = pymongo.MongoClient()
    mydb = client["mydatabase"]
    mycol = mydb["customers"]
    dblist = client.list_database_names()
    y = {"App": aplikacioni, "Email": email, "Password": passwordi}
    x = mycol.insert_one(y)
    find = mycol.find({}, {"_id": 0, "App": 1, "Email": 1, "Password": 1})
    print(find)
    if "mydatabase" in dblist:
        print('This database exists')


app = input("Cilin applikacion deshironi te jepni: ")
emaili = input("Me cilin email do e lidhni: ")
password = input('Jepni password qe keni ne kte app: ')

database_insert(app, emaili, password)
