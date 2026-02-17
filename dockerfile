FROM crpi-fhdn7tv1nno7r3nv.cn-shanghai.personal.cr.aliyuncs.com/chaofanat/python:latest AS builder
USER root

WORKDIR /app


#复制requirements.txt文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt


FROM builder
USER root

WORKDIR /app
# 复制项目文件
# COPY . /app

# 设置 Redis 服务器地址环境变量（可通过 docker-compose 覆盖）
ENV REDIS_SERVER_URL=redisserver
ENV ENABLE_ASYNC_SERVICES=false

# 暴露端口
EXPOSE 8080

# 启动脚本 - 根据环境变量决定是否启动 Celery
CMD ["sh", "-c", "if [ \"$ENABLE_ASYNC_SERVICES\" = \"true\" ]; then celery -A MainConfig worker -l info -P threads & fi; python manage.py runserver 0.0.0.0:8080"]

#生产环境
#CMD ["sh", "-c", "celery -A MainConfig worker -l info -P threads & python run.py"]