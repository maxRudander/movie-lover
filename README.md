# Filmälskaren

Filmälskaren är en webbapplikation som hjälper filmälskare hitta information om filmer. Webbapplikationen är en mashup som använder tre olika APIer för att få information om filmerna, posters, samt trailers.

## Installation
Följ instruktionerna nedan för att installera de program och beroenden som behövs för att kunna köra applikationen.

### Installera Python
Python 3.7 används som programmeringsspråk till servern. Följ instruktionerna på https://www.python.org/downloads/ och installera Python 3.7.

Kommande installationer sköts via kommandotolken / terminalen. När ordet “terminal” används framöver menas både Macs terminal och Windows kommandotolk.

Skapa en projektmapp och navigera till denna.
```
$ mkdir <project-name> (Skapar projektmapp. Skippa detta om en projektmapp redan finns.)
$ cd project-name
```

### Virtuell miljö
När Python är installerat bör en virtuell miljö för koden skapas i projektmappen. Beroenden som applikationen använder installeras i den virtuella miljön.

**Ubuntu Linux**
Virtuella miljöer är inte förinstallerade i Python som är installerat på Ubuntu Linux. Skriv följande kommando för att installera modulen för virtuella miljöer på din dator:
```
$ sudo apt-get install python3-venv
```

Skapa en virtuell miljö i projektmappen.
**Mac & Linux:**
```
$ python3 -m venv <venv-name>
```

**Windows:**
```
$ py -3 -m venv <venv-name>
```

Aktivera den virtuella miljön med följande kommando:

**Mac & Linux:**
```
$ . venv/bin/activate
```

**Windows:**
```
venv\Scripts\activate
```

När den virtuella miljön är aktiverad ska dess namn stå inom parenteser längst till vänster i sökvägen i terminalen.

### Installera Flask
Python-ramverket Flask används för att bygga webbservern. Installera Flask i den virtuella miljön. Den virtuella miljön måste vara aktiverad.

```
$ pip install Flask
```

### Installera Requests
För att skicka requests till APIer installeras modulen requests.

```
$ pip install requests
```

### Installera BeautifulSoup
För att behandla APIers data som returneras i HTML används biblioteket Beautiful Soup.

```
$ pip install beautifulsoup4
```

### Klona projektets git-repo
För att kunna köra programmet måste källkoden finnas på din dator. Denna hämtas enklast genom att klona projektets git-repo.

Navigera via terminalen till den virtuella miljön och kör sedan följande kommando:

```
git clone https://github.com/maxRudander/movie-lover.git
```

En mapp med namnet **movie-lover** innehållande all kod ska nu finnas i den virtuella miljön.

## Kör applikationen
Navigera via terminalen till den virtuella miljön och skriv följande kommando:

```
cd movie-lover/Topcats
```

Starta servern med följande kommando:

```
python app.py
```

### Använd applikationen i webbläsaren
Öppna valfri webbläsare och ange följande URL: **localhost:5000**.
