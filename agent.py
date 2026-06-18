import os
from pydantic import BaseModel
from google import genai
from google.genai import types
from dotenv import load_dotenv


load_dotenv()


client = genai.Client()


TEXT_MODEL = "gemini-2.5-flash"
PRO_MODEL = "gemini-2.5-pro"



class Architecture(BaseModel):
    output: str

class Culinary(BaseModel):
    output: str

class Culture(BaseModel):
    output: str

class History(BaseModel):
    output: str

class FinalTour(BaseModel):
    introduction: str
    architecture: str
    history: str
    culture: str
    culinary: str
    conclusion: str

class Planner(BaseModel):
    introduction: float
    architecture: float
    history: float
    culture: float
    culinary: float
    conclusion: float



ARCHITECTURE_AGENT_INSTRUCTIONS = """
You are the Architecture agent for a self-guided audio tour system. Given a location and the areas of interest of user, your role is to:
1. Describe architectural styles, notable buildings, urban planning, and design elements
2. Provide technical insights balanced with accessible explanations
3. Highlight the most visually striking or historically significant structures
4. Adopt a detailed, descriptive voice style when delivering architectural content
5. Make sure not to add any headings like ## Architecture. Just provide the content
6. Make sure the details are conversational and don't include any formatting or headings. It will be directly used in a audio model for converting to speech and the entire content should feel like natural speech.
7. Make sure the content is strictly between the upper and lower Word Limit as specified. For example, If the word limit is 100 to 120, it should be within that, not less than 100 or greater than 120
NOTE: Do not add any Links or Hyperlinks in your answer or never cite any source
Help users see and appreciate architectural details they might otherwise miss. Make it as detailed and elaborative as possible
"""

CULINARY_AGENT_INSTRUCTIONS = """
You are the Culinary agent for a self-guided audio tour system. Given a location and the areas of interest of user, your role is to:
1. Highlight local food specialties, restaurants, markets, and culinary traditions in the user's location
2. Explain the historical and cultural significance of local dishes and ingredients
3. Suggest food stops suitable for the tour duration
4. Adopt an enthusiastic, passionate voice style when delivering culinary content
5. Make sure not to add any headings like ## Culinary. Just provide the content
6. Make sure the details are conversational and don't include any formatting or headings. It will be directly used in a audio model for converting to speech and the entire content should feel like natural speech.
7. Make sure the content is strictly between the upper and lower Word Limit as specified. For example, If the word limit is 100 to 120, it should be within that, not less than 100 or greater than 120
NOTE: Do not add any Links or Hyperlinks in your answer or never cite any source
Make your descriptions vivid and appetizing. Include practical information like operating hours when relevant. Make it as detailed and elaborative as possible
"""

CULTURE_AGENT_INSTRUCTIONS = """
You are the Culture agent for a self-guided audio tour system. Given a location and the areas of interest of user, your role is to:
1. Provide information about local traditions, customs, arts, music, and cultural practices
2. Highlight cultural venues and events relevant to the user's interests
3. Explain cultural nuances and significance that enhance the visitor's understanding
4. Adopt a warm, respectful voice style when delivering cultural content
5. Make sure not to add any headings like ## Culture. Just provide the content
6. Make sure the details are conversational and don't include any formatting or headings. It will be directly used in a audio model for converting to speech and the entire content should feel like natural speech.
7. Make sure the content is strictly between the upper and lower Word Limit as specified. For example, If the word limit is 100 to 120, it should be within that, not less than 100 or greater than 120
NOTE: Do not add any Links or Hyperlinks in your answer or never cite any source
Focus on authentic cultural insights that help users appreciate local ways of life. Make it as detailed and elaborative as possible
"""

HISTORY_AGENT_INSTRUCTIONS = """
You are the History agent for a self-guided audio tour system. Given a location and the areas of interest of user, your role is to:
1. Provide historically accurate information about landmarks, events, and people related to the user's location
2. Prioritize the most significant historical aspects based on the user's time constraints
3. Include interesting historical facts and stories that aren't commonly known
4. Adopt an authoritative, professorial voice style when delivering historical content
5. Make sure not to add any headings like ## History. Just provide the content
6. Make sure the details are conversational and don't include any formatting or headings. It will be directly used in a audio model for converting to speech and the entire content should feel like natural speech.
7. Make sure the content is strictly between the upper and lower Word Limit as specified. For example, If the word limit is 100 to 120, it should be within that, not less than 100 or greater than 120
NOTE: Do not add any Links or Hyperlinks in your answer or never cite any source
Focus on making history come alive through engaging narratives. Keep descriptions concise but informative. Make it as detailed and elaborative as possible
"""

ORCHESTRATOR_INSTRUCTIONS = """
You are the Orchestrator Agent for a self-guided audio tour system. Your task is to assemble a comprehensive and engaging tour for a single location by integrating pre-timed content from four specialist agents (Architecture, History, Culinary, and Culture), while adding introduction and conclusion elements.
Follow the steps perfectly and return the structured output as requested. Ensure transitions are smooth and everything sounds like natural conversational speech.
"""

PLANNER_INSTRUCTIONS = """
You are the Planner Agent for a self-guided tour system. Your primary responsibility is to analyze the user's location, interests, and requested tour duration to create an optimal time allocation plan for content generation by specialist agents (Architecture, History, Culture, and Culinary).
Only return the number of minutes allocated to each section inside the structured JSON schema.
"""



def run_planner_agent(location: str, interests: str, duration: int) -> Planner:
  
    prompt = f"Calculate time allocation for Location: {location}, Interests: {interests}, Duration: {duration} minutes."
    
    response = client.models.generate_content(
        model=PRO_MODEL, 
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=PLANNER_INSTRUCTIONS,
            response_mime_type="application/json",
            response_schema=Planner,
            temperature=0.2
        ),
    )
   
    return Planner.model_validate_json(response.text)


def run_specialist_agent(agent_name: str, instructions: str, output_schema, location: str, interests: str, word_limit: str):
   
    
    prompt = f"Generate content for Location: {location}. User Interests: {interests}. Required Word Limit: {word_limit}."
    
    response = client.models.generate_content(
        model=TEXT_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=instructions,
            tools=[{"google_search": {}}],
            response_mime_type="application/json",
            response_schema=output_schema,
            temperature=0.7
        ),
    )
    return output_schema.model_validate_json(response.text)


def run_orchestrator_agent(location: str, interests: str, arch_out: str, hist_out: str, cult_out: str, cul_out: str) -> FinalTour:
    
    prompt = f"""
    Location: {location}
    Interests: {interests}
    
    Integrate these contents into a single final flow:
    Architecture Content: {arch_out}
    History Content: {hist_out}
    Culture Content: {cult_out}
    Culinary Content: {cul_out}
    """
    
    response = client.models.generate_content(
        model=TEXT_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=ORCHESTRATOR_INSTRUCTIONS,
            response_mime_type="application/json",
            response_schema=FinalTour,
            temperature=0.5
        ),
    )
    return FinalTour.model_validate_json(response.text)