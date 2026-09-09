






users = {
    "annw1995": "621993",
    "aung": "12345",
    "admin": "admin123"
}


while True:
    print("\n====login system====")
    print("1. login ")
    print("2. register")
    print("3. exit")

    choice = input("enter choice:")

    if choice == "1":
        username = input("enter username:").strip().lower()
        password = input("enter password:").strip()

        saved_password = users.get(username)
        if saved_password is None:
            print("user not found.")
        elif saved_password == password:
            print("login success.")
        else:
            print("wrong password.")

    elif choice == "2":
        username = input("enter username:").strip().lower()
        if username in users:
            print("user already exists.") 

        else:
            password = input("enter password:").strip()
            users[username]=password
            print("registeration success.")

    elif choice == "3":
        print("goodbye!")
        break
    
