import json
import google.generativeai as genai

def load_api_key(file_path='key.json'):
    try:
        with open(file_path, 'r') as file:
            api_keys = json.load(file)
            google_api_key = api_keys.get('google_api_key', '')

            # Configure the genai library with the Google API key
            genai.configure(api_key=google_api_key)

            print("API keys loaded successfully.")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON in the file {file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
load_api_key('./keys.json')

model = genai.GenerativeModel('gemini-pro')
prompt = input("Enter a prompt: ")
response = model.generate_content(prompt, stream=True)

for chunk in response:
    print(chunk.text)

#print(response.text)
#print(response.prompt_feedback)
