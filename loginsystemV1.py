users ={
    "annw1995":"621993",
    "aung":"12345",
    "admin":"admin123"
}

while True:
    print("\n===login system====")
    print("1. login")
    print("2. register")
    print("3. exit")

    choice = input("enter choice:")
    if choice == "1":
        username =input("enter username:").strip().lower()
        saved_password = users.get(username)
        if saved_password is None:
            print("user not found.")
            continue
        attempts = 0
        while attempts <3:
            password = input("enter password").strip()
            if saved_password == password:
                print("login success.")
                
                while True:
                    print("\n===user menu====")
                    print("1. username")
                    print("2. logout")

                    user_choice = input("enter choice:")
                    if user_choice == "1":
                        print("welcome ,",username)
                    elif user_choice == "2":
                        print("logout successful.")
                        break
        
                    else:
                        print("invalid input")
                break                               #important break when you logout , this break make to reach the top of login menu
        
            else:
                attempts +=1
                print("wrong password")
        if attempts ==3:
            print("account locked.")
        
    elif choice == "2":
        new_username = input("enter new username:").strip().lower()
        if new_username in users:
            print("user already exists.")
        else:
            new_password = input("enter new password:").strip()
            users[new_username]=new_password
            print("registration success.")

    elif choice == "3":
        print("good bye")
        break

    else:
        print("invalid choice")