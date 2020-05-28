# Readme (DE)
Dieses Dokument beinhaltet einen Setup-Guide sowie eine grundsätzliche Erklärung zu Funktionen, Einstellungen und allgemeinen Zustand der Anwendung.

## Modulinfo
- Programmiert unter Python 3.7.6
- Django & Django Restframework
- Sendgrid
- Env File

## Setupguide
1. Downloads eine gültige Version von [Python](https://www.python.org). Die Anwendung wurde unter [Python 3.7.6](https://www.python.org/downloads/release/python-376/) - Abwärts sowie Aufwärtskompatibilität wurde nicht getestet.

2. Installiere [Virtualenv](https://virtualenv.pypa.io/en/latest/index.html). Ein Setupguide hierzu findest du bei den [Docs](https://virtualenv.pypa.io/en/latest/installation.html)

3. Öffne den Projektordner in deinem Terminal.

4. Erstelle im Projektverzeichnis eine Virtuelle Entwicklungsumgebung (beachte Systemspezifische Unterschiede):

**Windows**
```
python -m venv venv
```
**Ubuntu / Mac**
```
python3 -m venv venv
```

5. Starte die Virtuelle Entwicklungsumgebung (beachte Systemspezifische Unterschiede)

**Windows**
```
venv\Scripts\activate.bat
```
**Ubuntu / Mac**
```
source venv/bin/activate
```

6. Update pip
```
pip install --update pip
``` 

7. Install Packages
```
pip install -r requirements.txt
```
8. erzeuge die .env file:
```
cp .env.example .env
```

9. Migriere das Datenbankschema
```
python manage.py makemigrations
python manage.py migrate
```
10. Erstelle einen Superuser
```
python manage.py createsuperuser
``` 
11. Starte den Server
```
python manage.py runserver
```

Wenn bis hier hin alles klappt, hast du den Server erfolgreich aufgesetzt.

## Zusätzliches Setup
### Sendgrid
Diese Anwendung nutzt in der aktuellen Version die API von [Sendgrid](https://sendgrid.com). Für einen vollen Funktionsumfang der Anwendung benötigst du in der aktuellen Version einen gültigen Account. Der Service von Sendgrid ist mit 100 Emails pro Tag kostenfrei. Weitere Emails kosten Geld.

### .env
Im Root-Verzeichnis dieser Anwendung sollte bei erfolgreichem Setup durch Punkt 8 eine .env File erzeugt werden. Dort sollten einige Eigenschaften angepasst werden.
*Solltest du eine Änderung an der Datei vornehmen, musst du den Server neu starten. Die Änderungen werden nicht im Laufenden Prozess übernommen.*

#### Secret Key - SECRET_KEY
Es ist ein Secret Key eingetragen. Ich empfehle dringend diesen neu zu generieren.

#### Cookie - Expire [SESSION_COOKIE_VALIDATION_TIME]
Gibt die Gültigkeitsdauer des Sessioncookies in Minuten an. Du kannst diese Zahl beliebig verändern.

#### Email-Access Pathes
Es gibt Zugänge via Accountaktivierung, Passwort Reset und Außenzugang. Für die Funktionalität der Django Anwendung sind die Pfade unerheblich. Sie werden einfach als Email mit verschickt, nehmen aber keine weitere interne Funktion ein.

#### Außenzugang - Expires
Mit den Variablen `ACTIVATION_KEY_PERIODS_OF_VALIDITY, PW_FORGOTTEN_KEY_PERIODS_OF_VALIDITY, ACCES_KEY_PERIODS_OF_VALIDITY` gibt man die Gültigkeitsdauer eines Außenzugangs ein. Die default Zeichenkettenlänge beträgt 6 Zeichen. Ich empfehle daher keine zu lange Gültigkeit für die Außenzugänge.

#### Mails Senden [SEND_MAIL]
Für die Entwicklung empfehle ich diese Variable nach der ersten Testphase auf False zu setzen. Um die 100 Frei-Emails nicht auszureizen oder das eigene Postfach zu schonen ist das verschicken der Mail selbst optional. An der Stelle empfehle ich es einmal zu testen und anschließend auf False zu setzen.

#### Empfänger-Mail [TEST_RECEIVER_MAIL]
Wenn `Debug = True` und `SEND_MAIL = True`, dann werden Mails verschickt. Die `TEST_RECEIVER_MAIL` ist der Default Empfänger der Email für die Testphase. So kannst du willkürliche Emails aussuchen, bekommst die Mail aber immer sicher an das eigene Postfach um keine fremden Personen zu schreiben

#### SENDGRID_API_KEY
Nachdem du dich bei Sendgrid registriert hast, bekommst du einen API Key. Diesen trägst du hier ein. Ohne den Key können keine Mails verschickt werden

#### SENDER_MAIL
Gibt die standard Absendemail-Adresse an die ein Empfänger der Email sieht.
