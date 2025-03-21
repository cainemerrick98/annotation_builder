import openai
from app.settings import settings

class LLMAnnotater:
    def __init__(self, system_prompt: str):
        self.model = openai.OpenAI(api_key=settings.LLM_API_KEY)
        self.system_prompt = system_prompt

    #TODO make this async
    def _annotate(self, data: str):
        return self.model.chat.completions.create(
            model=settings.LLM_MODEL,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": data}
            ]
        ).choices[0].message.content
    
    #TODO make this async
    def batch_annotate(self, data: list[str]):
        return [self._annotate(row) for row in data]
        

