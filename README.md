# BuchCrawler
Amazon Rang von Büchern auslesen und verarbeiten:

Url des Buchs wird benötigt.
Der Rang wird dann ausgegeben.
Aktuell ist geplant dass die Liste der Bücher via CSV eingelesen wird und dann als HTML Datei per Email versendet wird.

Geplante:
x Einlesen von CSV für die Links
x Einlesen des Titels von der Seite / aus der CSV
x Schreiben in CSV des Rangs
- CSV/JSON mit Historie ?!
- Versand via Email getimed einmal im Monat/Woche

Öffnen der via :
python Einlesen.py IMPORT.csv

In der Import.csv sollten folgende Inforamtionen enthalten sein:
Titel, Link

Titel des Buches, Link zur Amazonseite


Es erfolgt eine Ausgabe als CSV und HTML und kurze Rückmeldung im Terminal wenn der Prozess fertig ist.
