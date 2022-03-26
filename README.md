# REST Chess solver

## Opis aplikacji

### 1. API, wspomagające grę w szachy, które wystawia dwa adresy url:

* do wyświetlania wszystkich możliwych ruchów danej figury znajdującej się na wskazanym polu:
  #### [GET] `/api/v1/{chess-figure}/{current-field}`
* do walidacji czy ruch na wskazane pole jest poprawny:
  #### [GET] `/api/v1/{chess-figure}/{current-field}/{dest-field}`

> **WAŻNE**: aplikacja uwzględnia tylko sekwencje poruszania się jednej konkretnej figury, bez sekwencji bicia (zgodnie z zasadami gry)

### 2. Aplikacja wykonana przy użyciu:
* Python 3.8
* Flask
* Chess
* Black
* Flake8
* Pytest

## Aplikację można uruchomić na dwa sposoby:

### 1. Za pomocą Dockera:

* utworzyć nowy folder komendą: `mkdir chess_solver`
* przejść do utworzonego folderu: `cd chess_solver`
* pobrać plik z repozytorium plik `GRZEGORZ_GAŁĄZKA.bundle`
* uruchomić komendy:
    * `git init`
    * `git pull GRZEGORZ_GAŁĄZKA.bundle master`
    * `docker build .`
    * `docker-compose up`

### 2. "Tradycyjnie" bez Dockera:

* utworzyć nowy folder komendą: `mkdir chess_solver`
* przejść do utworzonego folderu: `cd chess_solver`
* pobrać plik z repozytorium plik `GRZEGORZ_GAŁĄZKA.bundle`
* uruchomić komendy:
    * `git init`
    * `git pull GRZEGORZ_GAŁĄZKA.bundle master`
    * `pip install pipenv`
    * `pipenv install`
    * `pipenv shell`
    * `python app.py` lub `python3 app.py`
