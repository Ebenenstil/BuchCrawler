from Buchrangsuche import Buchrang
import csv
from HTMLerstellen import htmlausgabe
from pathlib import Path
import sys

url = "https://amzn.to/3krfzQN"
labels=["Titel","Link","Rang"]

datei1 = sys.argv[1]
dateix = datei1[:-4]+"_CSV_Export.csv"


ausgabedatei = Path(dateix)
ausgabedatei.touch(exist_ok=True)

def csvreinraus(eingabe,ausgabe):
    with open(eingabe) as data:
        with open(ausgabe,"w") as data2:
            csvdatei = csv.DictReader(data)
            writer = csv.writer(data2)
            writer.writerow(labels)
            for line in csvdatei:
                line["Rang"]=Buchrang(line["Link"])
                writer.writerow(line.values())
        

csvreinraus(datei1,ausgabedatei)
htmlausgabe(dateix,datei1)
print("Fertig")

