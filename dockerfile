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

#设置系统环境变量SERVER_URL
ENV REDIS_SERVER_URL=redisserver

# 暴露端口
EXPOSE 8080

# 启动命令
CMD ["sh", "-c", "celery -A MainConfig worker -l info -P threads & python manage.py runserver 0.0.0.0:8080"]

#生产环境
#CMD ["sh", "-c", "celery -A MainConfig worker -l info -P threads & python run.py"]