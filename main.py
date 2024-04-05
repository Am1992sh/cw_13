import argparse
import user
import pickelManage

users = {}


def add_user(username):
    users[username] = user.User(username)
    pickelManage.save(users)


def remove_user(username):
    users.pop(username)
    pickelManage.save(users)


def change_username(old_username, new_username):
    users[old_username].edit_user(new_username)
    users[new_username] = users.pop(old_username)
    pickelManage.save(users)


def user_history(username):
    print(users[username].show_history())


def translator(username, source_lang, target_lang, text):
    users[username].translate(text, source_lang, target_lang)
    pickelManage.save(users)


def main():
    global users
    users = pickelManage.load()
    arg = argparse.ArgumentParser()
    arg.add_argument("--user")
    arg.add_argument("--source-lang")
    arg.add_argument("--target-lang")
    arg.add_argument("--text")
    arg.add_argument("--addUser")
    arg.add_argument("--editUser", nargs="+")
    arg.add_argument("--deleteUser")
    arg.add_argument("--userHistory")

    pars = arg.parse_args()

    if pars.user:
        translator(pars.user, pars.source_lang, pars.target_lang, pars.text)
    elif pars.addUser:
        add_user(pars.addUser)
    elif pars.editUser:
        change_username(pars.editUser[0], pars.editUser[1])
    elif pars.deleteUser:
        remove_user(pars.deleteUser)
    elif pars.userHistory:
        user_history(pars.userHistory)


if __name__ == "__main__":
    main()
