# import requests
#
#
# url = "https://api2.mubu.com/v3/api/user/phone_login"
#
# data = {
#     "phone": "18245297665",
#     "password": "123456lwj",
#     "callbackType": 0
# }
# proxies = {
#     "https": "http://127.0.0.1:8888",
# "http": "http://127.0.0.1:8888",
# }
# header = {
#                     "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
#                     "version": "3.0.0-2.0.0.1934",
#                     "sec-ch-ua-mobile": "?0",
#                     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
#                     "data-unique-id": "deead2a0-bd7b-4432-9632-3d1dd82cb940",
#                     "content-type": "application/json;charset=UTF-8",
#                     "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMjU0NzY0ODAiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2OTM4MDQwNDksImlhdCI6MTY5MTIxMjA0OX0.JcwAqIV9l1-9gazjGa0Tz0v6JITcR0gfd8Yw6ABu3MF1-G92Hb5wOxq41upa8AVgWxCTy7o_nI_6Zo29kc6Nvw",
#                     "x-request-id": "63ec7e4a-00a4-4543-b74b-3ebba5c87fe7",
#                     "sec-ch-ua-platform": '"Windows"',
#                     "sec-fetch-site": "same-site",
#                     "sec-fetch-mode": "cors",
#                     "sec-fetch-dest": "empty",
#                 }
# resp = requests.post(url=url, headers=header, json=data, proxies=proxies)
# print(resp.json())


"""
查看报告：
默认的测试报告：hrun testcase --html==test.html
allure测试报告：hrun testcase --alluredir=reports/
              allure serve reports/

locust: locusts -f testcase/mubu_login_test.py
"""