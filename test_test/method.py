import requests

method = ['GET', 'POST', 'PUT', 'DELETE' ]
method_len = len(method)
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
url_upd = ["response_get_params", "response_post_data", "response_put","response_delete_data"]
url_upd_len = len(url_upd)


response_get = requests.get(url)
response_post = requests.post(url)
response_put = requests.put(url)
response_delete = requests.delete(url)
response_head = requests.head(url)

response_get_params = requests.get(url, params = {"method": "GET"})
response_post_data = requests.post(url, data = {"method":"POST"})
response_put_data = requests.put(url, data = {"method":"PUT"})
response_delete_data = requests.delete(url, data = {"method":"DELETE"})

print("1)Ответы на  http-запрос любого типа без параметра method:")
print(f'метод GET возвращает: {response_get.status_code}, {response_get.text}')
print(f'метод POST возвращает: {response_post.status_code}, {response_post.text}')
print(f'метод PUT возвращает: {response_put.status_code},{response_put.text}')
print(f'метод DELETE возвращает: {response_delete.status_code}, {response_delete.text}')
print()
print("2)Ответы на  http-запрос не из списка, например HEAD без параметра method:")
print(f'метод HEAD возвращает: {response_head.status_code}',{response_head.reason})
print()
print("3)Ответы на  http-запрос любого типа c правильными параметрами method:")
print(f'метод GET возвращает: {response_get_params.status_code}, {response_get_params.text}')
print(f'метод POST возвращает: {response_post_data.status_code}, {response_post_data.text}')
print(f'метод PUT возвращает: {response_put_data.status_code},{response_put_data.text}')
print(f'метод DELETE возвращает: {response_delete_data.status_code}, {response_delete_data.text}')
print()
print("4) Проверка всех возможных сочетаний реальных типов запроса и значений параметра method:")

for i in range(0,method_len):
    response_get_params = requests.get(url, params={"method": method[i]})
    print(f'метод GET + params = {method[i]} возвращает: {response_get_params.status_code}, {response_get_params.text}')
for i in range(0, method_len):
    response_post_data = requests.post(url, data={"method": method[i]})
    print(f'метод POST + data = {method[i]} возвращает: {response_post_data.status_code}, {response_post_data.text}')
for i in range(0, method_len):
    response_put_data = requests.put(url, data={"method": method[i]})
    print(f'метод PUT + data = {method[i]} возвращает: {response_put_data.status_code},{response_put_data.text}')
for i in range(0, method_len):
    response_delete_data = requests.delete(url, data={"method": method[i]})
    print(f'метод DELETE + data = {method[i]} возвращает: {response_delete_data.status_code}, {response_delete_data.text}')



