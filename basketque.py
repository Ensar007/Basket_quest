import os
import time
from colorama import Fore, init

def start_game():
    print("\nvälkommen till Basket quest dag 1")
    time.sleep(2)
    os.system("cls")
    intro = R"""
     ___             _        _      ____                  _  
    |  _ \          | |      | |    / __ \                | |  
    | |_) | __ _ ___| | _____| |_  | |  | |_   _  ___  ___| |_ 
    |  _ < / _` / __| |/ / _ \ __| | |  | | | | |/ _ \/ __| __|
    | |_) | (_| \__ \   <  __/ |_  | |__| | |_| |  __/\__ \ |_ 
    |____/ \__,_|___/_|\_\___|\__|  \___\_\\__,_|\___||___/\__|"""   
    print(Fore.BLUE+intro)
    init(autoreset=True)
    time.sleep(1.9)
    os.system("cls")
    print("Dag 1: Vad vill du göra?")
    print("1. Gå till träningshallen")
    print("2. Stanna hemma och sova")

    choice = input("Välj ett alternativ (1/2): ")
    if choice == "1":
        träningshallen()
    elif choice == "2":
        print("Du stannade hemma och sov. Slut på dagen.")
        dag2()
    else:
        print("Ogiltigt val. Försök igen.")
        start_game()

def träningshallen():
    print("Du är nu i träningshallen. Vad vill du göra?")
    print("1. Träna på dribbling")
    print("2. Träna styrketräning")
    print("3. Träna på 3-poängare")

    choice = input("Välj ett alternativ (1/2/3): ")
    if choice == "1":
        dribbling()
    elif choice == "2":
        styrketräning()
    elif choice == "3":
        trepoängare()    
        
    else:
        print("Ogiltigt val. Försök igen.")
        träningshallen()

def dribbling():
    print("Du tränar på dribbling. Vad vill du göra härnäst?")
    print("1. Konditionsträning")
    print("2. Gå hem och vila")

    choice = input("Välj ett alternativ (1/2): ")
    if choice == "1":
        konditionsträning()
    elif choice == "2":
        print("Du gick hem och vilade. Slut på dagen.")
    else:
        print("Ogiltigt val. Försök igen.")
        dribbling()

def styrketräning():
    print("Du tränar styrka. Vad vill du göra härnäst?")
    print("1. Gå tillbaka till träningshallen")
    print("2. Gå hem och vila")

    choice = input("Välj ett alternativ (1/2): ")
    if choice == "1":
        träningshallen()
    elif choice == "2":
        print("Du gick hem och vilade. Slut på dagen.")
    else:
        print("Ogiltigt val. Försök igen.")
        styrketräning()

def trepoängare():
    animation()
    print("Du tränar på 3-poängsskott. Vad vill du göra härnäst?")
    print("1. Konditionsträning")
    print("2. Gå hem och vila")

    choice = input("Välj ett alternativ (1/2): ")
    if choice == "1":
        konditionsträning()
    elif choice == "2":
        print("Du gick hem och vilade. Slut på dagen.")
        dag2()
    else:
        print("Ogiltigt val. Försök igen.")
        trepoängare()

def animation():
    
    tre = R"""
        |\
         \O
          |
         /|
        |  \
        """
    print(tre)
    time.sleep(1)
    os.system("cls")
    skott = R"""   

            
    /|          
    \|=--           o
      ##
                    \\
                   /  \O
                O_/    T
                T     /|
                |\   | |
    ____________|_|________


        """
    print(skott)

    time.sleep(1)
    os.system("cls")
    skott2 = R"""   

            
    /|          o
    \|=--           o
      ##
                    \\
                   /  \O
                O_/    T
                T     /|
                |\   | |
    ____________|_|________


        """
    print(skott2)

    time.sleep(1)
    os.system("cls")
    skott3 = R"""   

            o
    /|           o
    \|=--           o
      ##
                    \\
                   /  \O
                O_/    T
                T     /|
                |\   | |
    ____________|_|________


        """
    print(skott3)

    time.sleep(1)
    os.system("cls")
    skott4 = R"""                                                                                                                                                                                                                                                                                                                                                                                                                                                               

            o
    /|  o        o
    \|=--           o
      ##
                    \\
                   /  \O
                O_/    T
                T     /|
                |\   | |
    ____________|_|________


        """
    print(skott4)


def konditionsträning():
    print("Nu så har du ett väldigt intensivt tränings pass i kondition och du springer länger!")
    print("Dag 1 är slut.")
    dag2()