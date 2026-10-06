users = {}
import hashlib

def hash_password(password):    #(password) >>> parameter  for hashing 
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed


def get_login_username(users):
    username = input("enter username:").strip().lower()
    if username not in users:
        return None
    return username

def login(users):
    username = get_login_username(users)
    if username is None:
        print("wrong username.")
        return False,None,None,None
    status = users[username]["status"]
    if status is False:
        print("account disabled.")
        return False,None,None,None
    saved_password = users[username]["password"]
    role = users[username]["role"]
    attempts = 0
    while attempts <3:
        password = input("enter password:").strip()
        hashed_password = hash_password(password)
        if saved_password == hashed_password:
            return True,username,role,status
        attempts += 1
        print("wrong password")
    print("acccount locked.")
    return False,None,None,None

def get_new_username(users):
    while True:
        new_username = input("enter new username:").strip().lower()
        if new_username in users:
            print("username already exist.")
            continue
        if len(new_username)<6:
            print("please enter at least 6 characters")
            continue
        return new_username

def get_new_password():
    while True:
        new_password = input("enter new password:").strip()
        if len(new_password)>= 6:
            break
        print("please enter at least 6 characters")

    while True:
        confirm_password = input("enter confirm password:").strip()
        if new_password == confirm_password:
            break
        print("passwords do not match.")
    return new_password

def register(users):
    username = get_new_username(users)
    password = get_new_password()   #arguement for hash_password(____)
    hashed_password = hash_password(password)   
    
    users[username]={
        "password":hashed_password,
        "role":"user",
        "status":True
    }
    return True

def change_password(users,username):
    old_password = input("enter old password:").strip()
    if old_password != users[username]["password"]:
        print("old password not found.")
        return False
    
    new_password = get_new_password()
    hashed_password = hash_password(new_password)
    users[username]["password"]=hashed_password
    return True

def first_admin(users):
    username = get_new_username(users)
    password = get_new_password()
    hashed_password = hash_password(password)
    users[username]= {
        "password":hashed_password,
        "role":"admin",
        "status":True
    }
    print("first admin created.")
    return True

if not users:
    first_admin(users)

def add_users(users):
    username = get_new_username(users)
    password =get_new_password()

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
    hashed_password = hash_password(password)
    users[username]={
        "password":hashed_password,
        "role":role,
        "status":True
        }
    return True

def delete_user(users,current_username):
    username = input("enter username :").strip().lower()
    if username not in users:
        print("user not found")
        return False
    elif users[username]["role"]== "admin":
        print("cannot delete admin role")
        return False
    elif username == current_username:
        print("connont delete current account.")
        return False

    del users[username]
    return True

def change_role(users,current_username):
    username = input("enter username:").strip().lower()
    if username not in users:
        print("user not found.")
        return False
    elif username == current_username:
        print("cannot change current user role")
        return False

    while True:
        print("1. normal user")
        print("2. admin")
        role_choice = input("enter role choice:")
        if role_choice == '1':
            role = "user"
            break
        elif role_choice == "2":
            role == "admin"
            break
        else:
            print("invalid role choice")

    users[username]["role"]=role
    return True

def change_users_status(users,current_username):
    username = input("enter username:").strip().lower()
    if username not  in users:
        print("user not found.")
        return False

    if username == current_username:
        print("cannot change your own status")
        return False

    while True:
        print("1. Disable")
        print("2. Enable")
        status_choice = input("enter status choice:")
        if status_choice == "1":
            status = False
            break
        elif status_choice == "2":
            status = True
            break
        else:
            print("invalid status choice.")

    users[username]["status"]= status
    return True

def admin_menu(users,username):
    while True:
        print("\n====admin menu===")
        print("1. show all users")
        print("2. add users")
        print("3. delete users")
        print("4. change roles")
        print("5. change user status")
        print("6. back")
        admin_choice = input("enter admin choice:")
        if admin_choice == "1":
            for user in users:
                role = users[user]["role"]
                print("username:",user)
                print("role:",role)
        elif admin_choice == "2":
            added = add_users(users)
            if added:
                print("new user added.")
        elif admin_choice == "3":
            deleted = delete_user(users,username)            
            if deleted:
                print("user deleted.")
        elif admin_choice == "4":
            changed = change_role(users,username)
            if changed:
                print("user role changed.")
        elif admin_choice == "5":
            ok = change_users_status(users,username)
            if ok:
                print("user status changed.")
        elif admin_choice == "6":
            print("back")
            break
        else:
            print("invalid admin choice.")

def user_menu(users,username):
    while True:
        print("1. username")
        print("2. change password")
        print("3. logout")
        user_choice = input("enter user chocie:")
        if user_choice == "1":
            print("welcome,",username)
        elif user_choice == "2":
            changed = change_password(users,username)
            if changed:
                print("password changed.")
        elif user_choice == "3":
            print("logout")
            break
        else:
            print("invalid user choice.")

while True:
    print("\n====login system===")
    print("1. login")
    print("2. register")
    print("3. logout")
    choice = input("enter choice:")
    if choice == "1":
        success,username,role,status =login(users)
        if success:
            if role == "admin":
                print("login success.")
                admin_menu(users,username)
            else:
                user_menu(users,username)
    elif choice == "2":
        registered= register(users)
        if registered:
            print("registration success.")
    elif choice == "3":
        print("logout")
        break
    else:
        print("invalid choice.")




