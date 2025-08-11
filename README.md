1. Клонировать репозиторий 
```bash
git clone https://github.com/vinterbris/qaguru_python_advanced_5_intro.git
```
2. В терминале в директории проекта создать и активировать виртуальное окружение
```bash
python -m venv .venv 
source .venv/bin/activate 
```
3. Установить зависимости
```bash
pip install -r requirements.txt 
```
4. Переименовать .env.sample в .env

5. Запустить api микросервис
```bash
uvicorn app.main:app --reload
```
6Запустить тесты командой
```bash
pytest
```