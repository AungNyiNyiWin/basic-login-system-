users = {
    "aung":"12345",
    "admin":"admin123"
}

while True:
    print("\n===login system===")
    print("1. login")
    print("2. register")
    print("3. exit")
    choice = input("enter choice:")
    if choice == "1":
        username = input("enter username:").strip().lower()
        saved_password = users.get(username)
        if saved_password is None:
            print("wrong username.")
            continue
        attempts = 0
        while attempts < 3:
            password = input("enter password:").strip()
            if saved_password == password:
                print("login success.")
                while True:
                    print("\n===user menu===")
                    print("1. username")
                    print("2. change password.")
                    print("3. logout.")
                    user_choice= input("enter choice:")
                    if user_choice == "1":
                        print("welcome,",username)
                    elif user_choice=="2":
                        old_password = input("enter Old PW:").strip()
                        if old_password == users[username]:
                            new_password = input("enter New PW:").strip()
                            users[username]=new_password
                            print("changed password.")
                        else:
                            print("old password do not found")
                    elif user_choice=="3":
                        print("successfully logout")
                        break
                    else:
                        print("invalid user choice.")
                break
            else:
                attempts += 1
                print("wrong password.")
        if attempts == 3:
            print("account locked.")
    elif choice == "2":
        
        
        while True:
            new_username = input("enter new username:").strip().lower()
            if new_username in users:
                print("username already exist.")
            else:
                if len(new_username) <6:
                    print("please enter username at least 6 characters")
                else:
                    break
            
        
                
        while True:
            new_password = input("enter new password").strip()
            if len(new_password) <6:
                print("please add password at least 6 character.")

            else:
                
            
                confirm_password = input("enter confirm password").strip()
                if new_password != confirm_password:
                    print("password do not match.")
                else:
                    users[new_username]= new_password
                    print("registration success")
                    break
    elif choice =="3":
        print("good bye")
        break
    else:
        print("invalid choice.")
