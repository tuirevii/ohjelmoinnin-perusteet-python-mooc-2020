# Exercise Kurssien tilastot (osa07-13_kurssistatistiikka)
Please note that only the code in the .py-file in the src folder is mine. All the other files and codes are part of the course material.

## Assignment / About the program (in Finnish)
Content copied from the course material https://python-s20.mooc.fi/osa-7/4-datan-kasittely#programming-exercise-kurssien-tilastot

### OSA 1: Tieto kursseista

Osoitteesta https://studies.cs.helsinki.fi/stats-mock/api/courses löytyy JSON-muodossa muutaman laitoksen verkkokurssin perustiedot.

Tee funktio `hae_kaikki()` joka hakee ja palauttaa kaikkien menossa olevien kurssien (kentän enabled arvona `True`) tiedot listana tupleja. Paluuarvon muoto on seuraava:

Esimerkkitulostus

    [
        ('Full Stack Open 2020', 'ofs2019', 2020, 201),
        ('DevOps with Docker 2019', 'docker2019', 2019, 36),
        ('DevOps with Docker 2020', 'docker2020', 2020, 36),
        ('Beta DevOps with Kubernetes', 'beta-dwk-20', 2020, 28)
    ]

Jokainen tuple siis sisältää seuraavat arvot:
* kurssin koko nimi (`fullName`)
* nimi (`name`)
* vuosi (`year`)
* harjoitusten (`exercises`) yhteenlaskettu määrä

**Huom:** Tämän tehtävän testien toimivuuden osalta on oleellista, että haet tiedot funktiolla urllib.request.urlopen.

**Huom2:** Testeissä käytetään myös ovelaa kikkaa, joka hieman muuttaa internetistä tulevaa dataa ja tämän avulla varmistaa, että et huijaa tehtävässäsi palauttamalla "kovakoodattua" dataa.

**Huom3:** Jotkut Mac-käyttäjät ovat törmänneet tehtävässä seuraavaan ongelmaan:

    File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/urllib/request.py", line 1353, in do_open
        raise URLError(err)
    urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1124)>

Ongelman ratkaisutapa riippuu siitä miten python on asennettu koneellesi. Joissain tapauksissa toimii seuraava:

    cd "/Applications/Python 3.8/"
    sudo "./Install Certificates.command

Huomaa, että cd-komennon polku riippuu käyttämästäsi Pythonin versiosta. Se voi olla myös `"/Applications/Python 3.8/"`.

Täällä on ehdotettu useita erilaisia ratkaisuja ongelmaan.

Eräs kikka jota voit kokeilla, on seuraava:

    import urllib.request
    import json
    import ssl # lisää tämä kirjasto importeihin

    def hae_kaikki():
        # ja tämä rivi funktioiden alkuun
        context = ssl._create_unverified_context()
        # muu koodi

Toinen tapa kiertää ongelma on seuraava:

    import urllib.request
    import certifi # lisää tämä kirjasto importeihin
    import json

    def hae_kaikki():
       osoite = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
       # lisätään kutsuun toinen parametri
       pyynto = urllib.request.urlopen(osoite, cafile=certifi.where())
       # muu koodi

### OSA 2: Yhden kurssin tiedot

Kunkin kurssin JSON-muotoinen tehtävästatistiikka löytyy omasta osoitteesta, joka saadaan vaihtamalla kurssin kenttä `name` seuraavassa tähtien paikalle https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats

Esimerkiksi kurssin `docker2019` tiedot ovat osoitteessa https://studies.cs.helsinki.fi/stats-mock/api/courses/docker2019/stats

Tee ohjelmaasi funktio `hae_kurssi(kurssi: str)`, joka palauttaa kurssin tarkemman tehtävästatistiikan.

Kun kutsutaan `hae_kurssi("docker2019")`, funktio palauttaa sanakirjan, jonka sisältö on seuraava:
Esimerkkitulostus

    {
        'viikkoja': 4,
        'opiskelijoita': 220,
        'tunteja': 5966,
        'tunteja_keskimaarin': 27,
        'tehtavia': 4988,
        'tehtavia_keskimaarin': 22
    }

Sanakirjaan tallennetut arvot määrittyvät seuraavasti:

* `viikkoja`: kurssia vastaavan JSON-olioiden määrä
* `opiskelijoita`: viikkojen opiskelijamäärien maksimi
* `tunteja`: kakkien viikkojen tuntimäärien (hour_total) summa
* `tunteja_keskimaarin`: edellinen jaettuna opiskelijamäärällä (kokonaislukuna pyöristettynä alaspäin)
* `tehtavia`: kakkien viikkojen tehtävämäärien (exercise_total) summa
* `tehtavia_keskimaarin`: edellinen jaettuna opiskelijamäärällä (kokonaislukuna pyöristettynä alaspäin)

**Huom:** Samat huomiot pätevät tähän osaan kuin edelliseen!

**Huom2:** löydät `math`-moduulista funktion, jonka avulla kokonaisluvun alaspäin pyöristäminen on helppoa
