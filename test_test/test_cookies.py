import requests

class TestCookie:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        resp_cookie = response.cookies
        print(resp_cookie)
        assert response.cookies.get("HomeWork") == "hw_value","There is no cookie 'HomeWork=hw_value' in response"

