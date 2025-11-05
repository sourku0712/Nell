from google import genai
from google.genai import types

GEM_API_KEY = "AIzaSyDlek-WWKK0DWDiJutmfVjN-KPU58haujw"

# ===== AI PROCESS ======
def aiProcess(command):
    # Configure the client
    client = genai.Client(api_key=GEM_API_KEY)
    # Define the grounding tool
    grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
    )
    # Configure generation settings
    config = types.GenerateContentConfig(
    tools=[grounding_tool],
    thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    )
    # Make the request
    response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents= command,
    config= config,
    )
    # Print the response
    return(response.text)