#!/bin/bash

# 检测操作系统
if [[ "$(uname)" == "Darwin" ]] || [[ "$(expr substr $(uname -s) 1 5)" == "Linux" ]]; then
    # Linux 或 macOS
    echo "Stopping services..."

    # 停止 Django 开发服务器
    pids=$(pgrep -f 'python manage.py runserver')
    if [[ -n "$pids" ]]; then
        echo "Stopping Django server..."
        kill -9 $pids
    fi

    # 停止 Celery worker
    pids=$(pgrep -f 'celery -A MainConfig worker')
    if [[ -n "$pids" ]]; then
        echo "Stopping Celery worker..."
        kill -9 $pids
    fi

    # 停止 Redis
    pids=$(pgrep -f 'Redis/redis-server')
    if [[ -n "$pids" ]]; then
        echo "Stopping Redis..."
        kill -9 $pids
    fi

    echo "All services stopped."
else
    echo "Unsupported operating system."
    exit 1
fi