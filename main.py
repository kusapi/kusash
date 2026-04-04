from sys import platform
import platform as pf
from rich import print
from rich.console import Console
from rich.panel import Panel
from pyfiglet import figlet_format
import getpass
from os import system
helplist="""Ekler kullanımı: 
    -p -->  try -p <Yazı>
        çıktı: Yazı
    -e --> try -e <Your Terminal Code here>
        örnek kullanım! --> try -e echo Hello World!
            çıktı: Hello World!
    -pkg --> try -pkg install <paket adı>
         --> try -pkg remove <paket adı>
         --> try -pkg list <paket adı>
        !NOT! --> Bu pkg eki apt paket yöneticisi kullanır eğer apt paket yöneticiniz yok ise hata alırsınız!!!
    --kusafetch --> try --kusafetch
        çıktı: <sistem bilgileriniz>
    ! SÜRÜM --> v0.1 !"""

console = Console()
system("clear")
h = figlet_format("KusaShell", font="slant")
console.print(Panel(f"{h}\nYardim icin ---> 'try --help'"))
uname = pf.uname()

while True:
    username = getpass.getuser()
    cmd = input(f"{username} | KuSaShell ~$   ")
    cmd = cmd.split()
    if(cmd[0] != "try"):
        non=cmd[0]
        print(f"[red]!HATA! --> Bilinmeyen[/red][cyan] '{non}'[/cyan], Yardım için: 'try --help'")
    else:
        if(cmd[1] == "-p"):
            yazi = " ".join(cmd[2:])
            print(f"[yellow]{yazi}[/yellow]")
        elif(cmd[1] == "-e"):
            exec = " ".join(cmd[2:])
            system(exec)
        elif(cmd[1] == "-pkg"):
            if(cmd[2] == "install"):
                pack = " ".join(cmd[3:])
                system(f"apt install {pack} -y")
            elif(cmd[2] == "remove"):
                pack = " ".join(cmd[3:])
                system(f"apt remove {pack} -y")
            elif(cmd[2] == "list"):
                system("apt list --installed")
            else:
                ek = cmd[2]
                print(f"[red]!HATA! --> Bilinmeyen Ek[/red][cyan] '{ek}'[/cyan], Yardım için 'try --help'")
        elif(cmd[1] == "--kusafetch"):
            print(uname)
        elif(cmd[1] == "--help"):
            print(helplist)
        elif(cmd[1] == "--whoami"):
            print(username)
        else:
            ek = cmd[1]
            print(f"[red]!HATA! --> Bilinmeyen Ek[/red][cyan] '{ek}'[/cyan], Yardım için 'try --help'")
