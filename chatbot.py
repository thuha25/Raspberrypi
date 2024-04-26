import json
import requests as re
API_KEY = 'AIzaSyAWFiq9tAnMTQvlVtMeO1D14SrZXQigPWs'
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"


while True:
    prompt = input(">>> ")
    content = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    res = re.post(URL, headers={
        'Content-Type': 'application/json_data;charset=UTF-8'}, data=json.dumps(content))

    json_data = res.json()
    if 'candidates' in json_data and len(json_data['candidates']) > 0:
        content = json_data['candidates'][0]['content']
        parts = content['parts']
        code = parts[0]['text']

        start_marker = code.find("`python\n") + len("`python\n")
        end_marker = code.rfind("```")
        extracted_code = code[start_marker:end_marker]

        print(extracted_code)

        with open('_code.py', 'w', encoding='UTF-8') as f:
            f.write(extracted_code)
