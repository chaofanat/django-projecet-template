## Django 应用开发规范

> 本文档定义了本模板中 Django 应用的开发规范，所有新应用开发必须遵循此规范，以最契合的使用模板的用户系统等功能。

### 一、应用目录结构

```
appXXX/
├── __init__.py
├── admin.py          # Django Admin 后台配置
├── apis.py           # JWT/Bearer 认证的 API (可选)
├── apis_session.py   # Session 认证的 API (可选)
├── apps.py           # 应用配置
├── migrations/       # 数据库迁移文件
├── models.py         # 数据模型
├── schemas.py        # Pydantic Schema (API 数据验证)
├── tasks.py          # Celery 异步任务 (可选)
├── templates/        # 模板文件
│   └── appXXX/       # 以应用名命名的子目录
├── tests.py
├── urls.py           # 页面路由（仅用于模板导航）
├── utils/            # 工具类目录 (可选)
│   ├── __init__.py
│   └── *.py          # 具体业务工具
└── views.py          # 视图函数（仅用于页面渲染）
```

### 二、两套 API 认证系统

#### 2.1 Session 认证 API

- **用途**：使用 Django Session 认证，适用于已登录用户的前端交互
- **文件位置**：`appXXX/apis_session.py`
- **注册位置**：`MainConfig/apis.py`
- **API 访问路径**：`/api/xxx/...`
- **用户获取**：`request.user`

```python
# MainConfig/apis.py 注册示例
api_session.add_router("/xxx", "appXXX.apis_session.router", tags=["功能名称"])
```

#### 2.2 JWT/Bearer 认证 API

- **用途**：使用 JWT Token 认证，适用于移动端、第三方集成
- **文件位置**：`appXXX/apis.py`
- **注册位置**：`MainConfig/apis_v1.py`
- **API 访问路径**：`/api/v1/xxx/...`
- **用户获取**：`request.auth`

```python
# MainConfig/apis_v1.py 注册示例
api.add_router("/xxx", "appXXX.apis.router", tags=["功能名称"])
```

### 三、项目命名规范

#### 3.1 应用命名

- **应用目录名**：驼峰命名 + `app` 前缀
  - 示例：`appNews`、`appToDoList`、`appDailyNote`
  - 配置类名：`AppnewsConfig`（应用名小写 + Config）

#### 3.2 Model 命名

- **模型类名**：驼峰命名，单数形式
  - 示例：`News`、`InfoSite`、`StoredFile`、`AIappProject`

#### 3.3 Schema 命名

- **输入 Schema**：模型名 + `In` 后缀
  - 示例：`NewsIn`、`InfoSiteIn`、`DailyNoteIn`

- **输出 Schema**：模型名 + `Out` 后缀
  - 示例：`NewsOut`、`InfoSiteOut`、`DailyNoteOut`

#### 3.4 函数命名

- **视图函数**：snake_case，动词开头
  - 示例：`get_stats`、`list_projects`、`create_note`

- **工具函数**：snake_case，动词开头
  - 示例：`calculate_exp`、`update_level`、`clean_text`

#### 3.5 变量命名

- **普通变量**：snake_case
  - 示例：`user_stats`、`news_list`、`info_site`

- **常量**：全大写 + 下划线
  - 示例：`PRIORITY_CHOICES`、`MAX_UPLOAD_SIZE`

#### 3.6 URL 路由命名

- **页面路由**：小写 + 连字符
  - 示例：`/appNews/`、`/todolist/`、`/stockanalysis/`

- **API 路由**：小写 + 连字符
  - Session API：`/api/news/`、`/api/todolist/`
  - JWT API：`/api/v1/dashboard/`、`/api/v1/todolist/`

#### 3.7 文件命名

| 文件类型 | 命名规范 | 示例 |
|----------|----------|------|
| Session API 文件 | `apis_session.py` | `appNews/apis_session.py` |
| JWT API 文件 | `apis.py` 或 `api.py` | `appNews/apis.py` |
| 工具类文件 | snake_case | `AIBase.py`、`crawler.py` |

#### 3.8 数据库字段命名

- **字段名**：snake_case
  - 示例：`created_at`、`is_active`、`pub_date`

- **外键字段**：关联模型名小写 + `_id`
  - 示例：`site_id`、`user_id`

---

### 四、静态文件与媒体文件规范

- **静态文件 (CSS/JS/图片等)**：统一存放在项目级 `static/` 目录
  - 按应用创建子目录：`static/appXXX/`
  - 示例：`static/appToDoList/`、`static/appDashboard/`
  - **禁止**在应用目录下存放 static 文件夹

```python
# settings.py 配置
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```

- **媒体文件 (用户上传文件等)**：统一存放在项目级 `media/` 目录
  - 按应用创建子目录：`media/appXXX/`
  - 示例：`media/appIndex/`、`media/objectsstorage/`

```python
# settings.py 配置
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```

- **文件引用方式**：
  ```html
  <!-- 静态文件 -->
  {% load static %}
  <link rel="stylesheet" href="{% static 'appToDoList/style.css' %}">

  <!-- 媒体文件 -->
  <img src="{{ user.profile_pic.url }}" alt="头像">
  ```

---

### 五、视图与路由分离原则

- **views.py**：仅用于页面模板渲染和导航 URL 定义，**不要**开发任何功能 API
- **urls.py**：注册到 `MainConfig/urls.py` 用于页面路由
- **apis.py/apis_session.py**：功能 API 分别注册到 `MainConfig/apis_v1.py` 或 `MainConfig/apis.py`

### 六、数据模型规范 (models.py)

```python
from django.db import models

class YourModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ['-created_at']
        verbose_name = '模型名称'
        verbose_name_plural = '模型名称'
```

### 七、Schema 规范 (schemas.py)

- 定义 `Response` 统一响应格式
- 定义 `*In` 输入 Schema 和 `*Out` 输出 Schema
- 必要时重写 `from_orm` 方法解决序列化问题（如 URLField 转换、方法属性序列化等）

```python
from pydantic import BaseModel, ConfigDict
from typing import Optional, Any

class Response(BaseModel):
    code: int
    msg: str
    data: Optional[Any] = None

class YourModelOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    # ... 字段定义
```

### 八、新应用注册清单

| 位置                       | 配置内容                      |
| -------------------------- | ----------------------------- |
| `MainConfig/settings.py` | `INSTALLED_APPS` 添加应用名 |
| `MainConfig/urls.py`     | 添加页面路由                  |
| `MainConfig/apis.py`     | 添加 Session API 路由         |
| `MainConfig/apis_v1.py`  | 添加 JWT API 路由             |
| `MainConfig/celery.py`   | 添加定时任务（如需要）        |

### 九、CSRF Token 处理规范

前端调用 Session API 时需要正确处理 CSRF Token，否则会返回 403 Forbidden 错误。

#### 9.1 模板中定义 CSRF Token

在 HTML 模板中使用 Django 模板标签定义全局变量：

```html
<script>
// CSRF Token - Django 模板会替换 {{ csrf_token }}
const CSRF_TOKEN = '{{ csrf_token }}';
</script>
```

**重要**：
- 必须在 HTML 模板的 `<script>` 标签内定义
- 外部静态 JS 文件中的 `{{ csrf_token }}` 不会被 Django 处理
- 必须在引入外部 JS 文件之前定义此全局变量

#### 9.2 API 类中使用 CSRF Token

```javascript
// 获取 CSRF Token
function getCSRFToken() {
    return typeof CSRF_TOKEN !== 'undefined' ? CSRF_TOKEN : '';
}

// API 类
class YourAPI {
    async request(endpoint, options = {}) {
        const defaultOptions = {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()  // 使用 CSRF Token
            },
            credentials: 'same-origin'
        };
        // ...
    }
}
```

#### 9.3 静态文件收集

静态文件修改后需要重新收集：

```bash
# Docker 环境中
docker exec <container_name> python manage.py collectstatic --noinput

# 本地开发环境
.venv/Scripts/python manage.py collectstatic
```

#### 9.4 完整示例

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>应用标题</title>
    <link rel="stylesheet" href="{% static 'appXXX/style.css' %}">
</head>
<body>
    <!-- 页面内容 -->

    <!-- CSRF Token 定义（必须在引入 JS 文件之前） -->
    <script>
    const CSRF_TOKEN = '{{ csrf_token }}';
    </script>

    <!-- 引入外部 JS -->
    <script src="{% static 'appXXX/api.js' %}"></script>
    <script src="{% static 'appXXX/app.js' %}"></script>
</body>
</html>
```

---

### 十、命令速查

```bash
# 创建应用
.venv/Scripts/python manage.py startapp appXXX

# 数据库迁移
.venv/Scripts/python manage.py makemigrations
.venv/Scripts/python manage.py migrate

# 收集静态文件
.venv/Scripts/python manage.py collectstatic

# Docker 环境收集静态文件
docker exec <container_name> python manage.py collectstatic --noinput

# 启动开发服务器
.venv/Scripts/python manage.py runserver
```
