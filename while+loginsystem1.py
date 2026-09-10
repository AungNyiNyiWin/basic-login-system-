users = {
    "annw1995": "621993",
    "aung": "12345",
    "admin": "admin123"
}

while True:
    print("\n====login system======")
    print("1. login")
    print("2. register")
    print("3. exit")

    choice = input("enter choice :")
    if choice == "1":
        username = input("enter username:").strip().lower()
        
        saved_password = users.get(username)

        if saved_password is None:
            print("user not found.")
            continue
        attempts = 0
        while attempts < 3:
            password = input("enter password:").strip()
            if saved_password == password:
                print("login success.")
                break
            else:
                attempts += 1
                print("wrong password.")
        if attempts == 3:
            print("account locked.")

    elif choice == "2":
        username = input("enter username:").strip().lower()
        if username in users:
            print("user already exists.")
        else:
            password = input("enter new password:")
            users[username]=password
            print("registration succes.")

    elif choice == "3":
        print("goodbye")
        break


    

    