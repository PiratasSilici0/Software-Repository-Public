import login_user
import repository_tools_public
import login_new_user
import capa_login
import public_software
capa_login.capa_login()
login_user.login_user()
usuario_user = False
while not usuario_user:
    print("\033[0;34;1m|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|\033[m")
    print("(1) \033[0;33;1mUser Setting\033[m")
    print("(2) \033[0;33;1mRespository \033[m")
    print("(3) Public Software\033[0;33;1m")
    print("(4) Back")
    usuario = str(input("\033[0;33;1mEnter options:\033[m"))
    print("\033[0;34;1m|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|\033[m")
    if usuario == "1":
        login_new_user.login_new_user()
    if usuario == "2":
        repository_tools_public.repository_tools_public()
    if usuario =="3":
        public_software.public_software()
    if usuario=="4":
        break


