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
    app = input("Which application you whant to add to your list:  ")
    emaili = input("With what email you whant it too sync: ")
    password = input('Enter the password: ')
    database_insert(app, emaili, password)
elif int(veprime) == 2:
    admin = input("Give the password admin: ")
    if admin == 'AminiMadh':
        print("The password are: ")
        database_output()
    else:
        print("You entered a wrong password!")
else:
    print('Invalide Value!')
