import pandas as pd
from app.prompts import ANNOTATE_WITH_EXPLANATION, ANNOTATE_WITHOUT_EXPLANATION
from app.llm_annotater import LLMAnnotater
import json

class AnnotationBuilder:
    def __init__(self, data: pd.DataFrame, criteria: str, examples: list[dict], explain:bool):
        self.data = data
        self.criteria = criteria
        self.explain = explain
        self.examples = self._format_examples(examples)
        self.prompt = self._insert_data_into_prompt(ANNOTATE_WITH_EXPLANATION) if explain else self.insert_data_into_prompt(ANNOTATE_WITHOUT_EXPLANATION)

    def _format_examples(self, examples: list[dict]):
        examples_str = ""
        for i, example in enumerate(examples):
            examples_str += f"Example {i+1}: {example['example']}\nAnnotation: {example['annotation']}\n"
            if self.explain:
                examples_str += f"Rationale: {example['rationale']}\n"
        return examples_str
    
    def _insert_data_into_prompt(self, prompt: str):
        return prompt.format(
            criteria=self.criteria,
            examples=self.examples,
        )

    def annotate_data(self):
        llm_annotater = LLMAnnotater(self.prompt)
        if self.explain:
            result = llm_annotater.batch_annotate([json.dumps(row) for row in self.data.to_dict(orient="records")])
            parsed_result = [json.loads(row) for row in result]
            annotations = [row["annotation"] for row in parsed_result]
            rationales = [row["rationale"] for row in parsed_result]
            self.data[["annotation", "rationale"]] = list(zip(annotations, rationales))
        else:
            result = llm_annotater.batch_annotate([json.dumps(row) for row in self.data.to_dict(orient="records")])
            annotations = [json.loads(row)["annotation"] for row in result]
            self.data["annotation"] = annotations
        return self.data


    


