import requests

class TestHeaders:
    def test_headers(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        resp_headers = response.headers
        print(resp_headers)
        assert response.headers.get("x-secret-homework-header") == "Some secret value","There is no headers  'x-secret-homework-header': 'Some secret value' in response"

