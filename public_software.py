def public_software():
    print("(1) Software Server")
    print("(2) Software tools")
    usuario = str(input("Enter options:"))
    if usuario =="1":
        print("(1) Ubuntu Server 18.04.2 LTS (2) Ubuntu Server 18.10 (3) Windows 2019")
    if usuario =="2":
        print("(1) Kali Linux (2) Debian (3) Ubuntu (4) Linux Mint (5) Opensuse (6) Manjaro (7) Elementary OS (8) Fedora (9) Zorin OS (10) CentOS")
if __name__=="__main__":
    public_software()