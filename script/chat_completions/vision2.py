import base64
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

functionalities = [
    {
        "nome": "Create Text Note",
        "imagens": ["./images/note/note2.png","./images/note/note4.png"]
    }
]

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  
def create_file(file_path, content):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'w') as file:
        file.write(content) 

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

for func in functionalities:
    textual_message = f"""From the point of view of a tester, give me exploratory test cases to the
{func['nome']} feature in the Omni-notes app.
This app is a note taking application . Please consider that to carry out these tests you only have access to an android cell phone. 
To use this app it is not necessary to create an account or log in, 
therefore it is not necessary to include tests related to this. The app is in portuguese, 
but you must answer in english. Notes are already saved after filling in any of the form fields, 
there is no need to click on any button to save them. Also pass throug each form of attachment
Consider unusual flows, try to find possible bugs, failures,
security issues, etc.
I will provide screenshots of the app GUI.
The test cases should follow the structure below:
- test number
- Description: The test case description
- Prerequisites: Specifies the conditions that must be met
before executing the test steps
- Steps: Enumerated steps to execute the test
- Expected results: The expected test results"""

    image_paths = func["imagens"]
    answer_path = f"./answers/OmniNotes/retest-6/prompt6-2.md"

    payload = {
        "model": "gpt-4o-2024-05-13",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": textual_message
                    }
                ]
            }
        ]
    }

    for image_path in image_paths:
        base64_image = encode_image(image_path)
        image_url = {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
        }
        payload["messages"][0]["content"].append(image_url)

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=payload
    )

    content = response.json()['choices'][0]['message']['content']
    create_file(answer_path, content)
    print(f"File created at: {answer_path}")