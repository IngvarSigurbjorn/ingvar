# Settu nafn og dagsetningu efst í kóða sem komment
# Kommentaðu verkefnið vel
# Lidur 1: Nafn
#Forrit biður um nafn notanda og uppáhalds fag.
#Forritið skifar svo á skjáinn:
#Velkomin í uppáhalds fag þetta verður skemmtileg önn hjá okkur nafn
#nafn

nafn = input("hvað heitir þú:")#hér er beðið um nafn
fag = input("hvað er uppáhals fægið þitt:")#hér er beðið um fag

#hér eru upplýsingar prentaðar
print(f"velkominn í {fag} þetta verður skemtileg önn hjá okkur {nafn}") #hér prentast útkoman


# Lidur 2: Heiltölur
#Forrit biður um tvær heiltölur.
#Forritið a) margfaldar tölurnar saman
# b) dregur seinni töluna frá fyrri
#c) athugar hversu oft seinni talan gengur upp í fyrri ( heiltöludeiling )
# d) athuga afgang ef seinni tölu er deilt í fyrri tölu ( modulus )

tala1 = int(input("hver er tala 1: "))# hér er beðið um tölu eitt
tala2 = int(input("hver er tala 2: "))# hér er beðið um tölu tvö
tala3 = tala1 * tala2 #hér er tala1 og 2 mínusað
tala4 = tala1 - tala2 #hér er tala1 og 2 margfaldað
print(f"{tala1} sinnum {tala2} er {tala3}")  # hér kemur útkoma tölu3
print(f"{tala1} mínus {tala2} er {tala4}") # hér kemur útkoma tölu4


# Lidur 3: Hringur
#Forrit biður notanda um radíus hrings.
#Forritið reiknar svo út og skrifar á skjá bæði ummál hrings og flatarmál með 1 aukastaf.
#Ummál hring er 2*radíus*π
#Flatarmál hrings er radíus*radíus* π eða radíus2* π

radius = int(input("hver er radius hringsins:"))#hér er beðið um radius hringsins
ummal = 2*radius*3.14
flatarmal = radius*radius*3.14
utkoma1 = round(ummal,1)
utkoma2 = round(flatarmal,1)
print(format(f"ummál hringsins er {utkoma1}"))#hér kemur ummál hringsins
print(format(f"flatarmál hringsins er {utkoma2}"))#hér kemur flatarmál hringsins


# Lidur 4: Aldur
#Forrit biður notanda um aldur sinn og aldur pabba síns.
#Forritið reiknar svo út og skrifar á skjá hversu gamall pabbinn var þegar notandinn fæddist.

tala1 = int(input("hversu gammall ert þú:"))# hér setur þú inn aldurinn þinn
tala2 = int(input("hversu gamall er pabbi þinn:"))# hér setur þú in aldur pabba þíns
tala3 = tala2 - tala1

print(f"pabbi þinn var {tala3} ára þegar þú fæddist")#útkoma

# Lidur 5: Meðalaldur
#Forrit biður um aldur þriggja einstaklinga.
#Forritið reiknar svo meðal aldurinn og skrifar svar á skjá með 2 aukastöfum.
#FORR1FG05AU Upplýsingatækniskólinn

#ég vissi ekki hverni ég átti að gera 5


# Lidur 6: Miðju tala
#Forritið spyr um þrjár heiltölur.
#Það má ekki slá inn sömu töluna tvisvar sinnum.
#Forritið skrifar síðan út hver talnanna er í miðjunni.

print("sláðu inn 3 tölur eina í einu með ENTER. Passa að engin sé eins")
t1 = int(input("tala 1:"))
t2 = int(input("tala 2:"))
t3 = int(input("tala 3:"))
mid = 0
if t1 == t2 or t2 == t3 or t3 == t1:
    print("ekki slá inn sömu tölu tvisvar")
    t1 = int(input("tala 1:")) ##hér 
    t2 = int(input("tala 2:"))
    t3 = int(input("tala 3:"))

if t1 < t2 and t2 < t3:
      print("miðjan er ",t2)

elif t2 < t3 and t3 < t1:
      print("miðjan er ",t3)

elif t3 < t1 and t1 < t2:
    print("miðjan er ",t1)


# Lidur 7: Tommur_Sentimetra
#Forritið umbreytir tommum í sentimetra eða öfugt.
#Forritið spyr um hvort umbreyta eigi tommum í sentimetra eða sentimetrum í tommur.
#Forritið spyr síðan um aðra stærðina en reiknar hina.
#Í einni tommu eru 2.54 sentimetrar.
#Svarið með 2 aukastöfum.

tala1 = float(input("skráðu inn tölu sem er annaðhvort sentimeter eða tomma:"))
tala2 = tala1 * 2.54
tala3 = tala1 / 2.54
utkoma = round(tala2, 2)
utkoma2 = round(tala3, 2)
spurning = input("langar þig að vita hvað talan er mikil í tommu(t) eða í sentimetrum(s) :")
if spurning == ("s"): 
    print (f"þú ert með {utkoma} sentimetrar")

elif spurning == ("t"):
    print (f"þú ert með {utkoma2} tommur")


# Lidur 8: Árstíðir
#Forritið spyr um númer mánaðar. Forritið skrifar síðan eftirfarandi út:
#Ef sleginn er inn talan 1‐3 skrifast út ”Nú er daginn tekið að lengja.”
#Ef sleginn er inn talan 4‐5 skrifast út ”Vorið er komið og grundirnar gróa.”
#Ef sleginn er inn talan 6‐8 skrifast út ”Núna er sumarið komið með blóm í haga.”
#Ef sleginn er inn talan 9‐10 skrifast út ”Núna er haustið gengið í garð.”
#Ef sleginn er inn talan 11‐12 ”Núna styttist í jólin”
#Ef sleginn er inn talan sem er 0 eða minni eða 13 og hærri á að skrifa “Rangur innsláttur”.


t1 = input("hver er mánuðurinn: ")# hér er spyrt um mánuðinn
if t1 == ("1"):
    print("Nú er daginn tekið að lengja")
elif t1 == ("2"):
    print("Nú er daginn tekið að lengja")
elif t1 == ("3"):
    print("Nú er daginn tekið að lengja")
elif t1 == ("4"):
    print("Vorið er komið og grundirnar gróa")
elif t1 == ("5"):
    print("Vorið er komið og grundirnar gróa")
elif t1 == ("6"):
    print("Núna er sumarið komið með blóm í haga")
elif t1 == ("7"):
    print("Núna er sumarið komið með blóm í haga")
elif t1 == ("8"):
    print("Núna er sumarið komið með blóm í haga")
elif t1 == ("9"):
    print("Núna er haustið gengið í garð")
elif t1 == ("10"):
    print("Núna er haustið gengið í garð")
elif t1 == ("11"):
    print("Núna styttist í jólin")
elif t1 == ("12"):
    print("Núna styttist í jólin")

else: print("Rangur innslátur") #útkoma ef insláturinn er er rangur 
#Ekki alveg þægilegasti koði 


# Lidur 9: Talnabil
#Forritið biður notanda um tölu sem er lægri en 0 eða hærri en 10.
#Ef notandi slær inn tölu frá 0 til 10 (að þeim meðtöldum) birtist "Þessi tala er ekki lægri en núll
#eða hærri en 10". Annars svarar forritið "Vel gert!".

spurning = int(input("veldu tölu sem er lægri en 0 eða hærri en 10:"))#hér er beðið um töluna
if 0 <= spurning <= 10:
    print("þessi tala er ekki á minni en 0 eða hærri en 10")#útkoma ef tala er ekki á minni en 0 eða hærri en 10
else:
    print ("vel gert")#útkoma ef tala er minni en 0 eða hærri en 10 
    

# Lidur 10: Nöfn
#Forrit biður um nöfn tveggja einstaklinga.
#Forritið finnur síðan út hvort nöfnin eru eins eða ekki og skrifar viðeigandi skilaboð á skjáinn. Hafðu
#úttak forrits líkt og dæmin hér fyrir neðan sýna.
Dæmi:
#Sláðu inn nafn 1: Jón
#Sláðu inn nafn 2: Jóna
#Jón og Jóna eru ekki sömu nöfnin.
#Annað dæmi:
#Sláðu inn nafn 1: Birna
#sláðu inn nafn 2: Birna
#Birna og Birna er sama nafnið.

n1 = input("sláðu in nafn1:")#hér er spyrt um nafn1
n2 = input("sláðu in nafn2:")#hér er spyrt um nafn2
if n1 == n2:
    print(f"{n1} og {n2} eru sömu nöfn")# hér er útkoman ef nöfnin eru eins
else: print(f"{n1} og {n2} eru ekki sömu nöfn")# hér er útkoman ef nöfnin eru ekki eins
