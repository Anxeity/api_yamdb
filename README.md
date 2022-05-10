# api_yamdb
api_yamdb
Функционал API:
```
1) Просмотр, создание и редактирвание постов.
```
```
2) Просмотр групп.
```
```
3) Просмотр, создание и редактирвание коментариев.
```

```
4) Подписка на пользователей.
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/pkrfc/api_yatube_rest.git
```

```
cd api_yatube_rest
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Документация по API находится по ссылке:
```
http://127.0.0.1:8000/redoc/
доступна после запуска сервера.