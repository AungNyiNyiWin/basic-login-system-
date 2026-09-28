users ={}


def get_login_username(users):
    username = input("enter username:").strip().lower()
    if username not in users:
        return None
    return username

def login(users):
    username = get_login_username(users)
    if username is None:
        return False,None,None
    saved_password = users[username]["password"]
    role = users[username]["role"]
    attempts = 0
    while attempts <3:
        password = input("enter password:").strip()
        if saved_password == password:
            return True,username,role
        attempts += 1
        print("wrong password")
    print("account locked")
    return False,None,None

def get_new_username (users):
    while True:
        new_username = input("enter new username:").strip().lower()
        if new_username in users:
            print("username already exists")
            continue
        if len(new_username)<6:
            print("please enter at least 6 characters")
            continue
        return new_username

def get_new_password():
    while True:
        new_password = input("enter new password:").strip()
        if len(new_password) >= 6:
            break
        print("enter at least 6 characters")

    while True:
        confirm_password = input("enter confirm password:").strip()
        if new_password == confirm_password:
            break
        print("passwords do not match.")
    return new_password

def get_first_admin(users):
    username = get_new_username(users)
    password = get_new_password()

    users[username] = {
        "password":password,
        "role":"admin"
    }
    print("first admin created")

if not users:
    get_first_admin(users)

def change_password(users,username):
    while True:
        old_password = input("enter old password:").strip()
        if old_password != users[username]["password"]:
            print("old password not found")
            return False
        new_password = get_new_password()

        users[username]["password"]=new_password
        return True

def register(users):
    new_username = get_new_username(users)
    new_password = get_new_password()

    users[new_username]={
        "password":new_password,
        "role":"user"
    }
    return True

def delete_user(users):
    
    username = input("enter username:").strip().lower()
    if username not in users:
        print("username not found.")
        return False
    if users[username]["role"]== "admin":
        print("cannot delete admin account")
        return False

    del users[username]
    print("acoount deleted.")
    return True

def change_users_role_by_admin(users,current_username):
    username = input("enter username:").strip().lower()
    if username not in users:
        print("user not found.")
        return False
    elif username == current_username:
        print("cannot change current user's role")
        return False
    
    while True:
        print("1. normal user")
        print("2. admin")
        role_choice = input("enter role choice:")
        if role_choice == "1":
            role = "user"
            break
        elif role_choice == "2":
            role = "admin"
            break
        else:
            print("invalid role choice")

    users[username]["role"]=role
    return True

def add_users(users):
    username = get_new_username(users)
    password =get_new_password()

    while True:
        print("1. normal user")
        print("2. admin")
        role_choice = input("enter choice:")
        if role_choice == "1":
            role = "user"
            break
        elif role_choice == "2":
            role = "admin"
            break
        else:
            print("invalid role choice.")

    users[username]= {
        "password":password,
        "role":role
    }
    return True


def admin_menu(users,username):
    while True:
        print("1. show all users")
        print("2. add users")
        print("3. delete users")
        print("4.add user role by admin")
        print("5. back")
        admin_choice = input("enter admin choice:")
        if admin_choice == "1":
            for user in users:  # username variable ကို ပြန်သုံးမှာဆိုးလို့ for user in users:လို့သုံးတာ သတိပြုပါ။
                role = users[user]["role"]  #users[username]သုံးရင် လက်ရှိ login ဝင် ထားတဲ့ account username ကိုပဲပြပေးမယ်ဆိုတာကိုသတိပြုပါ။
                print("username:",username)
                print("role ;",role)

        elif admin_choice == "2":
            added = add_users(users)
            if added:
                print("user added.")
        elif admin_choice == "3":
            deleted = delete_user(users)
            if deleted:
                print("user deleted.")
        elif admin_choice == "4":
            ok = change_users_role_by_admin(users,username)
            if ok:
                print("user role changed.")
        elif admin_choice == "5":
            print("back")
            break
        else:
            print("invalid admin choice")

def user_menu(users,username):
    while True:
        print("1. username")
        print("2. change password")
        print("3. back")
        user_choice = input("enter user choice:")
        if user_choice == "1":
            print("welcome,",username)
        elif user_choice == "2":
            changed = change_password(users,username)

        elif user_choice == "3":
            print("back")
            break
        else:
            print("invalid user choice.")

while True:
    print("\n=== login system ====")
    print("1.login")
    print("2. register")
    print("3. logout")
    choice = input("enter choice:")
    if choice == "1":
        success,username,role = login(users)
        if success:
            if role == "admin":
                print("login success")
                admin_menu(users,username)
            else:
                print("login success")
                user_menu(users,username)
    elif choice == "2":
        passed = register(users)
        if passed:
            print("registration successful")
    elif choice == "3":
        print("logout")
        break
    else:
        print("invalid choice")
        