# Elections_Scraper

ÚKOL PROGRAMU:
Program stahuje výsledky voleb pro vybrané území (okres) a ukládá je do csv souboru.

INSTALACE:
Nejdříve je potřeba si naistalovat virtuální prostředí. Všechny balíčky, které jsou k tomu potřeba najdete v přiloženém dokumentu requirements.txt

Zcela zásadní budou pro vaši práci knihovny requests a BeautifulSoap. Naistalujete je pomocí příkazu pip install requests a pip install beautifulsoup4.

SPOUŠTĚNÍ SCRIPTU: 

Pro spuštění skriptu jsou nutné dva argumenty. Jedná se o odkaz na webovou stránku (https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103), druhým je pak jméno výstupního souboru s daty (vysledky_prostejov.csv), bez toho nebude program fungovat.

Vzor spuštění: python projekt_3.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103' vysledky_prostejov.csv



