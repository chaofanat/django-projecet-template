@echo off
    setlocal

    :: 启动 Redis
    start "" Redis/redis-server

    :: 等待 Redis 启动完成
    timeout /t 5 /nobreak

    :: 启动 Celery worker
    start "" celery -A MainConfig worker -l info -P threads

    :: 等待 Celery 启动完成
    timeout /t 5 /nobreak

    :: 启动 Django 开发服务器
    start "django-testserver" python manage.py runserver 0.0.0.0:8080

    endlocal