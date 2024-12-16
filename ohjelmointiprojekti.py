# Haetaan päiväkirjan sisältö
with open("paivakirja.txt") as tiedosto:
    paivakirjateksti = [rivi.replace("\n", "") for rivi in tiedosto]
 
# Haetaan ystäväsivun sisältö
with open("ystavasivu.txt") as tiedosto:
    ystavasivuteksti = [rivi.replace("\n", "") for rivi in tiedosto]

# Haetaan osoitekirjan sisältö
with open("osoitekirja.txt") as tiedosto:
    osoitekirjatiedot = [rivi.replace("\n", "") for rivi in tiedosto]

# Alustetaan muuttujat
paivakirjateksti = []
ystavasivuteksti = [] 
osoitekirjatiedot = []
lista = []
rivit = []
# Avataan tiedostot lisäystä varten
while True:
    print("1 - Päiväkirja, 2 - Ystäväsivu, 3 - Osoitekirja, 4 - Lopeta") # Valikko
    toiminto = input("Valitse toiminto: ")
    if toiminto == "1":  # Päiväkirja
        with open("paivakirja.txt", "a+") as tiedosto:
            tiedosto.seek(0)
            for rivi in tiedosto:
                paivakirjateksti.append(rivi.strip())  # Lisätään merkinnät listaan
            
            while True:
                print("1 - Lisää teksti, 2 - Hae merkintä, 3 - Alkuun") # Alavalikko
                toiminto2 = input("Valitse toiminto: ")
                
                # Lisätään päiväkirjamerkintä
                if toiminto2 == "1":
                    paiva = input("Kirjoita päivämäärä (YYYY-MM-DD): ")
                    teksti = input("Kirjoita teksti: ")
                    merkinta = paiva + ": " + teksti
                    tiedosto.write(teksti + "\n")
                    paivakirjateksti.append(merkinta)
                    print("Teksti tallennettu")
                
                # Haetaan päiväkirjamerkintä päivämäärän perusteella
                elif toiminto2 == "2":
                    paivamaara = input("Kirjoita päivämäärä (YYYY-MM-DD): ")
                    hakutulos = [merkinta for merkinta in paivakirjateksti if merkinta.startswith(paivamaara)]
                    
                    if hakutulos:
                        print("Päiväkirjan teksti:")
                        for merkinta in hakutulos:
                            print(merkinta)
                    # Jos päivämäärällä ei löytynyt merkintöjä, tulostuu seuraava
                    else:
                        print("Päivämäärällä ei löytynyt merkintöjä.")
                
                elif toiminto2 == "3":
                    break
                # Virheellinen valinta, jos syöttää valikkoon jonkun muun kuin 1, 2 tai 3
                else:
                    print("Virheellinen valinta, syötä 1, 2 tai 3.")

    elif toiminto == "2":  # Ystäväsivu
        with open("ystavasivu.txt", "a+") as tiedosto:
            tiedosto.seek(0)
            for rivi in tiedosto:
                ystavasivuteksti.append(rivi.strip())  # Lisätään merkinnät listaan
            while True:
                print("1 - Lisää ystävä, 2 - Hae merkintä, 3 - Alkuun") # Alavalikko
                toiminto2 = input("Valitse toiminto: ")
                # Lisätään ystävän tiedot
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
                    ystavasivuteksti.append(merkinta.strip()) # Tallennetaan merkintä listaan

                    print("Ystävän tiedot tallennettu")
                # Haetaan ystävän tiedot nimen perusteella
                elif toiminto2 == "2":
                    nimi = input("Nimi: ")
                    hakutulos = [merkinta for merkinta in ystavasivuteksti if merkinta.startswith(nimi)]
                    
                    if hakutulos:
                        print("Ystäväsivun tiedot:")
                        print("Nimi: " + nimi + "\n" + "Syntymävuosi: " + str(syntymavuosi) + "\n" + "Harrastukset: " + harrastukset + "\n" + "Lempiväri: " + lempivari + "\n" + "Lempiruoka: " + lempiruoka + "\n" + "Ammatti: " + ammatti + "\n" + "Missä olette tavanneet: " + tapaaminen + "\n" + "Terveisiä ystävälle: " + terveiset)
                    # Jos nimen perusteella ei löytynyt ystävää, tulostuu
                    else:
                        print("Tällä nimellä ei löytynyt ystävää.")

                elif toiminto2 == "3":
                    break
                # Virheellinen valinta, jos syöttää valikkoon jonkun muun kuin 1, 2 tai 3
                else:
                    print("Virheellinen valinta, syötä 1, 2, tai 3.")

    elif toiminto == "3":  # Osoitekirja
        with open("osoitekirja.txt", "a+") as tiedosto:
            tiedosto.seek(0)
            for rivi in tiedosto:
                if rivi.strip():
                    osoitekirjatiedot.append(rivi.strip())  # Lisätään merkinnät listaan
            
        while True:
            print("1 - Lisää osoitetiedot, 2 - Hae osoitetiedot, 3 - Alkuun")
            toiminto2 = input("Valitse toiminto: ")
            # Lisätään osoitetiedot
            if toiminto2 == "1":
                etunimi = input("Etunimi: ")
                sukunimi = input("Sukunimi: ")
                kadun_nimi = input("Osoite: ")
                talon_numero = int(input("Talon numero: "))
                postinumero = int(input("Postinumero: "))
                paikkakunta = input("Paikkakunta: ")
                puh = int(input("Puhelinnumero: "))
                # Muokataan osoitetiedot listaksi ja tallennetaan tiedostoon
                merkinta = f"{etunimi}\n{sukunimi}\n{kadun_nimi}\n{talon_numero}\n{postinumero}\n{paikkakunta}\n{puh}\n"f"{etunimi}\n{sukunimi}\n{kadun_nimi}\n{talon_numero}\n{postinumero}\n{paikkakunta}\n{puh}\n"
                
                with open("osoitekirja.txt", "a") as tiedosto:
                    tiedosto.write(merkinta)
                    osoitekirjatiedot.append(merkinta.strip()) # Tallennetaan merkinnät

                print("Osoitetiedot tallennettu")
            # Haetaan osoitetiedot etunimen perusteella
            elif toiminto2 == "2":
                etunimi = input("Etunimi: ")
                hakutulos = [merkinta for merkinta in osoitekirjatiedot if merkinta.split('\n')[0] == etunimi]
                    
                if hakutulos:
                    print("Osoitetiedot:")
                    for merkinta in hakutulos:
                        rivit = merkinta.split("\n")
                        # Tulostetaan listana
                        if len(rivit) == 7:
                            print("Etunimi: " + rivit[0])
                            print("Sukunimi: " + rivit[1])
                            print("Osoite: " + rivit[2])
                            print("Talon numero: " + rivit[3])
                            print("Postinumero: " + rivit[4])
                            print("Paikkakunta: " + rivit[5])
                            print("Puhelinnumero: " + rivit[6])
                # Jos etunimellä ei löytynyt tietoja
                else:
                    print("Tällä nimellä ei löytynyt tietoja.")

            elif toiminto2 == "3":
                break
            # Virheellinen valinta, jos syöttää valikkoon jonkun muun kuin 1, 2 tai 3
            else:
                print("Virheellinen valinta, syötä 1, 2, tai 3.")
    # Lopetus
    elif toiminto == "4":
        print("Näkemiin, toivottavasti nähdään huomenna!")
        break
    # Virheellinen valinta, jos syöttää valikkoon jonkun muun kuin 1, 2, 3 tai 4
    else:
        print("Virheellinen valinta, syötä 1, 2, 3 tai 4.")