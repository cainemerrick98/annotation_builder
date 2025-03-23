import unittest
from fastapi import FastAPI
from app.api import app
from fastapi.testclient import TestClient
import os
from app.files import load_file_to_dataframe
from tests.fake_prompt_info import EXAMPLES, SENTIMENT_CATEGORIES
import logging

logging.basicConfig(level=logging.WARNING)

logger = logging.getLogger(__name__)

logger.warning("This test uses the actual API it costs money to run")

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.test_data = load_file_to_dataframe("test_data", use_test_folder=True).head(10)

    def tearDown(self):
        for file in os.listdir("uploads"):
            os.remove(os.path.join("uploads", file))
        for file in os.listdir("annotated_data"):
            os.remove(os.path.join("annotated_data", file))

    def test_upload_file(self):
        response = self.client.post("/upload", files={"file": ("test_data.csv", b"id,text\n1,hello\n2,world")})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(os.listdir("uploads")) > 0)

    def test_annotate_file(self):
        upload_response = self.client.post("/upload", files={"file": ("test_data.csv", self.test_data.to_csv(index=False).encode("utf-8"))})
        file_id = upload_response.json()["file_id"]
        response = self.client.post("/annotate", json={
            "file_id": file_id,
            "criteria": SENTIMENT_CATEGORIES,
            "examples": EXAMPLES,
            "explain": True
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(os.listdir("annotated_data")) > 0)

