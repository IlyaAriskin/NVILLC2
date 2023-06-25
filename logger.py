import logging
import os

# Создание объекта логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Создание пути для файла логов
log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app.log')

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)

# Создание форматтера логов
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)