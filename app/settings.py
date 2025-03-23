import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    ACCEPTED_FILE_TYPES = ["application/vnd.ms-excel", "text/csv"]
    ACCEPTED_FILE_EXTENSIONS = [".csv"]
    MAX_FILE_SIZE = 10 * 1024 * 1024 # 10MB
    LLM_MODEL = "gpt-4o-mini"
    LLM_API_KEY = os.getenv("OPENAI_API_KEY")
    UPLOAD_FOLDER = "uploads" #for dev purposes only 
    TEST_DATA_FOLDER = "tests/test_data"
    ANNOTATED_FOLDER = "annotated_data" #for dev purposes only

settings = Settings()

