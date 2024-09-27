 @echo off
    setlocal

    echo Stopping services...

    @REM :: 停止 Django 开发服务器
    taskkill /F /IM python.exe /T
   

    @REM :: 停止 Celery worker
    taskkill /F /IM celery.exe /T

    @REM :: 停止 Redis
    Redis\redis-cli flushall
    Redis\redis-cli shutdown
    timeout /t 3 /nobreak
    echo Redis stopped.
    taskkill /F /IM redis-server.exe /T

    echo All services stopped.

    endlocal