import getpass
database = {"username": "123456", "admin": "654321"}
username = input("Enter your username: ")
password = getpass.getpass("Enter Your Password: ")

if username in database:
    while password != database[username]:
        password = getpass.getpass("Enter Your Password Again: ")
    print("Verified")
else:
    print("Username not found")