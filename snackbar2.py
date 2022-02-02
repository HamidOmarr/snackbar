Bestellen = "ja"
while Bestellen  == "ja":
    TotaalPatat = int(input("Hoeveel Patat?"))
    TotaalFrikadellen = int(input("Hoeveel Frikadellen?"))
    TotaalKroketten = int(input("Hoeveel Kroketten?"))

    Zonder = 0 
    Gewoon = 0
    Metbrood = 0 
    xxl = 0 
    vega = 0 
    FrietSaus = 0 
    Ketchup = 0 

    for x in range(TotaalPatat):
        Patatsaus = input("Wat voor saus wil op deze patat? Ketchup of FrietSaus")
        if Patatsaus == "FrietSaus":
            FrietSaus = FrietSaus + 1
        if Patatsaus == "Ketchup":
            Ketchup = Ketchup + 1
    print ("FrietSaus:" ,FrietSaus, "X" ,"0.30","=",0.30*FrietSaus)
    print ("Ketchup:" ,Ketchup, "X" ,"0.20","=",0.20*Ketchup)

    for x in range(TotaalFrikadellen):
        FrikandelSoort = input("welke soort fricandel: gewone, Vega of Xxl?")
        if FrikandelSoort == "Vega":
            vega = vega + 1
        if FrikandelSoort == "Xxl":
            xxl = xxl + 1
        if FrikandelSoort == "Gewoon":
            Gewoon = Gewoon + 1
    print ("Gewoon:" ,Gewoon, "X","0","=",0*Gewoon)
    print ("vega:" ,vega, "X","0.30","=",0.30*vega)
    print ("xxl:" ,xxl, "X","1.20","=",1.20*xxl)

    for x in range(TotaalKroketten):
        KroketBrood = input("Met of Zonder Brood?")
        if KroketBrood == "Met":
            Metbrood = Metbrood + 1
        if KroketBrood == "Zonder":
            Zonder = Zonder + 1
    print ("Metbrood:" ,Metbrood, "X","0.20","=",0.20*Metbrood)
    print ("Zonder:" ,Zonder, "X","0","=",0*Zonder)


        
    verderBestellen = input("Wil je nog meer bestellen?")  
    if verderBestellen == "n":
        Bestellen = "nee"


    Patat = 1.50 * TotaalPatat
    Frikadellen = 1.80 * TotaalFrikadellen
    Kroketten = 2.00 * TotaalKroketten
    totaal = Patat + Frikadellen + Kroketten
    Bestelkosten = 2.30
    kortingboven40 = totaal / 100 * 5
    kortingboven100 = totaal / 100 * 7.5

if TotaalPatat > 0:
    print( "Patat:" ,"€", Patat , "Voor" , TotaalPatat ,"stukken")
if TotaalFrikadellen > 0:
    print("Frikadellen:", "€", Frikadellen, "Voor", TotaalFrikadellen,"stukken") 
if TotaalKroketten > 0:
    print("Kroketten:" , "€", Kroketten, "Voor", TotaalKroketten,"stukken")


if totaal < 10:
    totaal = totaal + Bestelkosten
    print ("BestelKosten:" ,"€", Bestelkosten)

if totaal >= 40:
    totaal = totaal - kortingboven40
    print ("Korting 5%:" , "€", kortingboven40)

if totaal >= 100:
    totaal = totaal - kortingboven100
    print ("Korting 7,5%:" , "€",kortingboven100)

print (int(totaal))


