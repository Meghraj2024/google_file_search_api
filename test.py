from google import genai
import os

client = genai.Client(api_key="AIzaSyAobFk-TqgMEQ7Lz4wjYfu6R4oXcPImZh4")

files = client.files.list()

for f in files:
    print(f"name:", f.name)
    print(f"display_name:", f.display_name)
    print(f"mime_type:", f.mime_type)
    print(f"size:", f.size_bytes, "bytes")
    print("-" * 40)
