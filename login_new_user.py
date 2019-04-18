def login_new_user():
    password_false = False
    while not password_false:
        print("\033[0;34;1m|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|\033[m")
        print("  \033[0;34;1m(1)\033[m \033[0;33;1mLogin Settings\033[m")
        print(" (2) Back")
        print("\033[0;34;1m|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|\033[m")
        usuario_user = str(input("  \033[0;33;1mEnter options:\033[m"))
        if usuario_user == "1":
            while usuario_user:
                if usuario_user=="1":
                        print ("\033[0;34;1m|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|\033[m")
                        login = str(input("  \033[0;33;1mLogin:\033[m"))
                        password = str(input("  \033[0;33;1mPassword:\033[m"))
                        arquivo_login = open("Arquivo_Login.txt","r")
                        for line in arquivo_login:
                            true_login = arquivo_login==login
                            true_password = arquivo_login=password
                            true_login = line.split("::")[0]
                            true_password = line.split("::")[1]
                            if login==true_login:
                                if password==true_password:
                                    print("\033[0;34;1m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m")
                                    login_new = str(input("\033[0;33;1m | New Login:\033[m"))
                                    password_new =str(input("\033[0;33;1m | New Password:\033[m"))
                                    print("\033[0;34;1m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m")
                                    arquivo_login  = open("Arquivo_Login.txt","a")
                                    arquivo_login.write("{}:{}".format(login_new,password_new))
                                    user_false = True
                            else:
                               print("\033[0;34;1m|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|\033[m")
                               print("\033[0;31;1m | Invalid operation              |\033[m")
                               print("\033[0;31;1m | Incorrect username or password |\033[m")
                               print("\033[0;34;1m|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|\033[m")
        if usuario_user=="2":
            break
if __name__=="__main__":
    login_new_user()