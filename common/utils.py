import requests

# 指定URLへリクエストしbodyを取得
def get_body(url):
    return requests.get(url).json()

# 
def write_file(path, body):
    f = open(path, 'w', encoding='UTF-8')
    f.write(body)
    f.close()

def read_file(path):
    f = open(path, 'r', encoding='UTF-8')
    body = f.read()
    f.close()
    return body