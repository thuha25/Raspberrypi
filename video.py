import requests as re

VIDEO_URL = 'https://dl206.filemate18.shop/?file=M3R4SUNiN3JsOHJ6WWQ2a3NQS1Y5ZGlxVlZIOCtyZ0RrWkFabEZVQ1VPQmlyc2dNZ2FHQ2M0SmpJYUVHaHNHUkh0RlcvRENUT3ZlQ2RTemE4N2wzQ1gySnN2VnIvQjJmdUpvaEVzSjVFeldyM3NUM21EWTlpdzZ3VzRtSU41a1RUMUZ2NkU1cjBqUFkyUG1SbWthOWtsN21xVXJHVDNkUGsyc1NkdTJWMHNrTjl6bktKUFRzeG9sQWlIZmF3TGdNZ3FlVC94S3o1dU43bXYwd2ZHQS9lSmdZK3Ntdy9xSFBtaEJMMElrNjhnT3B1YmJnQUpjNUdacU9lQ040WTJkYnovYmdTUThMelNCYnFrcXo1dnRndkVaWU5QSlR6elcrNCtqVFJSYVBhY25KV2NiV2V0anpxOVd0cFA1a3NCejNpS1hDaElwSmhBMnpRY1g2RzRCZjRCcHo5UERidDU1dzBWK2ozMUpJMDdWY2tCK3ZKd291V01wUElTRT0%3D'
print('Downloading...')
with re.get(VIDEO_URL, stream=True) as r:
    r.raise_for_status()
    with open("./video.mp4", 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
