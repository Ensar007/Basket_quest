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
def dag4():
    print("\nDag 4: En ny dag börjar. Du vaknar upp trött efter gårdagens firande.")
    print("Din tränare ringer dig.")
    print("1. Svara på samtalet")
    print("2. Ignorera samtalet")

    choice = input("Välj ett alternativ (1/2): ")
    if choice == "1":
        print("\nTränaren ger dig viktig information och ber dig att möta honom.")
        träffa_tränare()
    elif choice == "2":
        print("Du ignorerade samtalet och missade viktig information. Slut på spelet.")
        dag5()
    else:
        print("Ogiltigt val. Försök igen.")
        dag4()

def träffa_tränare():
    print("\nDu träffar tränaren och får veta om kommande matcher och möjligheter.")
    print("Vad vill du göra?")
    print("1. Förbered dig för nästa steg")
    print("2. Skjuta upp det till senare")

    choice = input("Välj ett alternativ (1/2): ")
    if choice == "1":
        print("Du förbereder dig för framtiden och är redo för nya utmaningar.!")
        dag5()
    elif choice == "2":
        print("Du skjuter upp det och missar en viktig möjlighet.")
        dag5()
    else:
        print("Ogiltigt val. Försök igen.")
        träffa_tränare()

# Starta spelet


def dag5():
    print("\nDag 5: Du har blivit scoutad av ett NBA-lag och behöver ta dig till USA!")
    print("Vad vill du göra först?")
    print("1. Hälsa på laget och berätta informationen för dem")
    print("2. Boka ett flyg direkt och förbereda dig")

    choice = input("Välj ett alternativ (1/2): ")
    if choice == "1":
        print("Du hälsar på laget, delar nyheten och går hem för att förbereda dig.")
    elif choice == "2":
        print("Du bokar ett flyg och börjar packa inför resan.")
    else:
        print("Ogiltigt val. Försök igen.")
        dag5()
        return

    print("\nDu anländer till USA och märker att två personer väntar på dig.")
    print("De representerar två NBA-lag som vill värva dig.")
    print("Vilket lag väljer du?")
    print("1. Brooklyn Nets")
    print("2. Golden State Warriors")

    choice = input("Välj ett alternativ (1/2): ")
    if choice == "1":
        print("Du valde Brooklyn Nets. De tar dig till deras träningsplats för att börja.")
        nets_rutin()
    elif choice == "2":
        print("Du valde Golden State Warriors. De tar dig till deras träningsplats för att börja.")
        warriors_rutin()
    else:
        print("Ogiltigt val. Försök igen.")
        dag5()

def nets_rutin():
    print("\nDu anländer till Brooklyn Nets träningsplats.")
    print("Vad vill du göra först?")
    print("1. Gå direkt till träningsplanen")
    print("2. Gå på en intervju och svara på frågor")

    choice = input("Välj ett alternativ (1/2): ")
    if choice == "1":
        print("Du börjar träna direkt och imponerar på dina nya lagkamrater. Spelet slutar här!")
    elif choice == "2":
        print("Du svarar på frågor och lär känna dina lagkamrater bättre. Spelet slutar här!")
    else:
        print("Ogiltigt val. Försök igen.")
        nets_rutin()

def warriors_rutin():
    print("\nDu anländer till Golden State Warriors träningsplats.")
    print("Vad vill du göra först?")
    print("1. Gå direkt till träningsplanen")
    print("2. Gå på en intervju och svara på frågor")

    choice = input("Välj ett alternativ (1/2): ")
    if choice == "1":
        print("Du börjar träna direkt och imponerar på dina nya lagkamrater. Spelet slutar här!")
        dag_sex()
    elif choice == "2":
        print("Du svarar på frågor och lär känna dina lagkamrater bättre. Spelet slutar här!")
        dag_sex()
    else:
        print("Ogiltigt val. Försök igen.")
       warriors_rutin()        
    
    def dag_sex():
    print("Dag 6 börjar!")
    print("Du vaknar och är jättepeppad.")
    val = input("Vill du gå direkt till träningsplatsen? (ja/nej): ").lower()

    if val == "ja":
        print("Du går direkt till träningsplatsen.")
        print("Slut på dag 6.")
        sista_dagen()
        return
    elif val == "nej":
        print("Du äter frukost.")
        print("Nu är du redo för att träna.")
        print("Du tar dig till träningsplatsen.")

        print("Din tränare ropar på alla i laget och pratar med er.")
        print("Han säger att imorgon kommer ni möta den bästa basketspelaren, LeBron James.")
        val = input("Vill du träna hela dagen eller gå hem och ta det lugnt? (träna/gå hem): ").lower()
    if val == "träna":
        print("Du tränar hela dagen, och är redo och peppad till morgondagens match")
    sista_dagen()


    def sista_dagen():
    print("Sista dagen är här!")
    print("Det är dags att möta den bästa basketspelaren och skapa historia.")

   
    print("\nDu har redan gjort allt du behöver och är på väg till matchplanen.")
    problem = input("Din bil stannar mitt på vägen! Vill du försöka laga bilen eller ta bussen? (laga/buss): ").lower()

    if problem == "laga":
        print("Du misslyckades att laga bilen och missade matchen. SLUT.")
        return
    
    elif problem == "buss":
        print("Du tog bussen och kommer fram till matchen i tid, men du måste gå direkt till planen.")

    
    print("\nDet har varit en seg match, men i 3:e quartern får du en chans att göra skillnad.")
    strategi = input("Vill du dribbla förbi eller försöka skjuta en 3-poängare? (dribbla/3-poängare): ").lower()

    if strategi == "dribbla":
        print("Du dribblar förbi en hoppande LeBron James, men din passning blockeras!")
        print("Du blir utbytt och sätts på bänken eftersom du är trött.")
    elif strategi == "3-poängare":
        print("Du försöker skjuta en 3-poängare, men LeBron James blockerar ditt skott.")
        print("Du blir utbytt och sätts på bänken.")


