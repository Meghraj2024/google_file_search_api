import os
from google import genai
from google.genai import types
from pathlib import Path
import time
from dotenv import load_dotenv


load_dotenv()
#DATA_DIR = Path(r"C:\Users\meghr\google_file_search_api\data\DA_ML_Report.pdf")
client = genai.Client(api_key=os.getenv('GOOGLE_AI_API_KEY'))

# File name will be visible in citations
file_search_store = client.file_search_stores.create(config={'display_name': 'test-file'})

operation = client.file_search_stores.upload_to_file_search_store(
  file= Path(r"C:\Users\meghr\google_file_search_api\data\DA_ML_Report.pdf"),
  file_search_store_name=file_search_store.name,
  config={
      'display_name' : 'display-file-name',
  }
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="""Can you tell me about the report""",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name]
                )
            )
        ]
    )
)

print(response.text)