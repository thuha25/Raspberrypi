import json
import requests as re

API_KEY = 'AIzaSyAWFiq9tAnMTQvlVtMeO1D14SrZXQigPWs'
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"
MESSAGE_FORMAT = """
Command: {command}. Requirements: The code should be in Python. The code should import the necessary libraries. The code should be runnable.
"""

def get_response_text(data):
    content = data['candidates'][0]['content']
    parts = content['parts']
    response = parts[0]['text']
    return response

while True:
    prompt = input(">>> ")
    content = {
        "contents": [
            {
                "parts": [
                    {
                        "text": MESSAGE_FORMAT.replace("{command}", prompt)
                    }
                ]
            }
        ]
    }

    res = re.post(URL, headers={
        'Content-Type': 'application/json_data;charset=UTF-8'}, data=json.dumps(content))

    json_data = res.json()
    if 'candidates' in json_data and len(json_data['candidates']) > 0:
        code = get_response_text(json_data)
        
        start_marker = code.find("`python\n") + len("`python\n")
        end_marker = code.rfind("```")
        extracted_code = code[start_marker:end_marker]

        with open('_code.py', 'w', encoding='UTF-8') as f:
            f.write(extracted_code)
            
        try:
            import _code
        except Exception as e:
            print(e)
