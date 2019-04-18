def repository_tools_public():
    usuario = False
    while not usuario:
        print("(1) Respository Public")
        print("(2) Respository Private")
        print("(3) Back")
        usuario = int(input("Enter opctions:"))
        if usuario=="1":
            print ("s")
        if usuario ==2:
            print("")
        if usuario ==3:
            break
if __name__=="__main__":
    repository_tools_public()