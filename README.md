# REST Chess solver

## Aplikację można uruchomić na dwa sposoby:

### 1. Za pomocą Dockera:
* utworzyć nowy folder komendą: `mkdir chess_solver`
* przejść do utworzonego folderu: `cd chess_solver`
* uruchomić komendy: 
  * `git init`
  * `git pull GRZEGORZ_GAŁĄZKA.bundle master`
  * `docker build .` 
  * `docker compose up` 
### 2. "Tradycyjnie" bez dockera:
* utworzyć nowy folder komendą: `mkdir chess_solver`
* przejść do utworzonego folderu: `cd chess_solver`
* uruchomić komendy:
  * `pip install pipenv`
  * `pipenv install`
  * `pipenv shell`
  * `python app.py` lub `python3 app.py`
