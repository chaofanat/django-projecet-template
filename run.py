from waitress import serve
from MainConfig.wsgi import application

serve(
    app=application,
    host='0.0.0.0',
    port=8080
)