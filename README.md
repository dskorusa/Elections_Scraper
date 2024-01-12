![Ukázka výstupu](https://github.com/dskorusa/Elections_Scraper/assets/143288246/3d8bb6f9-0ab7-4173-9af6-5ab1f0d82728)
# Elections_Scraper

ÚKOL PROGRAMU:
Program stahuje výsledky voleb pro vybrané území (okres) a ukládá je do csv souboru.

INSTALACE:
Nejdříve je potřeba si naistalovat virtuální prostředí. Všechny balíčky, které jsou k tomu potřeba najdete v přiloženém dokumentu requirements.txt

Zcela zásadní budou pro vaši práci knihovny requests a BeautifulSoap. Naistalujete je pomocí příkazu pip install requests a pip install beautifulsoup4.

SPOUŠTĚNÍ SCRIPTU: 

Pro spuštění skriptu jsou nutné dva argumenty. Jedná se o odkaz na webovou stránku (https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103), druhým je pak jméno výstupního souboru s daty (vysledky_prostejov.csv), bez toho nebude program fungovat.

Vzor spuštění: python projekt_3.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103' vysledky_prostejov.csv

Ukázka výstupu:
name,number,url
Alojzov,506761,
Bedihošť,589268,
Bílovice-Lutotín,589276,
Biskupice,589284,
Bohuslavice,589292,
Bousín,589306,
Brodek u Konice,589314,
Brodek u Prostějova,589322,
Březsko,589331,
Budětsko,589349,
Buková,589357,
Čehovice,589365,
Čechy pod Kosířem,589381,
Čelčice,589390,
Čelechovice na Hané,589403,
Dětkovice,589420,
Dobrochov,589438,
Dobromilice,589446,
Doloplazy,589454,
Drahany,589462,
Držovice,558419,
Dřevnovice,589489,
Dzbel,589497,
Hačky,549967,
Hluchov,589501,![image](https://github.com/dskorusa/Elections_Scraper/assets/143288246/f9bd28a6-deae-4866-a066-164aaf35ab07)
