from torchvision import models, transforms
import torch
import json
from torchvision.models import resnet50, ResNet50_Weights

# Загрузка предобученной нейросети
model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V2)
model.eval()

# Загрузка файла с метками классов
with open('imagenet_labels.json', 'r', encoding='utf-8') as f:
    class_labels = [line.strip() for line in f.readlines()]

def classify_image(image):
    # Преобразование изображения в формат, подходящий для модели
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)

    # Классификация изображения с использованием модели
    with torch.no_grad():
        output = model(input_batch)

    _, predicted_idx = torch.max(output, 1)
    predicted_label = class_labels[predicted_idx.item()]

    # Удаление кавычек и запятых из результата
    predicted_label = predicted_label.replace('"', '').replace(',', '')

    return predicted_label