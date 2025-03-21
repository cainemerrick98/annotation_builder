# Define sentiment categories
SENTIMENT_CATEGORIES = ["Positive", "Neutral", "Negative"]

# Define examples with annotations and rationales
EXAMPLES = [
    {
        "example": "Your product is amazing! Just wanted to say thank you for the great customer service.",
        "annotation": "Positive",
        "rationale": "The customer is explicitly expressing satisfaction and gratitude, using positive words like \"amazing\" and \"thank you\"."
    },
    {
        "example": "I ordered the wrong size. How do I exchange it for a different one?",
        "annotation": "Neutral",
        "rationale": "The customer is simply asking for information about an exchange process. There's no expression of dissatisfaction or satisfaction."
    },
    {
        "example": "I've been waiting for my refund for over 2 weeks now. When will I receive it?",
        "annotation": "Negative",
        "rationale": "The customer is expressing frustration about a delayed refund, indicating dissatisfaction with the service timeline."
    },
    {
        "example": "I love your company's commitment to sustainability. Keep up the good work!",
        "annotation": "Positive",
        "rationale": "The customer is expressing admiration and encouragement, using positive language like \"love\" and \"good work\"."
    },
    {
        "example": "The item I received is damaged. I want a replacement immediately.",
        "annotation": "Negative",
        "rationale": "The customer is reporting a problem (damaged item) and using demanding language (\"immediately\"), indicating frustration."
    }
]
