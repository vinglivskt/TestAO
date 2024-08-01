# TestAO

## Описание
### Тестовое задание для Агентства Облик.

В проекте используется база данных с тремя таблицами: t_request, t_client, и t_area. Таблицы связаны следующим образом:

t_request(client_id) связывается с t_client(id)
t_request(area_id) связывается с t_area(id)
## Задачи

1. Создать модели для SQLAlchemy:
- Модель для таблицы t_request
- Модель для таблицы t_client
- Модель для таблицы t_area

2. Соединить модели:
- Определить связи (ForeignKey) между таблицами.

3. Написать функцию для фильтрации:
- Фильтрация по fullname_area (из таблицы t_area)
- Фильтрация по fullname_client (из таблицы t_client)

4. Создать одну GET точку для фильтрации:

- Точка должна позволять фильтровать как по fullname_area, так и по fullname_client.
- Должна быть возможность указать один или оба параметра.

## Требования:
- Использовать FastAPI для создания API.
- Использовать SQLAlchemy для работы с базой данных.
- Код должен быть структурирован и хорошо документирован


## Установка
Чтобы запустить проект, выполните следующие шаги:
```
1. git clone https://github.com/vinglivskt/TestAO.git
2. cd TestAO
3. python -m venv venv
4. .\venv\Scripts\activate
5. pip install -r requirements.txt
6. cd app
7. python loading_db.py
8. uvicorn main:app --reload
```
### Проверить можно с помощью адрессной строки, curl или Swagger

## Проверка с помощью адрессной строки

1. Проверка всех запросов:
```
http://127.0.0.1:8000/requests/
```
2. Фильтрация по fullname_area:
```
http://127.0.0.1:8000/requests/?fullname_area=Russia
```
3. Фильтрация по fullname_client:
```
http://127.0.0.1:8000/requests/?fullname_client=Vlad
```
4. Фильтрация по обоим параметрам:
```
http://127.0.0.1:8000/requests/?fullname_area=Russia&fullname_client=Igor
```


## Использование curl для проверки

1. Проверка всех запросов:

```
curl -X GET "http://127.0.0.1:8000/requests/"
```
2. Фильтрация по fullname_area:

```
curl -X GET "http://127.0.0.1:8000/requests/?fullname_area=Russia"
```
3. Фильтрация по fullname_client:

```
curl -X GET "http://127.0.0.1:8000/requests/?fullname_client=Vlad"
```
4. Фильтрация по обоим параметрам:

```
curl -X GET "http://127.0.0.1:8000/requests/?fullname_area=Russia&fullname_client=Igor"

```

## Проверка с помощью Swagger
```
http://127.0.0.1:8000/docs
```
1. request
![request.jpg](img%2Frequest.jpg)
2. fullname_area
![fullname_area.jpg](img%2Ffullname_area.jpg)
3. fullname_client
![fullname_client.jpg](img%2Ffullname_client.jpg)
4. fullname_area and fullname_client
![fullname_area and fullname_client.jpg](img%2Ffullname_area%20and%20fullname_client.jpg)


## Используемые технологии
Этот проект построен с использованием следующих технологий:
- FastAPI
- SQLAlchemy
- SQLite
- GitHub
- Git
