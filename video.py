import requests as re

VIDEO_URL = 'https://dl125.filemate17.shop/?file=M3R4SUNiN3JsOHJ6WWQ2a3NQS1Y5ZGlxVlZIOCtyaDJpNTRzemhRbUR1QnVxWjk4MDl2emRabGZZS29mbWN5a0dOSlJ5aTdaWmRqV2RWMnZyNWN6Vm1hRDhwTnZuekxmcDh0eWY4ODBCRENveWVPZ2tUUjdvQVhIZmVlZVEraEdJM3ByOXdaazFpbk8rdCtTdkEzb3VtK29zMFNPYVhsYjVXcGViYUNEcE00ZmszckNkZks1Z2NKZC8zN1o4WXdVM3ZMTw%3D%3D'
print('Downloading...')
with re.get(VIDEO_URL, stream=True) as r:
    r.raise_for_status()
    with open("./video.mp4", 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
