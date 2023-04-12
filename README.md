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

Update 12.04.2023:

Nachdem Einlesen der CSV Datei wird aktuell eine neue CSV Datei geschrieben mit den Ergebnissen der Suche. Diese wird dann zum erstellen der HTML Datei verwendet.
Geplant ist der Aufbau eines Dict. in einer JSON Datei. Dort werden folgende Informationen gespeichert {"Titel":"XXX"; "Link": "https://XXX"; {"Datum":"XX.XX.XX"; "Rang":"Xxxx"}}
Dies dient zur einfacheren Verarbeitung im Programm und für eine Ausgabe einer Historie.

Programm soll neu gecodet werden in : function.py (<- Enthält alle Funktionen für die Durchführung des Programms), main.py (<- Führt EIngabe und ausgabe durch)
