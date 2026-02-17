@echo off
setlocal EnableDelayedExpansion

:: 从 .env 文件加载配置（如果存在）
if exist .env (
    for /f "tokens=*" %%a in ('type .env ^| findstr /v "^#"') do (
        set %%a
    )
)

:: 默认配置
if not defined ENABLE_ASYNC_SERVICES set ENABLE_ASYNC_SERVICES=false
if not defined REDIS_SERVER_URL set REDIS_SERVER_URL=127.0.0.1
if not defined DJANGO_RUNSERVER_HOST set DJANGO_RUNSERVER_HOST=0.0.0.0
if not defined DJANGO_RUNSERVER_PORT set DJANGO_RUNSERVER_PORT=8080

echo Starting Django server...

:: 根据配置决定是否启动异步服务
if "!ENABLE_ASYNC_SERVICES!"=="true" (
    echo Async services enabled. Starting Redis and Celery...

    :: 启动 Redis
    start "" Redis/redis-server
    :: 等待 Redis 启动完成
    timeout /t 5 /nobreak

    :: 启动 Celery worker
    start "" celery -A MainConfig worker -l info -P threads
    :: 等待 Celery 启动完成
    timeout /t 5 /nobreak
) else (
    echo Async services disabled. Starting Django only...
    echo To enable async services, set ENABLE_ASYNC_SERVICES=true in .env file
)

:: 启动 Django 开发服务器
start "django-testserver" python manage.py runserver !DJANGO_RUNSERVER_HOST!:!DJANGO_RUNSERVER_PORT!

endlocal