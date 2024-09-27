FROM crpi-fhdn7tv1nno7r3nv.cn-shanghai.personal.cr.aliyuncs.com/chaofanat/ngnix
USER root

# 拷贝 Nginx 配置文件
COPY ./conf/nginx.conf /etc/nginx/nginx.conf

# # 拷贝静态文件
# COPY ../staticfiles /etc/staticfiles

# #拷贝media文件
# COPY ../media /etc/media
#将nginx.conf文件中的127.0.0.1替换为app
RUN sed -i 's/127.0.0.1/mainservice/g' /etc/nginx/nginx.conf



# 暴露端口
EXPOSE 80


CMD ["nginx", "-g", "daemon off;"]