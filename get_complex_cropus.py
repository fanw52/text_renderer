import requests
import json
session = requests.Session()
session.headers['Authorization'] = "df620992-d943-4684-924b-b83c9605c48a"

headers = {
    "Authorization": "df620992-d943-4684-924b-b83c9605c48a"
}


def request_server(url, text, method="POST"):
    data = {
        "parameters": {
            "locale": "zh-hant"
        },
        "inputData": {
            "dataList": [
                {
                    "id": "1",
                    "content": text
                }
            ]
        },
        "experimentId": "1"
    }
    my_headers = {
        "Content-Type": "application/json"
    }
    my_headers.update(headers)
    resp = requests.request(method, url, headers=my_headers, data=json.dumps(data), timeout=200)

    return resp.json()






url = "http://192.168.51.40:32275/zhconv"

path = "./example_data/text/wiki_complex_corpus.txt"
output_path = "./example_data/text/wiki_complex_corpusv2.txt"
result = []
c = 0
with open(path,encoding="utf-8") as rfile:
    for line in rfile.readlines():
        s = request_server(url,line)
        out_line = s['data']['outputData'][0]['targetContent']
        result.append(out_line)
        c+=1
        if c==3000000:
            break


with open(output_path,'w',encoding="utf-8") as wfile:
    for line in result:
        wfile.writelines(line)