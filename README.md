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
```
pip install -r requirements.txt 
```
4. Запустить api микросервис
```bash
python  reqres_service.py
```
5. Запустить тесты командой
```bash
pytest
```