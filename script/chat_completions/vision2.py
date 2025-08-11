import base64
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

functionalities = [
    {
        "nome": "Register new user",
        "imagens": ["./images/par/par3.png", "./images/par/par4.png", "./images/par/par2.png"]
    },
    {
        "nome": "Login",
        "imagens": ["./images/par/par3.png", "./images/par/par4.png", "./images/par/par2.png"]
    },
        {
        "nome": "Logout",
        "imagens": ["./images/par/par7.png", "./images/par/par4.png"]
    },
            {
        "nome": "View profile",
        "imagens": ["./images/par/par1.png", "./images/par/par6.png"]
    },
                {
        "nome": "Edit profile",
        "imagens": ["./images/par/par6.png"]
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
{func['nome']} feature in the Par de jarro app.
This is a roommate-sharing app. It connects to a database that records registered users if the registration is successfully completed.
Please consider that to carry out these tests you only have access to the Linux operating system, and the Firefox and Chrome browsers.
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
    answer_path = f"./answers/par-de-jarro/retest-6/{func['nome'].replace(' ', '_').lower()}.md"

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