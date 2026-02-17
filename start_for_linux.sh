#!/bin/bash

# 加载环境变量配置（如果存在）
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# 默认不启用异步服务
ENABLE_ASYNC_SERVICES=${ENABLE_ASYNC_SERVICES:-false}
REDIS_SERVER_URL=${REDIS_SERVER_URL:-127.0.0.1}
DJANGO_RUNSERVER_HOST=${DJANGO_RUNSERVER_HOST:-0.0.0.0}
DJANGO_RUNSERVER_PORT=${DJANGO_RUNSERVER_PORT:-8080}

# 检测操作系统
if [[ "$(uname)" == "Darwin" ]] || [[ "$(expr substr $(uname -s) 1 5)" == "Linux" ]]; then
    # Linux 或 macOS
    echo "Starting Django server..."

    # 根据配置决定是否启动异步服务
    if [ "$ENABLE_ASYNC_SERVICES" = "true" ]; then
        echo "Async services enabled. Starting Redis and Celery..."

        # 启动 Redis
        nohup Redis/redis-server &
        # 等待 Redis 启动完成
        sleep 5

        # 启动 Celery worker
        nohup celery -A MainConfig worker -l info -P threads &
        # 等待 Celery 启动完成
        sleep 5
    else
        echo "Async services disabled. Starting Django only..."
        echo "To enable async services, set ENABLE_ASYNC_SERVICES=true in .env file"
    fi

    # 启动 Django 开发服务器
    python manage.py runserver $DJANGO_RUNSERVER_HOST:$DJANGO_RUNSERVER_PORT

else
    echo "Unsupported operating system."
    exit 1
fi