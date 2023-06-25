from flask import Flask, request, render_template, jsonify
from PIL import Image
import io
import os
import uuid
import shutil
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from model import classify_image
import webbrowser
from logger import logger


# Создание экземпляра приложения Flask
app = Flask(__name__, static_url_path='/static')

def clear_uploads_folder():
    """
    Удаляет все файлы в папке 'uploads'.
    """
    try:
        for filename in os.listdir(UPLOAD_FOLDER):
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        logger.info("Файлы в папке 'uploads' успешно удалены.")
    except Exception as e:
        logger.exception(f"Ошибка при удалении файлов из папки 'uploads': {e}")

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    """
    Обрабатывает загрузку и классификацию изображения.
    """
    error_message = None

    if request.method == 'POST':
        # Получение загруженного изображения
        image_file = request.files['image']
        filename = image_file.filename
        file_ext = os.path.splitext(filename)[1].lower()

        # Проверка расширения файла
        if file_ext not in ALLOWED_EXTENSIONS:
            error_message = "Неверный тип файла. Пожалуйста, загрузите допустимое изображение."
            logger.warning(f"Неверный тип файла загружен: {filename}")
        else:
            try:
                image = Image.open(io.BytesIO(image_file.read()))

                # Конвертация PNG в JPEG
                if file_ext == '.png':
                    image = image.convert('RGB')

                # Генерация уникального имени файла
                filename = str(uuid.uuid4()) + '.jpg'
                filepath = os.path.join(UPLOAD_FOLDER, filename)

                # Сохранение изображения
                image.save(filepath)

                # Определение ширины и высоты изображения
                width, height = image.size

                # Классификация изображения
                predicted_class = classify_image(image)

                # Вывод результата
                result = {
                    'width': width,
                    'height': height,
                    'class': predicted_class,
                    'filename': filepath
                }
                return render_template('index.html', result=result)
            except Exception as e:
                error_message = "Ошибка обработки изображения. Пожалуйста, попробуйте еще раз."
                logger.exception(f"Ошибка обработки изображения: {e}")

    return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    # Запуск браузера при запуске приложения
    webbrowser.open_new_tab("http://localhost:80")
    app.run(port=80)
    clear_uploads_folder()