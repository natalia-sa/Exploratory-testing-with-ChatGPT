import base64
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

functionalities = [
    {
        "name": "Feature",
        "images": []
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
    textual_message = f"""From the point of view of a tester, give me exploratory test cases for the 
    {func['name']} ..."""

    image_paths = func["images"]
    answer_path = f"./answers/{func['name']}"

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