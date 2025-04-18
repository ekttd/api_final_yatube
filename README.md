# api_final
api final

## Описание
Yatube API — это API-интерфейс для социальной сети Yatube, в которой пользователи могут публиковать посты, комментировать, подписываться друг на друга и взаимодействовать с контентом.

## Установка
1. Клонирование репозитория
`git clone https://github.com/ekttd/api_final_yatube.git`

2. Создание и активация виртуального окружения
`python -m venv venv
venv\Scripts\activate`

3. Установка зависимостей
`pip install -r requirements.txt`

4. Миграции
`python manage.py migrate`

5. Запуск сервера
`python manage.py runserver`

## Примеры запросов к API
1. Создание поста
<pre> POST /api/v1/posts/ 
  { 
    "text": "Новый пост", 
    "group": 1 
  }  </pre>
2. Подписка на пользователя
<pre>POST /api/v1/follow/

{
  "following": "username"
}</pre>
3. Получение комментариев к посту
<pre>GET /api/v1/posts/{post_id}/comments/</pre>
4. Поиск по подпискам
<pre>GET /api/v1/follow/?search=username</pre>
