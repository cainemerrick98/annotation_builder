import unittest
from unittest.mock import patch
from app.llm_annotater import LLMAnnotater
from app.prompts import ANNOTATE_WITH_EXPLANATION
from tests.fake_prompt_info import EXAMPLES, SENTIMENT_CATEGORIES
from app.settings import settings
from openai import OpenAI
from app.files import load_file_to_dataframe
import json 
import logging

logging.basicConfig(level=logging.WARN)

class TestLLMAnnotater(unittest.TestCase):
    def setUp(self):
        self.data = load_file_to_dataframe("test_data", use_test_folder=True)
        prompt = ANNOTATE_WITH_EXPLANATION.format(
            criteria=SENTIMENT_CATEGORIES,
            examples=EXAMPLES
        )
        self.annotater = LLMAnnotater(prompt)
        logging.warning("this test uses the api and costs money")

    def test_model_loaded(self):
        self.assertIsInstance(self.annotater.model, OpenAI)
    
    def test_system_prompt_loaded(self):
        self.assertEqual(self.annotater.system_prompt, ANNOTATE_WITH_EXPLANATION.format(
            criteria=SENTIMENT_CATEGORIES,
            examples=EXAMPLES
        ))

    def test_annotate_data(self):
        row = json.dumps(self.data.iloc[0].to_dict())
        self.assertIsInstance(row, str)
        result = self.annotater._annotate(row)
        result = json.loads(result)
        self.assertIsInstance(result, dict)
        self.assertIn("annotation", result)
        self.assertIn("rationale", result)

    # def test_batch_annotate(self):
    #     rows = [json.dumps(row) for row in self.data.to_dict(orient="records")]
    #     result = self.annotater.batch_annotate(rows)
    #     result = [json.loads(row) for row in result]
    #     self.assertIsInstance(result, list)
    #     self.assertIsInstance(result[0], dict)
    #     self.assertIn("annotation", result[0])
    #     self.assertIn("rationale", result[0])


