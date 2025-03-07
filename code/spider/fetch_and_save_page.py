import requests

def fetch_and_save_page(url, file_path=r"E:\code\spider\page_content.txt"):
    """
    请求指定的 URL,并将页面内容保存到文件中

    :param url: 要请求的网页 URL
    :param file_path: 保存 HTML 内容的文件路径，默认值为 'E:\code\spider\page_content.txt'
    """
    # 请求头伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        # 发送请求
        response = requests.get(url, headers=headers, timeout=30)

        # 打印状态码
        print("状态码: {}".format(response.status_code))

        # 如果响应状态码为200
        if response.status_code == 200:
            # 获取 HTML 内容
            html_data = response.text

            # 写入文件
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(html_data)

            print(f'HTML 数据已成功写入 {file_path}')

        else:
            print(f'请求失败，错误状态码: {response.status_code}')

    except requests.exceptions.RequestException as e:
        print("请求出错:", e)



