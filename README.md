# Polls


## 1. Запуск локально

### 1.1 Установка pipenv и клонирование репозитория
```shell
sudo pip3 install pipenv
git clone https://github.com/grum261/polls
```

### 1.2 Запуск сервера разработки
```shell
pipenv sync
cd src
# sudo chmod +x manage.py
# or use python manage.py command instead of ./manage.py
./manage.py makemigrations
./manage.py migrate
./manage.py runserver # 127.0.0.1:8000 by default
```

## 2. Документация  API
### 2.1 Авторизация

* Описание:
  *  Авторизация пользователя и получение токена, передающегося в заголовке Authorization
* Метод: POST
* URL: http://127.0.0.1/api/login/
* POST запрос:
  ```shell
  curl -X POST -H "Content-Type: application/json" \
    -d '{"name": "username", "email": "user@example.com"}' \
    http://127.0.0.1/api/login/
  ```
* Ответ:
  ```json
  {"token":  "awwed127kmdksl8hf7f7ey2feyuf"}
  ```
  

### 2.2 Опросы
#### Создать новый опрос
* URL: http://127.0.0.1/api/polls/
* POST:
  ```shell
  curl -X POST -H "Content-Type: application/json" \
      -H "Authorization: tokenfromloginpage" \
      -d '{"title": "asdsaada", "description": "dsadsada", "is_active": true}' \
      http://127.0.0.1/api/polls/
  ```
* Ответ:  
  ```json
  {
    "id": 1,
    "title": "asdsaada",
    "start_date": "2021-02-17",
    "end_date": "2021-02-18",
    "description": "dsadsada",
    "is_active": true
  }
  ```
  
#### Получить список всех опросов
* URL: http://127.0.0.1/api/polls/
* GET запрос:
  ```shell
  curl -i -H "Accept: application/json" \
      -H "Authorization: tokenfromloginpage" \
      -H "Content-Type: application/json" \
      -X GET http://127.0.0.1/api/polls/
  ```
* Ответ:  
  ```json
  [
    {
      "id": 1,
      "title": "asdsaada",
      "start_date": "2021-02-17",
      "end_date": "2021-02-18",
      "description": "dsadsada",
      "is_active": true
    }
  ]
  ```
#### Получить конкреный опрос по ID
* URL: http://127.0.0.1/api/polls/{poll_id}/
* GET запрос:
  ```shell
  curl -i -H "Accept: application/json" \
      -H "Content-Type: application/json" \
      -X GET http://127.0.0.1/api/polls/1/
  ```
* Ответ:
  ```json
  {
    "id": 1,
    "title": "asdsaada",
    "start_date": "2021-02-17",
    "end_date": "2021-02-18",
    "description": "dsadsada",
    "is_active": true
  }
  ```

#### Список всех активных опросов
* Методы: GET
* URL: http://127.0.0.1/api/active/polls/
* GET запрос:
  ```shell
  curl -i -H "Accept: application/json" \
      -H "Content-Type: application/json" \
      -X GET http://127.0.0.1/api/active/polls/
  ```
* Ответ:
  ```json
  [
    {
      "id": 1,
      "title": "asdsaada",
      "start_date": "2021-02-17",
      "end_date": "2021-02-18",
      "description": "dsadsada",
      "is_active": true
    }
  ]
  ```
  
#### Получение опроса по ID
* URL: http://127.0.0.1/api/active/polls/{active_poll_id}/
* GET запрос:
  ```shell
  curl -i -H "Accept: application/json" \
      -H "Content-Type: application/json" \
      -X GET http://127.0.0.1/api/active/polls/1/
  ```
* Ответ:
  ```json
  {
    "id": 1,
    "title": "asdsaada",
    "start_date": "2021-02-17",
    "end_date": "2021-02-18",
    "description": "dsadsada",
    "is_active": true
  }
  ```
  
#### Изменение опроса
* URL: http://127.0.0.1/api/polls/{poll_id}/
* PUT запрос:
  ```shell
  curl -X PUT -H "Content-Type: application/json" \
      -H "Authorization: tokenfromloginpage" \
      -d '{"title": "string", "description": "dsadsada", "is_active": true}' \
      http://127.0.0.1/api/polls/1/
  ```
* Ответ:
  ```json
  {
    "id": 1,
    "title": "string",
    "start_date": "2021-02-17",
    "end_date": "2021-02-18",
    "description": "dsadsada",
    "is_active": true
  }
  ```
  
#### Удаление опроса
* URL: http://127.0.0.1/api/polls/{poll_id}/
* DELETE запрос:
  ```shell
  curl -X -H "Authorization: tokenfromloginpage" DELETE http://127.0.0.1/api/polls/1/
  ```
* Ответ:
  ```shell
  204 No Content
  ```
  
### Вопросы к опросам
#### Получение списка вопросов
* URL: http://127.0.0.1:8000/api/questions/
* GET запрос:
  ```shell
  curl -i -H "Accept: application/json" \
      -H "Content-Type: application/json" \
      -H "Authorization: tokenfromloginpage" \
      -X GET http://127.0.0.1/api/questions/
  ```
* Ответ:
  ```json
  [
    {
      "id": 1,
      "text": "trew",
      "type": "text",
      "poll": 2
    }
  ]
  ```
  
#### Создание вопроса с одним из 3 типов к опросу
* URL: http://127.0.0.1:8000/api/questions/
* POST запрос:
  ```shell
  curl -X POST -H "Content-Type: application/json" \
      -H "Authorization: tokenfromloginpage" \
      -d '{"title": "Текст делового вопросика", "type": "text", "poll": 1}' \
      http://127.0.0.1/api/questions/
  ```
* Ответ:
  ```json
  { 
    "id": 1,
    "title": "Текст делового вопросика",
    "type": "text", 
    "poll": 1
  }
  ```
  
#### Изменение вопроса
* URL: http://127.0.0.1/api/questions/{question_id}/
* PUT запрос:
  ```shell
  curl -X PUT -H "Content-Type: application/json" \
      -H "Authorization: tokenfromloginpage" \
      -d '{"title": "Другой текст делового вопросика", "type": "multiple", "poll": "Название опроса"}' \
      http://127.0.0.1/api/questions/1/
  ```
* Ответ:
  ```json
  { 
    "id": 1,
    "title": "Другой текст делового вопросика",
    "type": "multiple", 
    "poll": 1
  }
  ```
  
#### Удаление вопроса
* URL: http://127.0.0.1/api/questions/{question_id}/
* DELETE запрос:
  ```shell
  curl -X -H "Authorization: tokenfromloginpage" DELETE http://127.0.0.1/api/questions/1/
  ```
* Ответ:
  ```shell
  204 No Content
  ```
  
### Варианты ответов в вопросах с несколькими вариантами ответа
#### Создание варианта
* URL: http://127.0.0.1:8000/api/choices/
* POST запрос:
  ```shell
  curl -X POST -H "Content-Type: application/json" \
      -H "Authorization: tokenfromloginpage" \
      -d '{"text": "Текст варианта ответа на деловой вопросик", "question": "Название вопросика"}' \
      http://127.0.0.1/api/choices/
  ```
* Ответ:
  ```json
  { 
    "id": 1,
    "text": "Текст делового вопросика",
    "question": 1
  }
  ```
  
#### Получение списко вариантов ответа на вопрос
* URL: http://127.0.0.1:8000/api/choices/
* GET запрос:
  ```shell
  curl -i -H "Accept: application/json" \
      -H "Authorization: tokenfromloginpage" \
      -H "Content-Type: application/json" \
      -X GET http://127.0.0.1/api/choices/
  ```
* Ответ:
  ```json
  [
    { 
      "id": 1,
      "text": "Текст делового вопросика",
      "question": 1
    }
  ]
  ```

#### Изменение варианта ответа
* URL: http://127.0.0.1/api/choices/{choice_id}/
* PUT запрос:
  ```shell
  curl -X PUT -H "Content-Type: application/json" \
      -H "Authorization: tokenfromloginpage" \
      -d '{"text": "Другой текст варианта ответа", "question": "Название вопросика"}' \
      http://127.0.0.1/api/choices/1/
  ```
* Ответ:
  ```json
  { 
    "id": 1,
    "text": "Другой текст варианта ответа",
    "question": 1
  }
  ```
  
#### Удаление варианта ответа на вопрос
* URL: http://127.0.0.1/api/choices/{choice_id}/
* DELETE запрос:
  ```shell
  curl -X -H "Authorization: tokenfromloginpage" DELETE http://127.0.0.1/api/choices/1/
  ```
* Ответ:
  ```shell
  204 No Content
  ```
  
### Ответы на вопросы
#### Список ответов на вопрос пользователя, создавшего его
* URL: http://127.0.0.1:8000/api/answers/
* GET запрос:
  ```shell
  curl -i -H "Accept: application/json" \
      -H "Authorization: tokenfromloginpage" \
      -H "Content-Type: application/json" \
      -X GET http://127.0.0.1/api/answers/
  ```
* Ответ:
  ```json
  [
    { 
      "id": 1,
      "text": "Текст делового вопросика",
      "question": 1
    }
  ]
  ```
  
#### Создание ответа на вопрос
* URL: http://127.0.0.1:8000/api/answers/
* POST запрос:
  ```shell
  curl -X POST -H "Content-Type: application/json" \
      -H "Authorization: tokenfromloginpage" \
      -d '{"text_vote": "Текст варианта ответа на деловой вопросик", "question": "Название вопросика"}' \
      http://127.0.0.1/api/answers/
  ```
* Ответ:
  ```json
  { 
    "id": 1,
    "text_vote": "Текст ответа на деловой вопросик",
    "question": 1,
    "poll": 2,
    "user": 1,
    "choice": 2
  }
  ```
  
#### Получение списка ответов на вопросы
* URL: http://127.0.0.1:8000/api/answers/
* GET запрос:
  ```shell
  curl -i -H "Accept: application/json" \
      -H "Authorization: tokenfromloginpage" \
      -H "Content-Type: application/json" \
      -X GET http://127.0.0.1/api/answers/
  ```
* Ответ:
  ```json
  [
    { 
      "id": 1,
      "text_vote": "Текст ответа на деловой вопросик",
      "question": 1,
      "poll": 2,
      "user": 1,
      "choice": 2
    }
  ]
  ```
  
#### Изменение ответа на вопрос
* URL: http://127.0.0.1/api/answers/{answer_id}/
* PUT запрос:
  ```shell
  curl -X PUT -H "Content-Type: application/json" \
      -H "Authorization: tokenfromloginpage" \
      -d '{"text_vote": "Какой-то ответ на деловой вопросик", "question": "Название вопросика"}' \
      http://127.0.0.1/api/answers/1/
  ```
* Ответ:
  ```json
  { 
    "text_vote": "Текст ответа на деловой вопросик",
    "question": 1,
    "poll": 2,
    "user": 1,
    "choice": 2
  }
  ```
  
#### Удаление ответа на вопрос
* URL: http://127.0.0.1/api/answers/{answer_id}/
* DELETE запрос:
  ```shell
  curl -X -H "Authorization: tokenfromloginpage" DELETE http://127.0.0.1/api/answers/1/
  ```
* Ответ:
  ```shell
  204 No Content
  ```