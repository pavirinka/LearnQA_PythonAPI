import requests

class TestCookie:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        resp_cookie = response.cookies
        print(resp_cookie)
        #resp_cookie = response.cookies.get("HomeWork")
        assert "hw_value" in resp_cookie,"There in no hw_value in the response"
        assert "HomeWork" in resp_cookie,"There in no HomeWork in the response"
