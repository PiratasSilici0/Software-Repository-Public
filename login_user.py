def login_user():
    password_false = False
    while not password_false:
        print("\033[0;34;1m|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|\033[m")
        login = str(input("  \033[0;33;1mLogin:\033[m"))
        password = str(input("  \033[0;33;1mPassword:\033[m"))
        print("\033[0;34;1m|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|\033[m")
        arquivo_login = open("Arquivo_Login.txt","r")
        for line in arquivo_login:
            login_true = line.split("::")[0]
            password_true = line.split("::")[1]
            if login==login_true:
                if password==password_true:
                    password_false = True
            else:
                print("\033[0;34;1m|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|\033[m")
                print("\033[0;31;1m | Invalid operation              |\033[m")
                print("\033[0;31;1m | Incorrect username or password |\033[m")
                print("\033[0;34;1m|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|\033[m")
if __name__=="__main__":
    login_user()