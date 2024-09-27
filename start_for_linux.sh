#!/bin/bash

# 检测操作系统
if [[ "$(uname)" == "Darwin" ]] || [[ "$(expr substr $(uname -s) 1 5)" == "Linux" ]]; then
    # Linux 或 macOS
    echo "Starting services..."

    # 启动 Redis
    nohup Redis/redis-server &

    # 等待 Redis 启动完成
    sleep 5

    # 启动 Celery worker
    nohup celery -A MainConfig worker -l info -P threads &

    # 等待 Celery 启动完成
    sleep 5

    # 启动 Django 开发服务器
    python manage.py runserver 0.0.0.0:8080

else
    echo "Unsupported operating system."
    exit 1
fi