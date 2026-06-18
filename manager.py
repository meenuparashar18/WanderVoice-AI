from __future__ import annotations
import json
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from agent import FinalTour


load_dotenv()

class TourManager:
 

    def __init__(self) -> None:
        self.client = genai.Client()
        self.text_model = "gemini-2.5-flash"

    def run(self, query: str, interests: list, duration: int, lang_choice: str) -> FinalTour:
       
        prompt = (
            f"You are an expert AI Travel Tour Guide. Create a highly engaging, personalized audio tour.\n\n"
            f"--- TOUR PARAMETERS ---\n"
            f"- Destination/Location: {query}\n"
            f"- User's Interests: {', '.join(interests)}\n"
            f"- Total Duration: {duration} minutes\n"
            f"- Target Language: {lang_choice}\n\n"
            f"--- INSTRUCTIONS ---\n"
            f"1. Create a warm and welcoming introduction paragraph.\n"
            f"2. Conduct deep research and write tailored, conversational content ONLY for the fields requested in the user's interests.\n"
            f"3. For any field/topic NOT present in the user's interests, strictly fill its value as: 'Not requested for this tour.'\n"
            f"4. Structure the text perfectly for an audio guide (no markdown syntax inside the paragraphs, no section headers, just fluid conversational paragraphs).\n"
            f"5. End with a memorable and beautiful conclusion paragraph.\n"
            f"6. Strictly write the ENTIRE response in {lang_choice} language (including fields like introduction and conclusion).\n\n"
            f"Deliver the final output matching the FinalTour Pydantic schema structure perfectly."
        )

        response = self.client.models.generate_content(
            model=self.text_model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=FinalTour,
                temperature=0.5
            ),
        )
        

        return FinalTour.model_validate_json(response.text)