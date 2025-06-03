from deepface import DeepFace

result = DeepFace.analyze(img_path='photos/image1.png', actions=['age', 'gender', 'race', 'emotion'])


person = result[0]  


print(f"Возраст: {person['age']} лет")
print(f"Пол: {person['dominant_gender']} ({person['gender'][person['dominant_gender']]:.1f}%)")
print(f"Раса: {person['dominant_race']} ({person['race'][person['dominant_race']]:.1f}%)")
print(f"Эмоция: {person['dominant_emotion']} ({person['emotion'][person['dominant_emotion']]:.1f}%)")
print(f"Уверенность в детекции лица: {person['face_confidence']:.2f}")

print("Все эмоции:")
for emotion, value in person['emotion'].items():
    print(f"  {emotion}: {value:.2f}%")

print("\nВсе расы:")
for race, value in person['race'].items():
    print(f"  {race}: {value:.2f}%")

print("\nВсе гендеры:")
for gender, value in person['gender'].items():
    print(f"  {gender}: {value:.2f}%")