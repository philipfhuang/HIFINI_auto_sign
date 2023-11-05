import os
import requests


def sign_in(client):
    url = "https://www.hifini.com/sg_sign.htm"
    cookie = os.getenv("COOKIE")

    if cookie is None:
        print("COOKIE 环境变量未设置")
        exit(1)

    headers = headers = {
        "Accept": "text/plain, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Length": "0",
        "Cookie": cookie,
        "Dnt": "1",
        "Origin": "https://www.hifini.com",
        "Referer": "https://www.hifini.com/",
        "Sec-Ch-Ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    response = client.post(url, headers=headers)
    response.raise_for_status()

    data = response.text
    print(data)
    return "成功" in data


if __name__ == "__main__":
    client = requests.Session()
    success = sign_in(client)
    if success:
        print("签到成功")
    else:
        print("签到失败")
        exit(3)
