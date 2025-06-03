from deepface import DeepFace

result = DeepFace.find(img_path='image1.png',db_path='photos')

print(f"Найдено совпадений: {len(result[0])}")

if len(result[0]) > 0:

    for i, row in result[0].iterrows():
        similarity_percent = (1 - row['distance']) * 100
        match_quality = "Отличное" if row['distance'] < 0.3 else "Хорошее" if row['distance'] < 0.5 else "Слабое"
        
        print(f"\nСовпадение #{i+1}:")
        print(f"   Файл: {row['identity']}")
        print(f"   Расстояние: {row['distance']:.4f}")
        print(f"   Схожесть: {similarity_percent:.1f}%")
        print(f"   Качество совпадения: {match_quality}")
        print(f"   Порог: {row['threshold']}")

    best_match = result[0].iloc[0]
    best_similarity = (1 - best_match['distance']) * 100
    print(f"Лучший результат: {best_match['identity']}")
    print(f"Схожесть: {best_similarity:.1f}%")
    
    if best_match['distance'] < best_match['threshold']:
        print("Это тот же человек")
    else:
        print("Похож, но не тот же человек")
        
else:
    print("Похожих лиц не найдено")


print(f"Модель: {result[0].columns[-3] if len(result[0]) > 0 else 'N/A'}")
print(f"Детектор: opencv")
print(f"Метрика: cosine distance")