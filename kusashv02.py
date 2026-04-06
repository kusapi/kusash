from os import system, chdir, getcwd
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from pyfiglet import figlet_format as figlet
import getpass

console=Console()
username=getpass.getuser()
header=figlet("KuSaSH\nCustom Shell")
path=getcwd()

def Value_Error_Message(value):
    print(f"[red]!HATA![red]: Yanlış değer girdiniz! --> '{value}'")

def FileNotFound_Error_Message(path):
    print(f"[red]!HATA![/red]: Yanlış veya Bilinmeyen Konum! --> '{path}'")

def Index_Error_Message(komut):
    print(f"[red]!HATA![/red]: Yanlış, Eksik veya Bilinmeyen komut --> '{komut}'\n Yardım için --> 'try --help' dene!")

def exit_the_shell():
    system("clear")
    print("![red]Çıkış[/red] [green]Başarılı[/green] | [red]Exit[/red] is [green]Succesful[/green]!")
    exit()
system("clear")
console.print(Panel(f"[red]{header}[/red]\n[yellow]yardım için 'try --help' yazın![/yellow]"))

try:
    while True:
        command_prompt=Prompt.ask(f"[green]{username}[/green] ~ [green]{path}[/green] -->    ")
        command_parts=command_prompt.split()
        try:
            match command_parts[0]:
                case "exit":
                    exit_the_shell()
                case "network":
                    try:
                        match command_parts[1]:
                            case "-mgr":
                                system("iwctl")
                            case "--ping":
                                target_ip = Prompt.ask("[yellow]IP address[/yellow]").strip()
                                if target_ip == "":
                                    Value_Error_Message(target_ip)
                                    continue  # shell loop devam eder

                                ping_count_str = Prompt.ask("[yellow]Ping Count[/yellow]").strip()
                                if ping_count_str == "":
                                    Value_Error_Message(ping_count_str)
                                    continue

                                try:
                                    ping_count = int(ping_count_str)
                                except ValueError:
                                    Value_Error_Message(ping_count_str)
                                    continue

                                system(f"ping -c {ping_count} {target_ip}")

                            case "--scan":
                                system("nmcli dev wifi rescan && nmcli -f IN-USE,SSID,SIGNAL dev wifi list")

                            case "--nmap":
                                nmap_command=Prompt.ask("[yellow]Nmap Komutu(başa nmap koymayın)    [/yellow]")
                                system(f"sudo nmap {nmap_command}")

                    except IndexError:
                        Index_Error_Message(command_prompt)
                case "try":
                    try:
                        match command_parts[1]:
                            case "--help":
                                system("cat help.txt")
                            case "-p":
                                try:
                                    try:
                                        yazi=" ".join(command_parts[2:])
                                        print(f"[yellow]{yazi}[/yellow]")
                                    except IndexError:
                                        Index_Error_Message(command_prompt)

                                except IndexError:
                                    Index_Error_Message(command_prompt)
                            case "-e":
                                try:
                                    exect = " ".join(command_parts[2:])
                                    if(exect==""):
                                        print("[red]!HATA![/red] exec(-e) ekinden sonra bir veya birden fazla sistem kodu gelmeli!")
                                    else:
                                        system(exect)
                                except IndexError:
                                    Index_Error_Message(command_prompt)
                            case "--e":
                                try:
                                    exect = " ".join(command_parts[2:])
                                    if(exect!=""):
                                        system(f"sudo {exect}")
                                    else:
                                        print("[red]!HATA![/red] exec(-e) ekinden sonra bir veya birden fazla sistem kodu gelmeli!")
                                except IndexError:
                                    Index_Error_Message(command_prompt)
                            case "--kusafetch":
                                exect="neofetch"
                                system(exect)
                            case "-cd":
                                try:
                                    try:
                                        go_to_path=" ".join(command_parts[2:])
                                        chdir(go_to_path)
                                        path=getcwd()
                                    except FileNotFoundError:
                                        FileNotFound_Error_Message(go_to_path)

                                except IndexError:
                                    Index_Error_Message(command_prompt)
                            case "-pkg":
                                package_manager=Prompt.ask("[yellow]Paket Yöneticinizin adı [/yellow]")
                                package_name=Prompt.ask("[yellow]Indirmek istediğiniiz paketin adı  [/yellow]")
                                system(f"sudo {package_manager} install {package_name}")
                            case _:
                                Index_Error_Message(command_prompt)

                    except IndexError:
                        Index_Error_Message(command_prompt)
                case _:
                    Index_Error_Message(command_prompt)
        except IndexError:
            Index_Error_Message(command_prompt)

except (KeyboardInterrupt, EOFError):
    exit_the_shell()