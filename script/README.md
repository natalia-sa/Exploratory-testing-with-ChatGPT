# Exploratory testing with ChatGPT

Script used to to call OpenAI completions API, using textual message and images as input. It was created based on the doc: https://platform.openai.com/docs/guides/vision?lang=python

## Run

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <script-directory>
    ```

2. Install the required dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```

3. Add your OpenAI API key to a `.env` file following .env.example. 

   - You can generate your key following the instructions in [openai-quick-start](https://platform.openai.com/docs/quickstart#create-and-export-an-api-key)

4. Run the script:
    ```bash
    python3 ./script/chatCompletions/visionWithEncodedImage.py  
    ```