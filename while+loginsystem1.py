users = {
    "annw1995": "621993",
    "aung": "12345",
    "admin": "admin123"
}




while True:
    print("\n====login system====")
    print("1. Login ")
    print("2. Register ")
    print("3. Exit")

    choice = input("enter your choice:")

    if choice == "1":
        username = input("enter username:").strip().lower()
        password = input("enter password:").strip()

        saved_password = users.get(username)
        if saved_password is None:
            print("user not found.")
        elif saved_password == password:
            print("login successful.")
        else:
            print("wrong password.")

    elif choice == "2":
        username = input("enter username:").strip().lower()
        if username in users:
            print("user exists.")
        else:
            password = input("enter password.").strip()
            users[username]=password
            print("registration success")
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("invalid choice")

            
    

