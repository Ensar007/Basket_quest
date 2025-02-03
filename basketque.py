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



def dag2():
    print("\nDag 2: Orkar du träna idag?")
    print("1. Ja")
    print("2. Nej")
    choice = input("Välj ett alternativ (1/2): ")
    if choice == "1":
        träning_dag2()
    elif choice == "2":
        print("Du stannade hemma och vilade. Slut på Dag 2.")
        dag3()
    else:
        print("Ogiltigt val. Försök igen.")

def träning_dag2():
    print("\nDu gör dig redo för träning och tar bussen till träningshallen.")
    print("Tränaren ber dig träna på det du inte gjorde Dag 1.")
    print("Vad vill du göra?")
    print("1. Träna dribbling")
    print("2. Träna styrketräning")
    print("3. Träna 3-poängsskott")

    choice = input("Välj ett alternativ (1/2/3): ")
    if choice == "1":
        print("Du tränar på dribbling.")
    elif choice == "2":
        print("Du tränar styrketräning.")
    elif choice == "3":
        print("Du tränar på 3-poängsskott.")
        animation()
    else:
        print("Ogiltigt val. Försök igen.")
        träning_dag2()

    print("\nEfter träningen har tränaren ett samtal med laget inför matchen imorgon.")
    gå_hem()

def gå_hem():
    print("\nTräningen är över. Vad vill du göra?")
    print("1. Vila hemma")
    print("2. Gå ut och spela med vänner")

    choice = input("Välj ett alternativ (1/2): ")
    if choice == "1":
        print("Du går hem och vilar. Slut på Dag 2.")
        dag3()
    elif choice == "2":
        print("Du går ut och spelar med vänner. Slut på Dag 2.")
        dag3()
    else:
        print("Ogiltigt val. Försök igen.")
        gå_hem()


def dag3():
    print("\nDag 3: Matchdag! Vad vill du göra?")
    print("1. Stanna hemma")
    print("2. Delta i matchen")

    choice = input("Välj ett alternativ (1/2): ")
    if choice == "1":
        print("Du valde att stanna hemma. Slut på dag 3.")
        dag4()
    elif choice == "2":
        spela_match()
    else:
        print("Ogiltigt val. Försök igen.")
        dag3()

def spela_match():
    print("\nMatchen är igång! Hur vill du spela?")
    print("1. Ge allt och spela ditt bästa (100%)")
    print("2. Ta det lite lugnare (50-70%)")

    choice = input("Välj ett alternativ (1/2): ")
    if choice == "1":
        print("Du spelade ditt bästa och vann matchen! Scouts var på plats och märkte dig!")
        fira_seger()
    elif choice == "2":
        print("Du tog det lugnare och förlorade matchen. Slut på dag 3.")
        dag4()
    else:
        print("Ogiltigt val. Försök igen.")
        spela_match()

def fira_seger():
    print("\nVad vill du göra efter matchen?")
    print("1. Gå hem och vila")
    print("2. Gå ut med laget och fira")

    choice = input("Välj ett alternativ (1/2): ")
    if choice == "1":
        print("Du gick hem och vilade. Slut på dag 3.")
        dag4()
    elif choice == "2":
        print("Du gick ut och firade med laget. Du hade roligt och kommer hem sent. Slut på dag 3.")
        dag4()
    else:
        print("Ogiltigt val. Försök igen.")
        fira_seger()