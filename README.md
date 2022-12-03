<div align="center">
<a href="https://github.com/ID-Start-Winter22/team2-banifli">
<img src="http://banifli.de/images/bannerneu.jpg" alt="Logo" width="100%" height="auto">
</a>

<h3 align="center">SafeSurf Chatbot</h3>

<p align="center">
Dein Begleiter für einen sicheren Internetumgang.
<br />
<a href="https://github.com/ID-Start-Winter22/team2-banifli/wiki"><strong>Erforsche das Wiki »</strong></a>
<br />
·
<a href="https://github.com/ID-Start-Winter22/team2-banifli/issues">Fehler melden</a>
</p>
</div>

<details>
<summary>Inhaltsverzeichnis</summary>
<ol>
<li>
<a href="#über">Über das Projekt</a>
</li>
<li>
<a href="#installation">Installation</a>
</li>
<li><a href="#nutzung">Nutzung</a></li>
<li><a href="#roadmap">Roadmap</a></li>
<li><a href="#kontakt">Kontakt</a></li>
<li><a href="#danksagungen">Danksagungen</a></li>
</ol>
</details>




## Über
Wir haben den Bot für Menschen entwickelt, die ihren sicheren Umgang in der digitalen Welt auf bekannte Schwachstellen Prüfen und verbessern wollen. 🌐 Der Bot führt gemeinsam mit dem User eine Checkliste 📝 durch und gibt diesem am Ende einen Score und Verbesserungsvorschläge. 🔒


## Vorraussetzungen

Um den Bot zu deployen, werden folgende Packete benötigt:

* Rasa

  ```
  https://github.com/michaeleggers/RasaIntro
  ```
* Python

  ```
  Python Version 3.9.13
  ```

## Installation

1. Clone the repo

   ```
   git clone https://github.com/ID-Start-Winter22/team2-SafeSurf.git
   cd team2-SafeSurf
   ```
2. Install pip packages

   ```
   pip install requests
   pip install json
   pip install hibpwned
   ```
3. Rasa starten
   
   ```
   conda activate rasaenv
   rasa train
   rasa run actions
   ```

5. Server Starten
   In einem zweiten Terminal
   ```
   python -m http.server
   rasa shell 
   ```
   In einem Browser http://localhost:8000/



<p align="right">(<a href="#über-das-projekt">Zurück nach oben</a>)</p>

## Nutzung

*Anwendungsbeispiele findet man in der Dokumentation.  [Dokumentation](https://github.com/ID-Start-Winter22/team2-banifli/wiki)*

<p align="right">(<a href="#über-das-projekt">Zurück nach oben</a>)</p>

<!-- ROADMAP -->

## Roadmap


Siehe [offene Issues](https://github.com/ID-Start-Winter22/team2-banifli/issues) für alle Zukünftigen Features und bekannte Fehler.

<p align="right">(<a href="#über-das-projekt">Zurück nach oben</a>)</p>

## Konakt

Schickt uns gerne eine Mail an:

wiest@hm.edu | 
basse@hm.edu |
lvock@hm.edu |
duske@hm.edu |


Project Link: <https://github.com/ID-Start-Winter22/team2-banifli/>

<p align="right">(<a href="#über-das-projekt">Zurück nach oben</a>)</p>

## Entwickelt mit

* [Python](https://www.python.org/)
* [Rasa](https://rasa.com/)


## Danksagungen

* [gsocher](https://github.com/gsocher)
* [michaeleggers](https://github.com/michaeleggers)
* [haveIbeenPwnd](https://haveibeenpwned.com/)

<p align="right">(<a href="#über-das-projekt">Zurück nach oben</a>)</p>
 
