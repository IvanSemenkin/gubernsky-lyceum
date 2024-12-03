from app import app

# Vercel требует функцию для обработки запросов
def handler(request, context):
    return app(request)
