from colorama import init, Fore, Back, Style
import random
init()
def generate():
    generate_menu = Fore.WHITE + """
----------------------------------------------------
█▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀▀
█▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ ██▄
----------------------------------------------------

[1]┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘

[2]████████████████████████████████████████

[3]¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶

[4]§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§

[5]All

[6]Exit

What option did you choose?: """ + Fore.YELLOW

    while True:
        try:
            num = int(input(generate_menu))
            if(num == 1):
                info(num)
            elif(num == 2):
                info(num)
            elif(num == 3):
                info(num)
            elif(num == 4):
                info(num)
            elif(num == 5):
                info(num)
            elif(num == 6):
                print(Fore.BLUE + """
s̳h̳u̳t̳t̳i̳n̳g̳ d̳o̳w̳n̳ g̳e̳n̳e̳r̳a̳t̳o̳r̳...
            """)
                break
        except(ValueError):
            print(Fore.BLUE + """
W̳r̳i̳t̳e̳ w̳h̳o̳l̳e̳ n̳u̳m̳b̳e̳r̳s̳ n̳o̳t̳ l̳e̳t̳t̳e̳r̳s̳
            """)

def info(num):
    try:
        preg1 = input(Fore.CYAN + "What name do you want to give it?: " + Fore.YELLOW)
        print(Fore.RED + """
---------------------------------------
Next, put a link that you want to be added, 
if you want the default one, press enter
---------------------------------------
""")
        preg2 = input(Fore.CYAN + "link: " + Fore.YELLOW)

        preg3 = int(input(Fore.CYAN + "How many times do you want to repeat it?: " + Fore.YELLOW))

        if(preg2 == "" and preg1 == ""):
            trava(num,"T͊̽̕R̔͝͝A̾͊͌V̐͐͝A͋̾͌","https://www.whatsapp.com/",preg3)
        elif(preg2 == "" or preg2 == " "):
            trava(num,preg1,"https://www.whatsapp.com/",preg3)
        else:
            trava(num,preg1,preg2,preg3)
    except(ValueError):
            print(Fore.BLUE + """
T̳h̳e̳r̳e̳ w̳a̳s̳ a̳ m̳i̳s̳t̳a̳k̳e̳
            """)

def trava(num,preg1,preg2,preg3):
    listStyle = ["┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘",
    "████████████████████████████████████████",
    "¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶",
    "§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§"]
    print(Fore.LIGHTMAGENTA_EX + "----------------------------------------------")
    contador = 0
    travaImp = ""
    while(contador < preg3):
        if(num != 5 and num < 6):
            travaImp += listStyle[num - 1]
        else:
            random_num = random.randint(0,3)
            travaImp += listStyle[random_num]
        contador += 1
    print(Fore.GREEN + f"""
( ❛︠ ‿ ︡❛)✽✽✽✽✽✽✽✽{preg1}✽✽✽✽✽✽✽✽( ❛︠ ‿ ︡❛){travaImp}{preg2}
    """)
    print(Fore.LIGHTMAGENTA_EX + "----------------------------------------------")