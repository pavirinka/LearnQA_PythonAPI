import requests
import json
import time
#Создание задачи
resp = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
obj = json.loads(resp.text)
token_value = obj['token']
time_value = obj['seconds']
param = {'token':token_value}

print("Запрос с token ДО того, как задача готова и проверка поля status")
try:
    resp1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=param)
    status_obj1=json.loads(resp1.text)
    status1 = status_obj1['status']
    if status1 == "Job is NOT ready":
        print(f"Успешная проверка для поля status: {status1}")
        print()
        print("Ожидание и запрос с token После того, как задача готова и проверка поля status")
        time.sleep(time_value)
        resp2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=param)
        status_obj2 = json.loads(resp2.text)
        status2 = status_obj2['status']
        if status2 == "Job is ready":
            print(f"Успешная проверка для поля status: {status2}")
except KeyError:
    print("Передан token, для которого не создавалась задача. Провалена проверка для поля status")









