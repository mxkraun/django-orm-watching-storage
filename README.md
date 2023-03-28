# Пульт охраны банка
Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но вы можете свободно использовать код верстки или посмотреть, как реализованы запросы к БД. 

Пульт охраны – это сайт, который можно подключить к удаленной базе данных с визитами и карточками пропуска сотрудников нашего банка.

## Окружение
### Зависимости
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
```

### Переменные окружения
- ENGINE
- HOST
- PORT
- NAME
- USER
- PASSWORD
- SECRET_KEY=REPLACE_ME
- DEBUG=False
- ALLOWED_HOSTS=['*']

1. Поместите файл `.env` рядом с `manage.py`.
2. `.env` содержит текстовые данные без кавычек.

Например, если вы распечатаете содержимое `.env`, то увидите:

```bash
$ cat .env
ENGINE=django.db.backends.postgresql
HOST=/pg_hba.conf
PORT=1234
NAME=mydatabase
USER=user123
PASSWORD=abcdef123
SECRET_KEY=secretkey
DEBUG=False
ALLOWED_HOSTS=localhost
```

## Запуск
Запуск на Linux(Python 3) или Windows:

```bash
$ python manage.py runserver
```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).