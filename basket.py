def start_game():
    print("Dag 1: Vad vill du göra?")
    print("1. Gå till träningshallen")
    print("2. Stanna hemma och sova")

    choice = input("Välj ett alternativ (1/2): ")
    if choice == "1":
        träningshallen()
    elif choice == "2":
        print("Du stannade hemma och sov. Slut på dagen.")
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
    print("Du tränar på 3-poängsskott. Vad vill du göra härnäst?")
    print("1. Konditionsträning")
    print("2. Gå hem och vila")

    choice = input("Välj ett alternativ (1/2): ")
    if choice == "1":
        konditionsträning()
    elif choice == "2":
        print("Du gick hem och vilade. Slut på dagen.")
    else:
        print("Ogiltigt val. Försök igen.")
        trepoängare()

def konditionsträning():
    print("Du tränar kondition. Bra jobbat!")
    print("Dagen är slut. Slut på spelet.")

start_game()