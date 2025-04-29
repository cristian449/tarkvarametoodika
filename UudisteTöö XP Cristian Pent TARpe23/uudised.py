import random
import datetime


uudised = {
    "tehnoloogia": [
        "Eksperdid: keelemudelid kujutavad inimväärilise tehisaru otsingutel tupikut",
        "Nutitelefonide müük langes esmakordselt kümne aasta jooksul.",
        "Andri Haran: uuel kujul on IT-sektor Eestile veelgi väärtuslikum.",
        "Eestis on 5G leviala laienenud 50% võrra."

    ],
    "spordiuudised": [
        "Eesti sportlased Hispaanias ja Portugalis: „Ühed hakkasid gaasipliite kokku ostma, teised jõid rahulikult baaris õlut.",
        "Maailmameister püstitas uue rekordi.",
        "Eesti kurlingupaar sai MMil esimese kaotuse ",
        "Eesti õhuisportlased võitsid Euroopa meistrivõistlustel pronksi.",
        "Eesti suusataja võitis maailmameistrivõistlustel hõbemedali."


    ],
    "majandus": [
        "Euro kurss tõusis dollari suhtes.",
        "Toiduhinnad kasvasid märtsis 4%.",
        "Tööpuudus vähenes rekordiliselt madalale tasemele.",
        "Eesti lõpuks suutis majandused plussi minna 4-jandas kvartalis.",
        "Inflatsioon tõusis 2% võrreldes eelmise aastaga.",
        "Automaks tõused järgmine aasta esimesest jaanuarist suure summa, aga kui auto on vanem kui 10 aastat siis ei pea maksma."
    ],
    "ilm": [
        "Homme on oodata vihma ja tuult.",
        "Sooja tuleb 15 kraadi.",
        "Temperatuur langeb -6 ja lumi tuleb tagasi.",
        "Jargmine nädalavahetus lubab äikesetormi.",
        "Eesti rannikud homme on väga tuulised."
    ],
    "muusika": [
        "Imagine Dragons album müüb hästi.",
        "AJR kontsert Tallnnnas lükati edasi.",
        "Eeesti võtiis Eurovisioni eelvooru.",
        "Eesti tippartist esitas uue laulu.",


    ],
    "poliitika": [
        "Venemaa ja Ukraina rahulepe on lähenemas ja mõlemad pooled on austanud praegust vaherahu.",
        "Eesti valitsus kiitis heaks uue seaduse, mis reguleerib digitaalseid allkirju.",
        "Euroopa Liit kehtestas uued sanktsioonid Venemaa vastu.",
        "Eesti valitsus plaanib suurendada kaitsekulutusi järgmise aasta eelarves."

    ]
    


    
}

def juuslik_kuupäev_viiimase_7_päeva_jooksul():
    täna = datetime.date.today()
    juhuslik_päev = täna - datetime.timedelta(days=random.randint(0, 6))
    return juhuslik_päev.strftime("%d.%m.%Y")

def genereeri_uudised(valik):
    valitud_uudised = random.sample(uudised[valik], k=2)
    genereeritud = []
    for uudis in valitud_uudised:
        kuupäev = juuslik_kuupäev_viiimase_7_päeva_jooksul()
        genereeritud.append(f"{kuupäev}  {uudis}")
    return genereeritud

def kuva_menüü():
    print("1. Tehnoloogia")
    print("2. Spordiuudised")
    print("3. Majandus")
    print("4. Ilm")
    print("5. Muusika")
    print("6. Poliitika")

def kategooria_valik():
    while True:
        kuva_menüü()
        valik = input("Valige palun uudiseed, valige nr 1-5 ")
        if valik == "1":
            return "tehnoloogia"
        elif valik == "2":
            return "spordiuudised"
        elif valik == "3":
            return "majandus"
        elif valik == "4":
            return "ilm"
        elif valik == "5":
            return "muusika"
        elif valik == "6":
            return "poliitika"
        else:
            print("Tekkis viga proovige uuesti number 1-6 palun")

def lisa_uudis(valik):
    uus_uudis = input("Palun sisestage uus uuddis:")
    uudised[valik].append(uus_uudis)
    print("Uudis lisatud tabelisse yay!")

def main():
    while True:
        kategooria = kategooria_valik()
        uudised = genereeri_uudised(kategooria)
        print("\n--- Genereeritud uudised ---")
        for u in uudised:
            print(u)

        tegevus = input("\nKas teie soovite äkki lisada uued uudised (valige kas jah või ei)").lower()
        if tegevus == "jah":
            lisa_uudis(kategooria)

        uuesti = input("Kas soovid uudiseid uuesti genereerida kas (valige kas jah või ei) ").lower()
        if uuesti != "jah":
            break

main()