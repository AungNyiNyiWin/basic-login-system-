users = {
    "aung123":"123456"
}
def get_login_username(users):
    username = input("enter username:").strip().lower()   #အသစ်သင်ခန်းစာပါ။
    if username not in users:
        return None
    return username

def login(users):
    username = get_login_username(users)
    saved_password = users.get(username)
    if saved_password is None:
        print("wrong username.")
        return False,None
    attempts = 0
    while attempts < 3:
        password = input("enter password.").strip()
        if saved_password == password:
            return True,username
        
        attempts += 1   #အသစ်နေရာ ပါ else ထည့်စရာမလိုတော့တာပါ။  return က function ကို ရပ်စေတဲ့အတွက် return နောက်က code မလုပ်တော့ဘူး။
        print("wrong password.")
    
    print("account locked.")
    return False,None

def get_username(users):
    while True:
        new_username = input("enter new username:").strip().lower()
        if new_username in users:
            print("username already exists.")
            continue
        if len(new_username) < 6:
            print("please enter at least 6 characters")
            continue
        return new_username

def get_password():
    while True:
        new_password = input("enter new password:").strip()
        if len(new_password) <6:
            print("please enter at least 6 characters")
        else:
            break
    while True:
        confirm_password = input("enter confirm password.").strip()
        if new_password != confirm_password:
            print("passwords do not match.")
        else:
            break
    return new_password

def register(users):
    new_username = get_username(users)
    new_password = get_password()
    users[new_username]=new_password
    return True

def change_password(users,username):
    old_password = input("enter old password.").strip()
    if old_password != users[username]:
        print("old password not found.")
        return False
    else:
        new_password = get_password()
        users[username]=new_password
        return True

def user_menu(users,username):
    while True:
        print("===user menu===")
        print("1. username.")
        print("2. change password")
        print("3. logout.")
        users_choice = input("enter user choice:")
        if users_choice =="1":
            print("welcome,",username)
        elif users_choice == "2":
            changed = change_password(users,username)
            if changed:
                print("password changed.")
            else:
                print("failed ")
        elif users_choice == "3":
            print("logout")
            break
        else:
            print("invalid users choice.")

while True:
    print("\n===login system===")
    print("1. login")
    print("2. register")
    print("3. exit.")
    choice = input("enter choice:")
    if choice == "1":
        success,username = login(users)
        if success:
            print("login success.")
            user_menu(users,username)
        else:
            print("try again later")
    elif choice == "2":
        passed = register(users)
        if passed:
            print("registration success.")
        else:
            print("registration failed.")
    elif choice == "3":
        print("exit")
        break
    else:
        print("invaild choice.")
