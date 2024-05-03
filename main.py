import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI, AzureChatOpenAI
# from decouple import config

from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks

from dotenv import load_dotenv
load_dotenv()

# DuckDuckGo search tool
# !pip install -U duckduckgo-search
# from langchain.tools import DuckDuckGoSearchRun
# search_tool = DuckDuckGoSearchRun()

# os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
# os.environ["OPENAI_ORGANIZATION"] = config("OPENAI_ORGANIZATION_ID")

class TripCrew:
    def __init__(self, origin, cities, travel_dates, interests):
        self.origin = origin
        self.cities = cities
        self.travel_dates = travel_dates
        self.interests = interests
        # self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        # self.AzureOpenAIGPT4 = AzureChatOpenAI(
        #     azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
        #     azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
        #     api_key=os.environ.get("AZURE_OPENAI_KEY"),
        #     api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),
        # )

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents =TravelAgents()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()

        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.travel_dates,
            self.interests
        )

        identify_city = tasks.identify_city(
            city_selection_expert,
            self.origin,
            self.cities,
            self.interests,
            self.travel_dates
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.cities,
            self.travel_dates,
            self.interests
        )

        # Define your custom crew here
        crew = Crew(
            agents=[
                expert_travel_agent, 
                city_selection_expert, 
                local_tour_guide
            ],
            tasks=[
                plan_itinerary, 
                identify_city, 
                gather_city_info
            ],
            # process = Process.hierarchical,
            # manager_llm = self.OpenAIGPT35,
            verbose = True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Trip Planner Crew")
    print("-------------------------------")
    origin = input(dedent(
        """
            Where will you be traveling from?
        """))
    cities = input(dedent(
        """
            What are the city options you are interested in visiting?
        """))
    travel_dates = input(dedent(
        """
            What is the date range you are interested in traveling?
        """))
    interests = input(dedent(
        """
            What are some of your high level interests and hobbies?
        """))

    trip_crew = TripCrew(origin, cities, travel_dates, interests)
    result = trip_crew.run()
    print("\n\n########################")
    print("## Here is your trip plan:")
    print("########################\n")
    print(result)
