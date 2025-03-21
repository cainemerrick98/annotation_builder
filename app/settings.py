import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    ACCEPTED_FILE_EXTENSIONS = [".xlsx", ".csv"]
    MAX_FILE_SIZE = 10 * 1024 * 1024 # 10MB
    LLM_MODEL = "gpt-4o-mini"
    LLM_API_KEY = os.getenv("OPENAI_API_KEY")
    UPLOAD_FOLDER = "uploads" #for dev purposes only 
    TEST_DATA_FOLDER = "tests/test_data"

settings = Settings()

