1. Клонировать репозиторий 
```bash
git clone https://github.com/vinterbris/qaguru_python_advanced_5_intro.git
```
2. В терминале в директории проекта создать и активировать виртуальное окружение poetry
```bash
poetry env use 3.10 
source .venv/bin/activate
```
3. Установить зависимости
```bash
poetry install
```
4. Переименовать .env.sample в .env

5. Запустить api микросервис
```bash
poetry run python -m app.main
```
6. Запустить БД в докере
```bash
docker compose up -d
```
7. Запустить тесты командой
```bash
pytest
```