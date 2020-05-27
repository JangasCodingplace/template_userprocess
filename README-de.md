# Readme (DE) - Allgemeine Informationen

Dieses Repository beinhaltet eine Django Rest Anwendung mit einem React Frontend.

Grundsätzlich wird ein funktionsfähiges Authentifikationssystem inklusive gängige Nutzerinteraktionen bereitgestellt. Dieses Template ist eine Komposition aus einigen meiner Snippets.
Ein Emailservice wird mit Sendgrid bereitgestellt. Dieser ist jedoch optional und austauschbar. Langfristig dient dieses Template für ein möglichst schnelles Prototyping bei dem man den Fokus auf die individuellen Problemstellungen legen kann.

## Setup
Die Anwendung ist strikt getrennt in Frontend (fe) und Backend (be). Als erstes sollte das Backend aufgesetzt werden und anschließend das Frontend. Für die jeweiligen Setups bitte ich die Readmes der einzelnen Ordner zu lesen und zu befolgen.

## Funktionalität
### Login
- Der Nutzer hat die Möglichkeit sich mit seiner Email und seinem Passwort auf die Plattform einzuloggen
- Bei einem Login bekommt der Nutzer eine Infomail

### Registrierung
- Der Nutzer registriert sich durch Eingabe von Vorname, Nachname, Email und Passwort. Auch mit den AGB muss er sich einverstanden erklären.
- Nach der Registrierung wird ein Aktivierungslink verschickt
- Der Account wird aktiviert, sobald der Nutzer auf den Link klickt

### Passwort vergessen
- durch Eingabe einer Email wird eine Mail verschickt. Diese leitet den Nutzer weiter auf eine Passwort neu erstellen Seite.
- Existiert ein Account nicht, so wird keine Email geschickt. Der Nutzer bekommt Frontendseitig kein invalides Feedback

### Profil bearbeiten
- Der Nutzer hat die Möglichkeit seine angegebenen Daten (Vorname und Nachname, Email und Passwort) zu bearbeiten
- Zur Änderung der Email oder des Passworts muss das aktuell gültige Passwort eingegeben werden
- Wird die Email des Nutzers geändert, wird der Nutzer automatisch per Email an seine alte Emailadresse benachrichtigt

### Authentifizierung (allgemeine Info)
Die Standard Authentifizierung ist die SessionAuthentification. Im Browser des Nutzers wird ein HTTP Cookie gelegt. Die Gültigkeit des Cookies kann man editieren. Zusätzlich muss ein Token mitgeschickt werden. Auch dieser liegt als Cookie im Browser des Nutzers und wird automatisch gesetzt

### Email Links
In den Fällen Passwort vergessen sowie Accountaktivieren wird eine Email mit einem Link zur Seite geschickt. Über diesen Link authentifiziert sich der Nutzer automatisch und wird auf den jeweiligen Bereich weitergeleitet.
Der Link hat eine bestimmte Gültigkeitsdauer die geändert werden kann.

## Info
Das ist ein nicht kommerzielles Projekt!
Es ist in meiner Freizeit entstanden. Auch sind viele Bereiche nicht getestet. Die Testeinheiten werden noch implementiert.
Fehler und Tipps können mir aber gerne gemeldet werden.
