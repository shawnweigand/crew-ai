from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI, AzureChatOpenAI

from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

import os
from dotenv import load_dotenv
load_dotenv()

class TravelAgents:
    def __init__(self):
        self.AzureOpenAIGPT4 = AzureChatOpenAI(
            azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
            azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
            api_key=os.environ.get("AZURE_OPENAI_KEY"),
            api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),
        )
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        # self.Ollama = Ollama(model="openhermes")

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(
            f"""
                Expert at analyzing travel data to pick ideal destinations
            """),
            goal=dedent(
            f"""
                Select the best cities based on weather, season, prices, and traveler interests
            """),
            tools=[
                SearchTools.search_internet, 
            ],            
            allow_delegation=True,
            verbose=True,
            llm=self.AzureOpenAIGPT4,
            # max_iter=3
        )
    
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(
            f"""
                Knowledgable local guide with extensive information about the city, it's attractions and customs
            """),
            goal=dedent(
            f"""
                Provide the BEST insights about the selected city
            """),
            tools=[
                SearchTools.search_internet, 
            ],            
            allow_delegation=True,
            verbose=True,
            llm=self.AzureOpenAIGPT4,
            # max_iter=3
        )
    
    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(
            f"""
                Expert in travel planning and logistics.
                I have decades of experience making travel itineraries.
            """),
            goal=dedent(
            f"""
                Create a 7-day travel itinerary with detailed per-day plans,
                include budget, packing suggestions, and safety tips
            """),
            tools=[
                SearchTools.search_internet, 
                CalculatorTools.calculate
            ],
            allow_delegation=True,
            verbose=True,
            llm=self.AzureOpenAIGPT4,
            # max_iter=3
        )
