import unittest
from app.annotation_builder import AnnotationBuilder
import pandas as pd
from app.files import load_file_to_dataframe
from app.prompts import ANNOTATE_WITH_EXPLANATION, ANNOTATE_WITHOUT_EXPLANATION
from tests.fake_prompt_info import EXAMPLES, SENTIMENT_CATEGORIES
import logging

logging.basicConfig(level=logging.WARN)

class TestAnnotationBuilder(unittest.TestCase):
    
    def setUp(self):
        self.data = load_file_to_dataframe("test_data", use_test_folder=True).head(3)
        self.builder = AnnotationBuilder(
            self.data, 
            SENTIMENT_CATEGORIES, 
            EXAMPLES,
            True
        )
        logging.warning("this test uses the api and costs money")

    def test_format_examples(self):
        formatted_examples = self.builder._format_examples(EXAMPLES)
        self.assertEqual(self.builder.examples, formatted_examples)

    def test_insert_data_into_prompt(self):
        prompt = ANNOTATE_WITH_EXPLANATION.format(
            criteria=self.builder.criteria,
            examples=self.builder.examples,
        )
        self.assertEqual(self.builder.prompt, prompt)

    def test_annotate_data(self):
        annotated_data = self.builder.annotate_data()
        self.assertIn("annotation", annotated_data.columns)
        self.assertIn("rationale", annotated_data.columns)
        self.assertEqual(len(annotated_data), len(self.data))
        print(annotated_data[['annotation', 'rationale']])

