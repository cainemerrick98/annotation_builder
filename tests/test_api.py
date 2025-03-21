import unittest
from fastapi import FastAPI
from app.api import app
from fastapi.testclient import TestClient
import os

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)


    def test_upload_file(self):
        response = self.client.post("/upload", files={"file": ("test.csv", b"id,text\n1,hello\n2,world")})
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "File uploaded successfully"})
        self.assertTrue(os.path.exists("uploads/test.csv"))


