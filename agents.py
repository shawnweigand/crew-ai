from crewai import Agent
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools
class TravelAgents:

    def editor_agent(self):
        return Agent(
            role="Editor",
            goal="Oversee the creation of the travel plan",
            backstory="""With a keen eye for detail and a need for organization, 
            ensure that the travel plan is instructional for the user, touches on all the user's interests, and gives all necessary logistical information.
            Make sure it aligns with the chosen travel dates and includes budgets, packing suggestions, overnight stays, weather forecasts, and dining options
            regarding the recommended activities.""",
            allow_delegation=True,
            verbose=True,
            max_iter=15
        )
    
    def destination_research_agent(self):
        return Agent(
            role="Destination Researcher",
            goal="Research the best things to do in the selected destination for the user's interests",
            backstory="""With a knack for research and a love for travel, scour the internet for relevant actviites and logistics for the user's trip
            to the chosen destination. Given details about activites that align with their preferences, and logistical information that prepares them for an enjoyable 
            trip without having to plan themselves.""",
            allow_delegation=True,
            verbose=True,
            tools=[SearchTools.search_internet]
        )
    
    def travel_plan_compiler_agent(self):
        return Agent(
            role="Travel Plan Compiler",
            goal="Compile a final comprehensive travel plan for the user's trip",
            backstory="""As the final architect for the travel plan, you meticulously arrange all the details into a comprehensive itinerary for the user's trip.
            Ensure it is coherent and visually easy to follow along for each day. It should be informative, instructional, and include all the necessary details
            such as daily itineraries, activity suggestions, dining options, packing suggestions, budget breakdowns, and weather forecasts. 
            Ensure that the plan is well-structured, informative, and aligned with the user's interests and travel dates.""",
            verbose=True,
            tools=[CalculatorTools.calculate]
        )




# from crewai import Agent
# from textwrap import dedent
# from langchain.llms import OpenAI, Ollama
# from langchain_openai import ChatOpenAI, AzureChatOpenAI

# from tools.search_tools import SearchTools
# from tools.calculator_tools import CalculatorTools

# import os
# from dotenv import load_dotenv
# load_dotenv()

# class TravelAgents:
#     def __init__(self):
#         self.AzureOpenAIGPT4 = AzureChatOpenAI(
#             azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
#             azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
#             api_key=os.environ.get("AZURE_OPENAI_KEY"),
#             api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),
#         )
#         self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
#         # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
#         # self.Ollama = Ollama(model="openhermes")

#     def city_selection_expert(self):
#         return Agent(
#             role="City Selection Expert",
#             backstory=dedent(
#             f"""
#                 Expert at analyzing travel data to pick ideal destinations
#             """),
#             goal=dedent(
#             f"""
#                 Select the best cities based on weather, season, prices, and traveler interests
#             """),
#             tools=[
#                 SearchTools.search_internet, 
#             ],            
#             # allow_delegation=True,
#             verbose=True,
#             # llm=self.AzureOpenAIGPT4,
#             max_iter = 3
#         )
    
#     def local_tour_guide(self):
#         return Agent(
#             role="Local Tour Guide",
#             backstory=dedent(
#             f"""
#                 Knowledgable local guide with extensive information about the city, it's attractions and customs
#             """),
#             goal=dedent(
#             f"""
#                 Provide the BEST insights about the selected city
#             """),
#             tools=[
#                 SearchTools.search_internet, 
#             ],            
#             allow_delegation=True,
#             verbose=True,
#             # llm=self.AzureOpenAIGPT4,
#             max_iter = 3
#         )
    
#     def expert_travel_agent(self):
#         return Agent(
#             role="Expert Travel Agent",
#             backstory=dedent(
#             f"""
#                 Expert in travel planning and logistics.
#                 I have decades of experience making travel itineraries.
#             """),
#             goal=dedent(
#             f"""
#                 Create a 7-day travel itinerary with detailed per-day plans,
#                 include budget, packing suggestions, and safety tips
#             """),
#             tools=[
#                 SearchTools.search_internet, 
#                 CalculatorTools.calculate
#             ],
#             # allow_delegation=True,
#             verbose=True,
#             # llm=self.AzureOpenAIGPT4,
#             max_iter = 3
#         )
