
import hashlib
import json




def load_users():
    try:
        with open("users.json","r")as file:
            users = json.load(file)
        return users
    except FileNotFoundError:
        return {}

users = load_users()

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

save_users(users)
    
def hash_password(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

def get_login_username(users):
    username = input("enter username").strip().lower()
    if username not in users:
        return None
    return username

def login(users):
    username = get_login_username(users)
    if username is None:
        print("wrong username")
        return False,None,None,None
    status = users[username]["status"]
    if status is False:
        print("account disabled")
        return False,None,None,None
    saved_password = users[username]["password"]
    role = users[username]["role"]
    attempts = 0
    while attempts<3:
        password = input("enter password").strip()
        hashed_password = hash_password(password)
        if saved_password == hashed_password:
            return True,username,role,status
        attempts += 1
        print("wrong password")
    print("account locked")
    return False,None,None,None



def get_new_username(users):
    while True:
        username = input("enter username:").strip().lower()
        if username in users:
            print("username already exist.")
            continue
        if len(username) < 6:
            print("please enter at least 6 characters")
            continue
        return username

def get_new_password():
    while True:
        new_password = input("enter password:").strip()
        if len(new_password) >= 6:
            break
        print("enter at least 6 characters")

    while True:
        confirm_password = input("enter confirm password:").strip()
        if new_password == confirm_password:
            break
        print("passwords do not match")
    return new_password

def first_admin(users):
    username = get_new_username(users)
    password = get_new_password()
    hashed_password = hash_password(password)
    users[username] = {
        "password":hashed_password,
        "role":"admin",
        "status":True
    }
    print("first admin created.")
    return True

if not users:
    first_admin(users)
    save_users(users)

def register(users):
    username = get_new_username(users)
    password = get_new_password()
    hashed_password = hash_password(password)
    users[username]= {
        "password":hashed_password,
        "role":"user",
        "status":True
    }

    return True

def change_password(users,username):
    
    old_password = input("enter old password:").strip() #old password ကို ပါ hashed password လုပ်ပါမယ်။
    hashed_old_password = hash_password(old_password)
    
    if hashed_old_password  != users[username]["password"]:   #အသစ်နေရာ 
        print("old password not found.")
        return False
    
    new_password = get_new_password()
    hashed_password= hash_password(new_password)
    users[username]= hashed_password
    return True

def add_user_by_admin(users):
    username = get_new_username(users)
    password = get_new_password()

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
            print("invalid choice.")
    hashed_password = hash_password(password)
    users[username]= {
        "password":hashed_password,
        "role":role,
        "status":True
    }
    return True

def delete_user_by_admin(users,current_user):
    username = input("enter username").strip().lower()
    if username not in users:
        print("user not found.")
        return False
    if username == current_user:
        print("cannot delete current user")
        return False
    if users[username]["role"]== "admin":
        print("cannot delete admin role")
        return False

    del users[username]
    print("user deleted.")

    return True

def change_user_role_by_admin(users,username):
    username =input("enter username:").strip().lower()
    if username not in users:
        print("user not found.")
        return False
    if users[username]["role"]== "admin":
        print("cannot delete admin role")
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
            print("invalid choice.")

    users[username]["role"]= role      
    print("role changed.")
    return True

def change_status_by_admin(users,current_username):
    username = input("enter username").strip().lower()
    if username not in users:
        print("username not found")
        return False
    if users[username]["role"]== "admin":
        print("cannot disable admin role")
        return False
    if username == current_username:
        print("cannot disable current username")
        return False

    while True:
        print("1. enable account")
        print("2. disable account")
        admin_choice = input("enter choice:")
        if admin_choice == "1":
            status = True
            break
        elif admin_choice == "2":
            status = False
            break
        else:
            print("invalid choice.")

    users[username]["status"]= status
    print("status changed.")
    return True

def admin_menu(users,username):
    while True:
        print("1. show all users")
        print("2. add user")
        print("3. delete user")
        print("4. enable/disable account")
        print("5. change user role")
        print("6. back")
        admin_choice = input("enter admin choice:")
        if admin_choice == "1":
            for user in users:
                print("username:",user)
                role = users[user]["role"]
                print("role:", role)
                status = users[user]["status"]
                print("status:",status)

        elif admin_choice == "2":
            added = add_user_by_admin(users)
            if added:
                save_users(users)
                print("new account added.")

        elif admin_choice == "3":
            deleted = delete_user_by_admin(users,username)
            if deleted:
                save_users(users)
                print("account deleted")

        elif admin_choice == "4":
            changed = change_status_by_admin(users,username)
            if changed:
                save_users(users)
                print("account enabled or disabled")

        elif admin_choice == "5":
            annw = change_user_role_by_admin(users,username)
            if annw:
                save_users(users)
                print("user role changed.")
        elif admin_choice == "6":

            print("back")
            break

def user_menu(users,username):
    while True:
        print("1. username")
        print("2. change password")
        print("3. back")

        user_choice = input("enter user chice:")
        if user_choice == "1":
            print("Welcome :",username)
        elif user_choice == "2":
            changed = change_password(users,username)
            if changed:
                save_users(users)
                print("password changed.")
        elif user_choice == "3":
            print("back")
            break
        else:
            print("invalid user choice.")

while True:
    print("1. login")
    print("2. register")
    print("3. logout")
    choice = input("enter choice:")
    if choice == "1":
        success,username,role,status = login(users)
        if success:
            if role== "admin" and status == True:
                print("login success.")
                admin_menu(users,username)
                
            elif role == "user" and status == True:
                print("login success")
                user_menu(users,username)
                
    elif choice == "2":
        registered = register(users)
        if registered:
            save_users(users)
            print("registration success.")
    elif choice == "3":
        print("logout")
        break
    else:
        print("invalid choice.")



