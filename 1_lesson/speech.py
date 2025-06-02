import speech_recognition as speech

mic_names = speech.Microphone.list_microphone_names()

r = speech.Recognizer()

answers = []

def sum_numbers(x,y):
    return x + y

with speech.Microphone() as source:
    audio = r.listen(source, timeout=5,phrase_time_limit=10)

    try:
        text_google = r.recognize_google(audio, language='ru-RU')
        #print(type(text_google))
        splitted_text = text_google.split()
        try:
            numbers = [int(number) for number in splitted_text]
            result = sum_numbers(x=numbers[0], y=numbers[1])
            print(result)
            answers.append(f"сумма = {result}")

        except Exception as e:
            print('не получилось преобразовать ответ гугла', e)
    except speech.UnknownValueError as u:
        print("не удалось распознать текст", u)
    except speech.RequestError as r:
        print("ошибка серсива:", r)

if mic_names:

    for device_index, mic_name in enumerate(mic_names):

        answers.append(f"используется микрофон: {device_index}: {mic_name}")

else:
    answers.append("микрофонов нет")

for i in answers:
    print(i)
    # из-за логов не видно то, что я принтую. я решил выводить в самом конце кода ответы 
    