# Linkchecker

Dies ist ein Python-Code zum Überprüfen der URLs, die in DB-Tool eingegeben sind. 

## Prozess

Weil keine andere API-Schnittstelle als die API für Kollektion bekannt ist, werden alle Kollektionen in DB-Tools untersucht. Deshalb sind die Links ebenso untersucht, die in der Erläuterung erwähnt sind.
Die defekten URLs werden in der CSV-File "link_error_log.csv" aufgezeichnet.
(Leider ist es nicht möglich, aus der Kollektion-Daten die einschlägigen Fachbereiche festzustellen.)
Der Überprüfungsprozess wird mit "linkcheck.py" ausgeführt.

Falls der Mail-Server zugegriffen werden könnte, kann man die E-mails auch automatisch versenden (wie "mailVersand.py"). 
Voraussetzungen dafür sind:

1. Authentifizierungsdaten des Mail-Server vorhanden
1. Die Liste der Zuständigen in Form von "linkCheckPerso.csv" vorhanden
1. Link-Fehler müssen irgendwie zu einem Fachbereich zugewiesen werden

Wenn alle Information parat ist, könnte man den ganzen Prozess automatisieren...


Einige defekte URLs verursachen noch Fehler während des Überprüfungsprozesses. 


Nachdem man diese Fehler beseitigt hat, könnte man diesen Code durch [cron](https://de.wikipedia.org/wiki/Cron#:~:text=Der%20Cron%2DDaemon%20dient%20der,Aufgaben%20%E2%80%93%20Cronjobs%20%E2%80%93%20zu%20automatisieren.) automatisch & regelmässig laufen lassen.

## Umgebung & Requirements

* Python == 3.8.6
* beautifulsoup4 == 4.10.0
* pandas == 1.4.1
* requests == 2.27.1


