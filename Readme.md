# NVILLC2
![alt tag](https://img.hhcdn.ru/employer-logo/3888364.png)

Это сервис для классификации изображений с использованием предварительно обученной модели глубокого обучения. В нем используется архитектура ResNet-50(IMAGENET1K_V2) и набор данных ImageNet для классификации.

## Задача:
Реализовать простейший сервис для классификации изображений: пользователь
загружает картинку, ему выводится, что на ней изображено.

#### Функциональные требования:
- Сервис запускается локально, на 80 порту (или каком-то другом порту) поднимается
веб-приложение
- У приложения примерно такой интерфейс:
- Есть кнопка “Загрузить картинку” – при нажатии на нее пользователю предлагается
загрузить картинку для классификации.
- После загрузки появляется результат распознавания – ширина и высота изображения в
пикселях, а также ответ классификатора.

#### Рекомендации: (необязательны, но приветствуются)
- Для классификации изображений используется нейросеть (можно взять готовую
отсюда: https://pytorch.org/vision/stable/models.html)
- Решение залито в репозиторий на Github/Gitlab

#### Критерии оценивания:
- К решению приложена инструкция для запуска и тестирования приложения.
Проверяющий будет следовать этой инструкции.
- Приложение соответствует функциональным требованиям, описанным в этом
документе.
- Приложение более-менее корректно распознает, что изображено на картинках.

## Файлы в проекте:
```python
app.py: Этот файл содержит основной код Flask-приложения. Он отвечает за обработку запросов, загрузку изображений, их классификацию и вывод результатов.

logger.py: В этом файле находится код, связанный с логированием.

config.py: В этом файле содержатся конфигурационные параметры приложения.

model.py: Этот файл содержит код, связанный с моделью классификации изображений.
```
## Установка

Для запуска этого проекта локально следуйте этим шагам:
1. Клонируйте репозиторий:
```bash
git clone https://github.com/IlyaAriskin/NVILLC2.git
```
2. Установите необходимые зависимости
```bash
pip install -r requirements.txt
```
3. Запустите приложение

```bash
python app.py
```

## Скриншоты

![alt text](inter_1.jpg)

![alt text](inter_2.jpg)

## Использование:

```python

1. Загрузите изображение с помощью предоставленной формы "Выбрать картинку".

2. Нажмите кнопку "Загрузить" для классификации загруженного изображения.

3. Предсказанный класс будет отображен на экране.
```

