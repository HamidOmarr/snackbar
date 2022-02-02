import random
def Snackbar():
    TotaalPatat = int(input("Hoeveel Patat?"))
    TotaalFrikadellen = int(input("Hoeveel Frikadellen?"))
    TotaalKroketten = int(input("Hoeveel Kroketten?"))

    return TotaalPatat,TotaalFrikadellen,TotaalKroketten

def PatatSaus(TotaalPatat):
    FrietSaus = 0
    Ketchup = 0 
    for x in range(TotaalPatat):
        Patatsaus = input("Wat voor saus wil op deze patat? Ketchup of FrietSaus")
        if Patatsaus == "FrietSaus":
            FrietSaus = FrietSaus + 1
        if Patatsaus == "Ketchup":
            Ketchup = Ketchup + 1
    TotaalSausPrijs = (0.30*FrietSaus) + (0.20*Ketchup)
    return TotaalSausPrijs


def Frikandelkeuzen(TotaalFrikadellen):
    Gewoon = 0
    Xxl = 0 
    vega = 0 
    for x in range(TotaalFrikadellen):
        FrikandelSoort = input("welke soort fricandel: Gewoon , Vega of Xxl ?")
        if FrikandelSoort == "Vega":
            vega = vega + 1
        if FrikandelSoort == "Xxl":
            Xxl = Xxl + 1
        if FrikandelSoort == "Gewoon":
            Gewoon = Gewoon + 1
    TotaalFrikandelPrijs = (0.30*vega) + (1.20*Xxl)
    return TotaalFrikandelPrijs

def KroketMetBrood(TotaalKroketten):
    Zonder = 0 
    Metbrood = 0
    for x in range(TotaalKroketten):
        KroketBrood = input("Met of Zonder Brood?")
        if KroketBrood == "Met":
            Metbrood = Metbrood + 1
        if KroketBrood == "Zonder":
            Zonder = Zonder + 1
    TotaalKroketPrijs =  0.20*Metbrood
    return TotaalKroketPrijs

def bittergarnituur():
    SupriseSnacks = ["Bitterbal","Kaasvlammetje","Gehaktbal","Kipburger"]
    SupriseBitter = input("Wil jij een surprise bittergarnituur?")
    if SupriseBitter == "j": 
        GrooteSnack = input("mini, normal of big?")
        SnackRandom = random.choice(SupriseSnacks)
        print (SnackRandom)
    return SnackRandom


def BijKosten(TotaalPatat,TotaalFrikadellen,TotaalKroketten,TotaalSausPrijs,TotaalFrikandelPrijs,TotaalKroketPrijs,SnackRandom):
    Patat = (1.50 * TotaalPatat) + TotaalSausPrijs
    Frikadellen = 1.80 * TotaalFrikadellen + TotaalFrikandelPrijs
    Kroketten = 2.00 * TotaalKroketten + TotaalKroketPrijs
    totaal = Patat + Frikadellen + Kroketten
    Bestelkosten = 2.30
    kortingboven40 = totaal / 100 * 5
    kortingboven100 = totaal / 100 * 7.5
    print (SnackRandom)
    if TotaalPatat > 0:
        print( "Patat:","€",Patat)
    if TotaalFrikadellen > 0:
        print("Frikadellen:","€",Frikadellen) 
    if TotaalKroketten > 0:
        print("Kroketten:","€",Kroketten)
    if SnackRandom:
        print(SnackRandom,":","€","1.0")


    if totaal < 10:
        totaal = totaal + Bestelkosten
        print ("BestelKosten:" ,"€", Bestelkosten)

    if totaal >= 40:
        totaal = totaal - kortingboven40
        print ("Korting 5%:" , "€", kortingboven40)

    if totaal >= 100:
        totaal = totaal - kortingboven100
        print ("Korting 7,5%:" , "€",kortingboven100)

    print ("Totaal:","€",totaal)


def SausV():
    Ketchup = 0.20
    Frietsaus = 0.30 
    Curry = 0.20 
    Mosterd = 0.10 
    print ("----------------------------------------------------")
    print ("    Ketchup: €0.20  ")
    print ("    Frietsaus: €0.30  ")
    print ("    Curry: €0.20  ")
    print ("    Mosterd: €0.10  ")
    print ("----------------------------------------------------")
    Sausvraag = input("Wat voor Saus wil je hierop?")



Bestellen = True
while Bestellen == True:
    HvlPatat, Hvlfrikandel, HvlKroket = Snackbar()
    TotaalSaus = PatatSaus(HvlPatat)
    TotaalFrikandel = Frikandelkeuzen(Hvlfrikandel)
    TotaalKroket = KroketMetBrood(HvlKroket)
    TotaalSnacks = bittergarnituur()
    verderBestellen = input("Wil je nog meer bestellen?")
    if verderBestellen == "n":
        BijKosten(HvlPatat,Hvlfrikandel,HvlKroket,TotaalSaus,TotaalFrikandel,TotaalKroket,TotaalSnacks)
        Bestellen = False



