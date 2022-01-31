TotaalPatat = int(input("Hoeveel Patat?"))
TotaalFrikadellen = int(input("Hoeveel Frikadellen?"))
TotaalKroketten = int(input("Hoeveel Kroketten?"))

Patat = 1.50 * TotaalPatat
Frikadellen = 1.80 * TotaalFrikadellen
Kroketten = 2.00 * TotaalKroketten
Bestelkosten = 2.30
totaal = Patat + Frikadellen + Kroketten
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
