<div align="center">
<a href="https://github.com/ID-Start-Winter22/team2-banifli">
<img src="https://wiesty.de/images/uploads/banner.png" alt="Logo" width="100%" height="auto">
</a>

<h3 align="center">Banifli Chatbot</h3>

<p align="center">
Dein alltäglicher Studienbegleitung
<br />
<a href="https://github.com/ID-Start-Winter22/team2-banifli/wiki"><strong>Erforsche das Wiki »</strong></a>
<br />
<br />
·
<a href="https://github.com/ID-Start-Winter22/team2-banifli/issues">Fehler melden</a>
</p>
</div>

<details>
<summary>Inhaltsverzeichnis</summary>
<ol>
<li>
<a href="#über-das-projekt">Über das Projekt</a>
<ul>
<li><a href="#geschrieben-mit">Entwickelt mit</a></li>
</ul>
</li>
<li>
<a href="#erstmalige-installation">Erstmalige Installation</a>
<ul>
<li><a href="#voraussetzungen">Voraussetzungen</a></li>
<li><a href="#installation">Installation</a></li>
</ul>
</li>
<li><a href="#nutzung">Nutzung</a></li>
<li><a href="#roadmap">Roadmap</a></li>
<li><a href="#kontakt">Kontakt</a></li>
<li><a href="#danksagungen">Danksagungen</a></li>
</ol>
</details>

## Über das Projekt

<img width="200" alt="image" src="https://user-images.githubusercontent.com/14870896/197070856-6547d5d8-1ea7-4f84-8ad5-82c4618cb374.png">

<p align="right">(<a href="#über-das-projekt">Zurück nach oben</a>)</p>

### Entwickelt mit

* [Python](https://www.python.org/)
* [Rasa](https://rasa.com/)


<p align="right">(<a href="#über-das-projekt">Zurück nach oben</a>)</p>

## Erstmalige Installation

* [Rasa installieren](https://github.com/michaeleggers/RasaIntro)
* `git clone https://github.com/ID-Start-Winter22/team2-banifli.git`
* `cd team2-banifli`
* `pip install mvg-api`
* `pip install requests`
* `pip install json`
* `conda activate rasaenv`
* `rasa train`
* `rasa run --cors "*"`


in einem zweiten Terminal:

* `python -m http.server`

im Browser http://localhost:8000/


### Vorraussetzungen

Um den Bot zu deployen, werden folgende NPM Packete benötigt:

* npm

  ```
  npm install npm@latest -g
  npm install rasa
  npm install mvg
  
  ```
  * Python

  ```
  Python Version 9.13.3
  ```

### Installation

1. Clone the repo

   ```
   git clone https://github.com/ID-Start-Winter22/team2-banifli/
   ```
2. Install NPM packages

   ```
   npm install rasa
   npm install mvg
   ```
3. API Key von openweather einetzen in Line 16 `action.py`

   ```
   api_key = "API KEY eingeben"
   ```

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


## Danksagungen

* [gsocher](https://github.com/gsocher)
* [michaeleggers](https://github.com/michaeleggers)
* [mvg-api by uberardy](https://pypi.org/user/uberardy/)

<p align="right">(<a href="#über-das-projekt">Zurück nach oben</a>)</p>
