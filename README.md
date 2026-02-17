# django-project-template

## 项目概述

一个django项目启动模板。

集成了django-allauth、django-allauth-bootstrap5、simpleui、django-ninja、django-ninja-jwt等django适配的应用，用于提供一个基础设施更加完善的django项目启动模板。

项目模板功能

- [X] 账户相关功能界面美化。基于django-allauth-bootstrap5。
- [X] 三方登录集成。基于django-allauth。
- [X] 后台管理界面美化。基于simpleui。
- [X] api开发集成。基于django-ninja。
- [X] api登录JWT认证。基于django-ninja-jwt.
- [X] 集成django框架实时分析和检查工具。基于django-silk
- [X] 生产环境wsgi服务器。基于waitress。

其他：

* [X] 建立了templates文件夹，用于管理所有前端页面。
* [X] 建立了locale文件夹，用于管理项目语言本地化。
* [X] 建立appIndex应用，作为项目初始主页以及示例。
* [X] 配置vscode调试launch.json文件
* [X] 完成了三方适配应用的相关开箱即用的初始配置。
* [X] 可选集成redis作为内存管理服务和Celery进行异步任务调度管理（默认不启用）。
* [X] 配置了dockerfile等docker相关配置。
* [X] 集成了nginx进行请求转发。对静态文件以及媒体文件的访问做了优化处理。


## 快速部署

1. 将项目拉到本地

```cmake
    git clone https://gitee.com/chaofanat/django-projecet-template.git
```

2. 安装依赖

   ```cmake
   pip install -r requirements.txt
   ```
3. 数据库迁移

   ```cmake
   python manage.py makemigrations
   python manage.py migrate
   ```
4. 创建超级用户

   ```cmake
   python manage.py createsuperuser
   ```
5. 配置邮箱相关配置MainConfig/settings.py

   ```python
   # email
   #邮件配置,需要去三方邮箱开启授权服务
   # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.qq.com'  # 如果是 163 改成 smtp.163.com
   EMAIL_PORT = 465
   EMAIL_HOST_USER = 'chaofanat@qq.com'  # 发送邮件的邮箱帐号
   EMAIL_HOST_PASSWORD = 'abcderfetg'  # 授权码,各邮箱的设置中启用smtp服务时获取
   DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  #收件人显示发件人的邮箱
   # DEFAULT_FROM_EMAIL = '<xxxxx@qq.com>' #也可以随意写
   EMAIL_USE_SSL = True   # 使用ssl
   # EMAIL_USE_TLS = False # 使用tls
   # EMAIL_USE_SSL 和 EMAIL_USE_TLS 是互斥的，即只能有一个为 True
   ```
6. 启动服务

   **默认模式（仅 Django，不启动 Redis/Celery）：**

   ```cmake
   # Windows - 8080端口访问
   start_for_windows.bat

   # Linux/macOS
   bash start_for_linux.sh
   ```

   **启用异步服务（Redis + Celery）：**

   创建 `.env` 文件设置 `ENABLE_ASYNC_SERVICES=true`：

   ```cmake
   # 复制示例配置
   cp .env.example .env

   # 编辑 .env，设置以下配置：
   # ENABLE_ASYNC_SERVICES=true
   ```

   然后运行启动脚本，或使用 Docker：

   ```cmake
   # Docker - 基础模式（仅 Django + Nginx）
   docker compose build
   docker compose up -d

   # Docker - 完整模式（包含 Redis + Celery）
   docker compose -f docker-compose.yml -f docker-compose.with-async.yml build
   docker compose -f docker-compose.yml -f docker-compose.with-async.yml up -d
   ```
7. 登录管理界面，添加三方登录

   ![1725534423502](image/README/1725534423502.png)


## 异步服务配置（Redis + Celery）

项目默认不启动 Redis 和 Celery，以减少启动复杂度和资源占用。

如需使用异步任务功能：

1. **复制配置文件：**
   ```bash
   cp .env.example .env
   ```

2. **修改 `.env` 文件：**
   ```env
   ENABLE_ASYNC_SERVICES=true
   ```

3. **重新启动服务**

**适用场景：**
- 需要执行耗时任务（如发送邮件、生成报表）
- 需要定时任务调度
- 需要 Redis 缓存功能

**不适用场景：**
- 简单的 CRUD 应用
- 开发/测试环境不需要异步处理
- 资源受限的环境


## 效果展示

![1725534529979](image/README/1725534529979.png)

![1725534567677](image/README/1725534567677.png)

![1725534590568](image/README/1725534590568.png)

![1725534625562](image/README/1725534625562.png)
