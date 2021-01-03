# KURSSIEN TILASTOT:

# OSA 1: tieto kursseista

# Osoitteesta https://studies.cs.helsinki.fi/stats-mock/api/courses löytyy JSON-muodossa muutaman 
# laitoksen verkkokurssin perustiedot. Tee funktio hae_kaikki() joka hakee ja palauttaa kaikkien 
# menossa olevien kurssien (kentän enabled arvona True) tiedot listana tupleja. Paluuarvon muoto on seuraava:

#[
#    ('Full Stack Open 2020', 'ofs2019', 2020, 201),
#    ('DevOps with Docker 2019', 'docker2019', 2019, 36),
#    ('DevOps with Docker 2020', 'docker2020', 2020, 36),
#    ('Beta DevOps with Kubernetes', 'beta-dwk-20', 2020, 28)
#]

# Jokainen tuple siis sisältää seuraavat arvot:

#    kurssin koko nimi (fullName)
#    nimi (name)
#    vuosi (year)
#    harjoitusten (exercises) yhteenlaskettu määrä

def hae_kaikki():
    import urllib.request
    import json 

    pyynto = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    pyynto = pyynto.read()
    data = json.loads(pyynto)

    lista = []
    
    for i in data:
        summa = 0
        for maara in i["exercises"]:
            summa += maara
        if i["enabled"] == True:
            koko_nimi = i["fullName"]
            nimi = (i["name"])
            vuosi = i["year"]
            lista.append((koko_nimi, nimi, vuosi, summa))

    return lista

# OSA 2: yhden kurssin tiedot

# Kunkin kurssin JSON-muotoinen tehtävästatistiikka löytyy omasta osoitteesta, joka saadaan 
# vaihtamalla kurssin kenttä name seuraavassa tähtien paikalle 
# https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats

# Esimerkiksi kurssin docker2019 tiedot ovat osoitteessa 
# https://studies.cs.helsinki.fi/stats-mock/api/courses/docker2019/stats

# Tee ohjelmaasi funktio hae_kurssi(kurssi: str), joka palauttaa kurssin tarkemman tehtävästatistiikan.
# Kun kutsutaan hae_kurssi("docker2019"), funktio palauttaa sanakirjan, jonka sisältö on seuraava:

#{
#    'viikkoja': 4,
#    'opiskelijoita': 220,
#    'tunteja': 5966,
#    'tunteja_keskimaarin': 27,
#    'tehtavia': 4988,
#    'tehtavia_keskimaarin': 22
#}

# Sanakirjaan tallennetut arvot määrittyvät seuraavasti:

#    viikkoja: kurssia vastaavan JSON-olioiden määrä
#    opiskelijoita: viikkojen opiskelijamäärien maksimi
#    tunteja: kakkien viikkojen tuntimäärien (hour_total) summa
#    tunteja_keskimaarin: edellinen jaettuna opiskelijamäärällä (kokonaislukuna pyöristettynä alaspäin)
#    tehtavia: kakkien viikkojen tehtävämäärien (exercise_total) summa
#    tehtavia_keskimaarin: edellinen jaettuna opiskelijamäärällä (kokonaislukuna pyöristettynä alaspäin)

# Huom: Samat huomiot pätevät tähän osaan kuin edelliseen!
# Huom2: löydät math -moduulista funktion, jonka avulla kokonaisluvun alaspäin pyöristäminen on helppoa

def hae_kurssi(kurssi: str):
    import urllib.request
    import json 

    pyynto = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{kurssi}/stats")
    pyynto = pyynto.read()
    data = json.loads(pyynto)

    viikkoja = 0 # kurssia vastaavan JSON-olioiden määrä
    opiskelijoita = 0 # viikkojen opiskelijamäärien maksimi
    tunteja = 0 # kaikkien viikkojen tuntimäärien (hour_total) summa
    tehtavia = 0 # kaikkien viikkojen tehtävämäärien (exercise_total) summa
    
    kurssi = {}
    for i in data:
        viikko = data[str(i)]
        tehtavia += viikko["exercise_total"]
        viikkoja += 1
        if viikko["students"] > opiskelijoita:
            opiskelijoita = viikko["students"]
        tunteja += viikko["hour_total"]

    tunteja_keskimaarin = tunteja // opiskelijoita # edellinen jaettuna opiskelijamäärällä (kokonaislukuna pyöristettynä alaspäin)
    tehtavia_keskimaarin = tehtavia // opiskelijoita # edellinen jaettuna opiskelijamäärällä (kokonaislukuna pyöristettynä alaspäin)

    kurssi["viikkoja"] = viikkoja
    kurssi["opiskelijoita"] = opiskelijoita
    kurssi["tunteja"] = tunteja
    kurssi["tunteja_keskimaarin"] = tunteja_keskimaarin
    kurssi["tehtavia"] = tehtavia
    kurssi["tehtavia_keskimaarin"] = tehtavia_keskimaarin
    
    return kurssi


if __name__ == "__main__":
    tulos = hae_kaikki()
    for kurssi in tulos:
        print(kurssi)
    kurssi = hae_kurssi("docker2019")
    print(kurssi)
