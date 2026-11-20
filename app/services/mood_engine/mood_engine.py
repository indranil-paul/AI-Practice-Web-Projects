from openai import OpenAI
from app.services.mood_engine.mood_engine_models import Mood, MoodResponse
# from app.exceptions.handlers import MoodClassificationException
from app.utils.logger import logger


PROMPT_FOR_MOOD_DETECTION = f"""
    [ ROLE ]: You are a strict mood classifier.

    [ ACTION ]: Read and analyze the entire text carefully and correctly determine 
    its single most dominant mood.

    [ CONTEXT ]: The text may contain various mental states, sentiments or emotions, 
    but you must identify the most prominent one.
    Concentrate on the tone, intent, wording, and overall meaning.
    Here are the available moods for your reference: {", ".join(m.value for m in Mood)}

    [ EXECUTE ]:
        Rules:
            - Select EXACTLY ONE mood from the available moods.
            - Do not assume positive or negative sentiment.
            - Base your decision only on the tone and meaning of the text.
            - If multiple moods are present, choose the strongest one.
            - If the mood is unclear, choose "neutral".
            - If you found a mood outside the allowed list, choose "confused".

        Response Format: Return the response strictly in the provided response_format.
"""


class MoodClassifier:
    """
    Classifies the dominant mood of a given text using
    OpenAI's structured output (beta parse) API.
    """

    def __init__(self, client: OpenAI, model: str, temperature: float = 0.0):
        self.client = client
        self.model = model
        self.temperature = temperature

    def get_mood(self, text: str) -> Mood:
        """
        Classify the dominant mood of the provided text.
        Falls back to Mood.CONFUSED on any failure.
        """
        try:
            completion = self.client.beta.chat.completions.parse(
                model=self.model,
                messages=[
                    {"role": "system", "content": PROMPT_FOR_MOOD_DETECTION},
                    {"role": "user",   "content": text},
                ],
                response_format=MoodResponse,
                temperature=self.temperature,
            )
            parsed = completion.choices[0].message.parsed
            if not parsed:
                logger.warning("Mood classification returned empty response, defaulting to CONFUSED.")
                return Mood.CONFUSED

            logger.debug(f"Mood classified as: {parsed.mood.value}")
            return parsed.mood

        except Exception as e:
            logger.error(f"Mood classification failed: {e}")
            # raise MoodClassificationException(detail=str(e))
            raise e
