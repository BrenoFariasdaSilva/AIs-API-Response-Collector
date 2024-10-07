import google.generativeai as genai # Import the Google AI Python SDK

class GeminiModel:
	"""
	A class to interact with the Google Gemini AI model.

	"""

	def __init__(self): # Constructor
		self.api_key = None # The API key
		self.model = None # The AI model
