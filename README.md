# Filmälskaren

Filmälskaren är en webbapplikation som hjälper filmälskare hitta information om filmer. Webbapplikationen är en mashup som använder tre olika APIer för att få information om filmerna, posters, samt trailers.

## Kom igång
Genom att följa instruktionerna nedan kommer applikationen kunna köras lokalt på din dator.

### Installera Python
Python 3.7 används som programmeringsspråk till servern. Följ instruktionerna på https://www.python.org/downloads/ och installera Python till datorn.

Kommande installationer sköts via kommandotolken / terminalen. När ordet “terminal” används framöver menas både Macs terminal och Windows kommandotolk.

### Virtuell miljö
När Python är installerat bör en virtuell miljö för koden skapas inuti projektmappen. Dependencies som Python-programmet använder installeras i den virtuella miljön.

Navigera via terminalen till den mapp projektmappen ska ligga i. Skriv sedan följande kommando:

```
$ mkdir <project-name> (Skapar projektmapp. Skippa detta om en projektmapp redan finns.)
$ cd project-name
```

Mac:
```
$ python3 -m venv <venv-name>
```

Windows:
```
$ py -3 -m venv <venv-name>
```

Aktivera den virtuella miljön med följande kommando:

Mac:
```
$ . venv/bin/activate
```

Windows:
```
venv\Scripts\activate
```

När den virtuella miljön är aktiverad ska dess namn stå inom parenteser längst till vänster i sökvägen i terminalen.

### Installera Flask
Python-ramverket Flask används för att bygga webbservern. Installera Flask i den virtuella miljön. Den virtuella miljön måste vara aktiverad.

```
$ pip install Flask
```

### … Fyll på när vi pippar nya saker

* Christopher
* Martin
* Max
* Tobias
