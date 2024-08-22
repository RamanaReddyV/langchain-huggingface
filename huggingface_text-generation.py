
from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEndpoint

load_dotenv()  # Load environment variables from .env file
sec_key = os.getenv('HF_KEY')

llmObjectInstance = HuggingFaceEndpoint(

    repo_id="EleutherAI/gpt-neo-2.7B",
    task="text-generation",
    token=sec_key
)

text_Gen_Output = llmObjectInstance.invoke("Announce the release of our new eco-friendly water bottle.")

print(text_Gen_Output)



