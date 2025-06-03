from deepface import DeepFace

result = DeepFace.verify(img1_path='photos/image1.png', img2_path='photos/image4.png')


print(f"Результат: {'Одинаковые люди' if result['verified'] else 'Разные люди'}")
print(f"Расстояние: {result['distance']:.4f}")
print(f"Порог схожести: {result['threshold']:.4f}")
print(f"Модель: {result['model']}")
print(f"Детектор: {result['detector_backend']}")
print(f"Метрика схожести: {result['similarity_metric']}")
print(f"Время анализа: {result['time']:.2f} секунд")

print("Изображение 1:")
face1 = result['facial_areas']['img1']
print(f"  Координаты: x={face1['x']}, y={face1['y']}")
print(f"  Размер: {face1['w']}x{face1['h']} пикселей")
print(f"  Левый глаз: {face1['left_eye']}")
print(f"  Правый глаз: {face1['right_eye']}")


face2 = result['facial_areas']['img2']
print(f"  Координаты: x={face2['x']}, y={face2['y']}")
print(f"  Размер: {face2['w']}x{face2['h']} пикселей")
print(f"  Левый глаз: {face2['left_eye']}")
print(f"  Правый глаз: {face2['right_eye']}")


similarity_percent = (1 - result['distance']) * 100
print(f"Схожесть лиц: {similarity_percent:.1f}%")

if result['verified']:
    print("Лица принадлежат одному человеку")
else:
    print("Лица принадлежат разным людям")
    if result['distance'] > result['threshold'] * 1.5:
        print("Лица очень разные")
    else:
        print("Лица имеют некоторое сходство, но недостаточное для совпадения")