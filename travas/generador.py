from material.generate import generate
from material.defauld import defauld
from colorama import init, Fore, Back, Style
init()

def menu():
    print(Fore.LIGHTMAGENTA_EX + "----------------------------------------------")
    impMenu = Fore.RED + """
████████╗██████╗░░█████╗░██╗░░░██╗░█████╗░░██████╗
╚══██╔══╝██╔══██╗██╔══██╗██║░░░██║██╔══██╗██╔════╝
░░░██║░░░██████╔╝███████║╚██╗░██╔╝███████║╚█████╗░
░░░██║░░░██╔══██╗██╔══██║░╚████╔╝░██╔══██║░╚═══██╗
░░░██║░░░██║░░██║██║░░██║░░╚██╔╝░░██║░░██║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░



█▄▄ █▄█   ░░█ █▀█ █▀ █▀▀   █▀▀ ▄▀█ █▄▄ █▀█ █ █▀▀ █░░
█▄█ ░█░   █▄█ █▄█ ▄█ ██▄   █▄█ █▀█ █▄█ █▀▄ █ ██▄ █▄▄

[1]𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕖
[2]𝔻𝕖𝕗𝕒𝕦𝕝𝕕
[3]𝔼𝕩𝕚𝕥

What option did you choose?: """ + Fore.GREEN
    while True:
        try:
            res = int(input(impMenu))
            if(res == 1):
                generate()
            elif(res == 2):
                defauld()
            elif(res == 3):
                print(Fore.BLUE + "L̳o̳g̳g̳i̳n̳g̳ o̳u̳t̳ o̳f̳ t̳h̳e̳ s̳y̳s̳t̳e̳m̳...")
                break
            else:
                print(Fore.BLUE + f"O̳p̳t̳i̳o̳n̳ {res}d̳o̳e̳s̳ n̳o̳t̳ e̳x̳i̳s̳t̳")
        except(ValueError):
            print(Fore.BLUE + """
W̳r̳i̳t̳e̳ w̳h̳o̳l̳e̳ n̳u̳m̳b̳e̳r̳s̳ n̳o̳t̳ l̳e̳t̳t̳e̳r̳s̳
            """)
        finally:
            print(Fore.LIGHTMAGENTA_EX + "----------------------------------------------")