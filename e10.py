# e10
import os
import sys
import time
import socket 
import requests 
from colorama import Fore
def __tar__():
    os.system("clear")
    print(Fore.RED + "Hello , Welcome Back ;)")
    time.sleep(0.4)
    target = input(Fore.BLUE + "\n[" + Fore.RED + "!" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.GREEN + "Pleass Enter Your Adress Target" + Fore.YELLOW + " ==>  ")
    if target == "" or None:
        try:
            time.sleep(1)
            print(Fore.RED + "\n[!] ~ Error : Your Target Is None Or Not Found ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    my_list = ["xmlrpc.php" , "xmlrpc.login" , "xmlrpc" , "xmlrpc.admin" , "xmlrpc.robot.txt", "xmlrpc.bot" , "xmlrpc.search"]
    if not "http" in target + not "https" in target:
        target = "http://" + target
    s = target + "/wp-content/plugins/"
    if s.status_code == 404 or s.status_code == 500:
     try:   
        time.sleep(1)
        print(Fore.RED + "[-] ~ Error : Your Target Is Not Word Press ;(")
        time.sleep(1)
        sys.exit()
     except:
         pass   
    else:
        time.sleep(1)
        print(Fore.GREEN + "[+] ~ Ok , Your Target Is WordPress ;)")
        time.sleep(0.4)
        sys.exit()
    for i in my_list:
        t = target + "/" + i
        r = requests.get(t)
        if r.status_code == 200:
            print(Fore.GREEN + "[+] ~ " + Fore.GREEN + t)
            time.sleep(0.1)
        else:
            print(Fore.RED + "[-] ~ " + Fore.RED + t)
__tar__()
