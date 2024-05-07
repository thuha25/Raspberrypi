import requests as re

VIDEO_URL = 'https://dl205.filemate5.shop/?file=M3R4SUNiN3JsOHJ6WWQ2a3NQS1Y5ZGlxVlZIOCtyaDN5b1J4OUQ4V0w0OEhnNnNKOHNlVUVJSUVHSTQ5N0ticEl2RmgyeHFUVlBhdEZTeTloZE1BYlVIS3p2a0lqUXJ0MXJ3VFpwb25CZ2EybHZiMzBEZC9oUUxLYnRuWkhlVVRQMUZpckZWM3hpU1dpYVB5dEFXczlpK0xvZ2pSU2lFVG1Ub3lhT0hSeE05eDZqcWRQK2VxM29CUjZ5R2E3Y2QvOUxhWXJCSC8wYmNxc2RGd0F4VWpJc1VOak02Z2phQ0t0bEZFaEp0Sg%3D%3D'
print('Downloading...')
with re.get(VIDEO_URL, stream=True) as r:
    r.raise_for_status()
    with open("./video.mp4", 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
