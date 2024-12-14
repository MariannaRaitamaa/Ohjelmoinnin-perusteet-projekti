# Ladataan pääpäiväkirjan sisältö
with open("paivakirja.txt") as tiedosto:
    paivakirjateksti = [rivi.replace("\n", "") for rivi in tiedosto]
 
# Ladataan ystäväsivun sisältö
with open("ystavasivu.txt") as tiedosto:
    ystavasivuteksti = [rivi.replace("\n", "") for rivi in tiedosto]

with open("osoitekirja.txt") as tiedosto:
    osoitekirjatiedot = [rivi.replace("\n", "") for rivi in tiedosto]

paivakirjateksti = []
ystavasivuteksti = [] 
osoitekirjatiedot = []
lista = []
rivit = []
# Avataan molemmat tiedostot lisäystä varten
while True:
    print("1 - Päiväkirja, 2 - Ystäväsivu, 3 - Osoitekirja, 4 - Lopeta")
    toiminto = input("Valitse toiminto: ")
    if toiminto == "1":  # Päiväkirja
        with open("paivakirja.txt", "a+") as tiedosto:
            tiedosto.seek(0)
            for rivi in tiedosto:
                paivakirjateksti.append(rivi.strip())  # Merkinnät listaan
            
            while True:
                print("1 - Lisää teksti, 2 - Hae merkintä, 3 - Alkuun")
                toiminto2 = input("Valitse toiminto: ")
                
                if toiminto2 == "1":
                    paiva = input("Kirjoita päivämäärä (YYYY-MM-DD): ")
                    teksti = input("Kirjoita teksti: ")
                    merkinta = paiva + ": " + teksti
                    tiedosto.write(teksti + "\n")
                    paivakirjateksti.append(merkinta)
                    print("Teksti tallennettu")
                
                elif toiminto2 == "2":
                    paivamaara = input("Kirjoita päivämäärä (YYYY-MM-DD): ")
                    hakutulos = [merkinta for merkinta in paivakirjateksti if merkinta.startswith(paivamaara)]
                    
                    if hakutulos:
                        print("Päiväkirjan teksti:")
                        for merkinta in hakutulos:
                            print(merkinta)

                    else:
                        print("Päivämäärällä ei löytynyt merkintöjä.")
                
                elif toiminto2 == "3":
                    break

                else:
                    print("Virheellinen valinta, syötä 1, 2 tai 3.")

    elif toiminto == "2":  # Ystäväsivu
        with open("ystavasivu.txt", "a+") as tiedosto:
            tiedosto.seek(0)
            for rivi in tiedosto:
                ystavasivuteksti.append(rivi.strip())  # Merkinnät listaan
            while True:
                print("1 - Lisää ystävä, 2 - Hae merkintä, 3 - Alkuun")
                toiminto2 = input("Valitse toiminto: ")
                if toiminto2 == "1":
                    nimi = input("Nimi: ")
                    syntymavuosi = int(input("Syntymävuosi: "))
                    harrastukset = input("Harrastukset: ")
                    lempivari = input("Lempiväri: ")
                    lempiruoka = input("Lempiruoka: ")
                    ammatti = input("Ammatti: ")
                    tapaaminen = input("Kerro missä olette tavanneet:")
                    terveiset = input("Kirjoita terveiset: ")

                    merkinta = (nimi + "\n" + str(syntymavuosi) + "\n" + harrastukset + "\n" + lempivari + "\n" + lempiruoka + "\n" + ammatti + "\n" + tapaaminen + "\n" + terveiset + "\n")
                    tiedosto.write(merkinta + "\n")
                    ystavasivuteksti.append(merkinta.strip())

                    print("Ystävän tiedot tallennettu")

                elif toiminto2 == "2":
                    nimi = input("Nimi: ")
                    hakutulos = [merkinta for merkinta in ystavasivuteksti if merkinta.startswith(nimi)]
                    
                    if hakutulos:
                        print("Ystäväsivun tiedot:")
                        print("Nimi: " + nimi + "\n" + "Syntymävuosi: " + str(syntymavuosi) + "\n" + "Harrastukset: " + harrastukset + "\n" + "Lempiväri: " + lempivari + "\n" + "Lempiruoka: " + lempiruoka + "\n" + "Ammatti: " + ammatti + "\n" + "Missä olette tavanneet: " + tapaaminen + "\n" + "Terveisiä ystävälle: " + terveiset)

                    else:
                        print("Tällä nimellä ei löytynyt ystävää.")

                elif toiminto2 == "3":
                    break

                else:
                    print("Virheellinen valinta, syötä 1, 2, tai 3.")

    elif toiminto == "3":  # Osoitekirja
        with open("osoitekirja.txt", "a+") as tiedosto:
            tiedosto.seek(0)
            for rivi in tiedosto:
                if rivi.strip():
                    osoitekirjatiedot.append(rivi.strip())  # Merkinnät listaan
            
        while True:
            print("1 - Lisää osoitetiedot, 2 - Hae osoitetiedot, 3 - Alkuun")
            toiminto2 = input("Valitse toiminto: ")

            if toiminto2 == "1":
                etunimi = input("Etunimi: ")
                sukunimi = input("Sukunimi: ")
                kadun_nimi = input("Osoite: ")
                talon_numero = int(input("Talon numero: "))
                postinumero = int(input("Postinumero: "))
                paikkakunta = input("Paikkakunta: ")
                puh = int(input("Puhelinnumero: "))

                merkinta = f"{etunimi}\n{sukunimi}\n{kadun_nimi}\n{talon_numero}\n{postinumero}\n{paikkakunta}\n{puh}\n"f"{etunimi}\n{sukunimi}\n{kadun_nimi}\n{talon_numero}\n{postinumero}\n{paikkakunta}\n{puh}\n"
                
                with open("osoitekirja.txt", "a+") as tiedosto:
                    tiedosto.write(merkinta + "\n")
                    osoitekirjatiedot.append(merkinta.strip())

                print("Osoitetiedot tallennettu")

            elif toiminto2 == "2":
                etunimi = input("Etunimi: ")
                hakutulos = [merkinta for merkinta in osoitekirjatiedot if merkinta.startswith(etunimi)]
                    
                if hakutulos:
                    print("Osoitetiedot:")
                    for merkinta in hakutulos:
                        rivit = merkinta.split("\n")

                        if len(rivit) == 7:
                            print("Etunimi: " + rivit[0])
                            print("Sukunimi: " + rivit[1])
                            print("Osoite: " + rivit[2])
                            print("Talon numero: " + rivit[3])
                            print("Postinumero: " + rivit[4])
                            print("Paikkakunta: " + rivit[5])
                            print("Puhelinnumero: " + rivit[6])

                else:
                    print("Tällä nimellä ei löytynyt tietoja.")

            elif toiminto2 == "3":
                break

            else:
                print("Virheellinen valinta, syötä 1, 2, tai 3.")
 
    elif toiminto == "4":
        print("Näkemiin, toivottavasti nähdään huomenna!")
        break

    else:
        print("Virheellinen valinta, syötä 1, 2, 3 tai 4.")