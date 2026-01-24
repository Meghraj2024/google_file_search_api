from google import genai
import os
from dotenv import load_dotenv


load_dotenv()

client = genai.Client(api_key=os.getenv('GOOGLE_AI_API_KEY'))

files = client.files.list()

for f in files:
    print(f"name:", f.name)
    print(f"display_name:", f.display_name)
    print(f"mime_type:", f.mime_type)
    print(f"size:", f.size_bytes, "bytes")
    print("-" * 40)
