import requests

urls = 'https://shem1234.s3.ap-northeast-2.amazonaws.com/test_json.json'

response = requests.get(urls)

print(response)