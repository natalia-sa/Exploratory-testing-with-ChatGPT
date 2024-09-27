# Exploratory testing with ChatGPT

Script used to to call OpenAI completions API, using textual message and images as input. It was created based on the doc: https://platform.openai.com/docs/guides/vision?lang=python

## Run

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```

3. Add your OpenAI API key to a `.env` file following .env.example

4. Run the script:
    ```bash
    python3 ./scripts/visionWithEncodedImage.py  
    ```