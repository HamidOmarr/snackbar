TotaalPatat = int(input("Hoeveel Patat?"))
TotaalFrikadellen = int(input("Hoeveel Frikadellen?"))
TotaalKroketten = int(input("Hoeveel Kroketten?"))

Metbrood = 0
xxl = 0
vega = 0
FrietSaus = 0 
Ketchup = 0
Patat = 1.50 * TotaalPatat
Frikadellen = 1.80 * TotaalFrikadellen
Kroketten = 2.00 * TotaalKroketten
Bestelkosten = 2.30
totaal = Patat + Frikadellen + Kroketten
kortingboven40 = totaal / 100 * 5
kortingboven100 = totaal / 100 * 7.5

for x in range(TotaalPatat):
    Patatsaus = input("Wat voor saus wil op deze patat? Ketchup of FrietSaus")
    if Patatsaus == "FrietSaus":
        FrietSaus = FrietSaus + 1
    if Patatsaus == "Ketchup":
        Ketchup = Ketchup + 1
print ("FrietSaus:" ,FrietSaus, "X")
print ("Ketchup:" ,Ketchup, "X")

for x in range(TotaalFrikadellen):
    FricandelSoort = input("welke soort fricandel: gewone, vega of XXL?")
    if FricandelSoort == "Vega":
        vega = vega + 1
    if FricandelSoort == "Xxl":
        xxl = xxl + 1
    if FricandelSoort == "Gewoon":
        Gewoon = 0
        Gewoon = Gewoon + 1
print ("Gewoon:" ,Gewoon, "X")
print ("vega:" ,vega, "X")
print ("xxl:" ,xxl, "X")

for x in range(TotaalKroketten):
    KroketBrood = input("Met of Zonder Brood?")
    if KroketBrood == "Met":
        Metbrood = Metbrood + 1
    if KroketBrood == "Zonder":
        Zonder = 0
        Zonder = Zonder + 1
print ("Metbrood:" ,Metbrood, "X")
print ("Zonder:" ,Zonder, "X")


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
