import os

# Путь к папке для загрузки файлов
UPLOAD_FOLDER = 'static/uploads'

# Разрешенные расширения файлов
ALLOWED_EXTENSIONS = ['.jpg', '.jpeg', '.png']

# Создание папки UPLOAD_FOLDER, если она не существует
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
