# fastapi
api development

uvicorn app.main:app --reload   # запуск

alembic позволяет контролировать изменения в бд. можно вручную прописать upgrade и downgrade,
также можно и сделать autogenerate и алембик сам пропишет апгрейд и даунгрейд

CORS - middleware который позволяет настроить апи и методы чтобы разрешить другим доменам отправлять нам на сервер
запросы.

pip freeze > requirements.txt (команда создает файл в котором версии используемых пакетов в проекте)

pip install -r requirements.txt (команда устанавливает все версии пакетов указанные в этом файле)

heroku create appname (создает приложение на хероку)
git push heroku main (пишит реп с гита на хероку)

psycopg2 не деплоится на хероку, вместо него надо устанавливать psycopg2-binary  

