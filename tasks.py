from crewai import Task

class TravelTasks():
    def research_destination_task(self, agent):
        return Task(
            description="""Compile an in-depth guide for the selected city during the travel dates, gathering information about key attractions, 
            local customs, special events, and daily activity recommendations. This guide should align with the travelers interests and provide a thorough
            overview of what the city has to offer, including hidden gems, cultural hotspots, must-visit landmarks, weather forecasts, and high-level costs.""",
            agent=agent,
            async_execution=True,
            expected_output="""A detailed report on the chosen city, including actual flight costs, weather forecast, events and attractions.
            Example output:
            {
                'City': 'Paris',
                'Flight Cost': '$500',
                'Weather Forecast': 'Sunny with a chance of rain',
                'Events': ['Bastille Day Parade', 'Fashion Week'],
                'Attractions': ['Eiffel Tower', 'Louvre Museum']
            }"""
        )
    
    def compile_travel_plan_task(self, agent, context):
        return Task(
            description="""Expand the city guide for the selected city into a full multi-day travel itinerary during the chosen travel dates with detailed 
            per-day plans, including weather forecasts, places to eat, packing suggestions, and a budget breakdown that are relevant to the travelers interests. 
            You MUST suggest actual places to visit, actual hotels to stay, and actual restaurants to go to. This itinerary should  cover all aspects of the 
            trip, from arrival to departure, integrating the city guide information with practical travel logistics.""",
            agent=agent,
            async_execution=True,
            context=context,
            expected_output="""A detailed 7-day travel itinerary with per-day plans, including weather forecasts, places to eat, packing suggestions, and a 
            budget breakdown.
            Example output:
            [
                {
                    'Budget': {'Total': '$500', 'Hotel': '$100', 'Meals': '$150', 'Activities': '$250'},
                    'Weather Forecast': 'Sunny with a chance of rain',
                    'Safety Tips': ['Beware of pickpockets', 'Use a money belt'],
                    'Packing Suggestions': ['Comfortable shoes', 'Light jacket'],
                },
                {
                    'Day': 'Day 1',
                    'Date': '2022-07-01',
                    'Description': 'Arrival in Paris',
                    'Activities': ['Visit Eiffel Tower', 'Lunch at Café de Flore', 'Dinner at Le Jules Verne'],
                    'Hotel': 'Hotel Ritz Paris',
                    'Meals': {'Breakfast': { 'Location': 'Hotel', 'Cost': '$20' }, 'Lunch': { 'Location': 'Café de Flore', 'Cost': '$30' }, 'Dinner': { 'Location': 'Le Jules Verne', 'Cost': '$100' }},
                    'Pack': ['Comfortable shoes', 'Light jacket'],
                    'Budget': '$500'
                },
                {{...}}
            ]"""
        )
    
    def edit_travel_plan_task(self, agent, context, callback_function):
        return Task(
            description="""Edit the travel itinerary into a readable and informative markdown format that can be easily shared with the traveler.
            Include all the details provided in the itinerary, such as daily activities, accommodation options, restaurant recommendations, 
            weather forecasts and budget breakdown.""",
            agent=agent,
            context=context,
            expected_output="""An updated and finalized travel itinerary that reflects the traveler's preferences and needs, with adjustments made to the daily 
            activities, accommodation options, restaurant recommendations, and budget breakdown. The final plan should be customized to the traveler's expectations 
            and provide a seamless and enjoyable experience.
            Example output:
            '# Travel Itinerary for Paris Trip:\\n\\n'

            ##Overview:\\n\\n
            **Description:** This travel itinerary will guide you through a 7-day trip to Paris, France, from July 1st to July 7th. The primary focus of this trip is
            to explore the rich history, culture, and cuisine of Paris.\\n\\n
            **Budget:** The total budget for this trip is $1000, with a breakdown of $300 for accommodation, $200 for meals, and $500 for activities.\\n\\n
            **Weather Forecast:** The weather in Paris during this period is expected to be sunny with a chance of rain.\\n\\n
            **Safety Tips:** Be aware of pickpockets and consider using a money belt to keep your valuables safe.\\n\\n
            **Packing Suggestions:** Make sure to pack comfortable shoes and a light jacket for the trip.\\n\\n

            ##Day 1: Arrival in Paris\\n\\n
            **Date:** July 1st, 2022\\n\\n
            **Description:** Upon arrival in Paris, you will check into the Hotel Ritz Paris and begin your exploration of the city.\\n\\n
            **Activities:** Visit the Eiffel Tower, have lunch at Café de Flore, and enjoy dinner at Le Jules Verne.\\n\\n
            **Hotel:** Hotel Ritz Paris\\n\\n
            **Meals:** Breakfast at the hotel ($20), lunch at Café de Flore ($30), dinner at Le Jules Verne ($100)\\n\\n
            **Packing Suggestions:** Comfortable shoes, light jacket\\n\\n
            **Budget:** $200\\n\\n""",
            callback=callback_function
        )












# from crewai import Task
# from textwrap import dedent

# class TravelTasks:
#     def __tip_section(self):
#         return "If you do your BEST WORK, I'll give you a $10,000 commission!"

#     def identify_city(self, agent, origin, cities, interests, travel_dates):
#         return Task(
#             agent=agent,
#             # async_execution=True,
#             description=dedent(
#                 f"""
#                     Analyze and select the best city for a trip out of {origin} during the dates {travel_dates} based on specific criteria such as 
#                     weather patterns, seasonal and cultural events, travel costs, and attractions. This task involves comparing multiple cities from 
#                     the options: {cities}. Take into account that the traveler's interests are {interests}.

#                     **Note**: {self.__tip_section()} 
#                 """
#             ),
#             expected_output=
#             """
#                 A detailed report on the chosen city, including actual flight costs, weather forecast, events and attractions.

#                 Example output:
#                 {
#                     'City': 'Paris',
#                     'Flight Cost': '$500',
#                     'Weather Forecast': 'Sunny with a chance of rain',
#                     'Events': ['Bastille Day Parade', 'Fashion Week'],
#                     'Attractions': ['Eiffel Tower', 'Louvre Museum']
#                 }
#             """
#         )
    
#     def gather_city_info(self, agent, city, travel_dates, interests):#, context):
#         return Task(
#             agent=agent,
#             async_execution=True,
#             # context=context,
#             description=dedent(
#                 f"""
#                     Compile an in-depth guide for the selected city {city} during {travel_dates}, gathering information about key attractions, local customs, 
#                     special events, and daily activity recommendations. This guide should align with the travelers interests of {interests} and provide a 
#                     thorough overview of what the city has to offer, including hidden gems, cultural hotspots, must-visit landmarks, weather forecasts, and 
#                     high-level costs.

#                     **Note**: {self.__tip_section()} 
#                 """
#             ),
#             expected_output=
#             """
#                 A list of information about the city, including attractions, local customs, events, and daily activity recommendations.
#                 Include a thorough overview of what the city has to offer with hidden gems, cultural hotspots, must-visit landmarks, weather forecasts, and high-level costs.
                
#                 Example output:
#                 {
#                     'City': 'Paris',
#                     'Attractions': ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame Cathedral'],
#                     'Local Customs': ['Kissing on the cheek', 'Bread with every meal'],
#                     'Events': ['Bastille Day Parade', 'Fashion Week'],
#                     'Daily Activities': ['Morning coffee at a local café', 'Afternoon visit to the Louvre']
#                     'Hidden Gems': ['Secret rooftop bar with a view', 'Underground jazz club'],
#                     'Cultural Hotspots': ['Local art galleries', 'Historical theaters'],
#                     'Landmarks': ['Eiffel Tower', 'Arc de Triomphe'],
#                     'Weather Forecast': 'Sunny with a chance of rain',
#                     'Costs': {'Average Hotel': '$150 per night', 'Average Meal': '$20 per person'}
#                 }
#             """
#         )

#     def plan_itinerary(self, agent, context, callback_function):
#         return Task(
#             agent=agent,
#             async_execution=True,
#             context=context,
#             callback=callback_function,
#             description=dedent(
#                 f"""
#                     Expand the city guide for the selected city into a full multi-day travel itinerary during the chosen travel dates with detailed per-day 
#                     plans, including weather forecasts, places to eat, packing suggestions, and a budget breakdown that are relevant to the travelers interests. 
#                     You MUST suggest actual places to visit, actual hotels to stay, and actual restaurants to go to. This itinerary should  cover all aspects of
#                     the trip, from arrival to departure, integrating the city guide information with practical travel logistics.

#                     **Note**: {self.__tip_section()}
#                 """
#             ),
#             expected_output=
#             """
#                 A detailed 7-day travel itinerary with per-day plans, including weather forecasts, places to eat, packing suggestions, and a budget breakdown.

#                 Example output:
#                 [
#                     {
#                         'Budget': {'Total': '$500', 'Hotel': '$100', 'Meals': '$150', 'Activities': '$250'},
#                         'Weather Forecast': 'Sunny with a chance of rain',
#                         'Safety Tips': ['Beware of pickpockets', 'Use a money belt'],
#                         'Packing Suggestions': ['Comfortable shoes', 'Light jacket'],
#                     },
#                     {
#                         'Day': 'Day 1',
#                         'Date': '2022-07-01',
#                         'Description': 'Arrival in Paris',
#                         'Activities': ['Visit Eiffel Tower', 'Lunch at Café de Flore', 'Dinner at Le Jules Verne'],
#                         'Hotel': 'Hotel Ritz Paris',
#                         'Meals': {'Breakfast': { 'Location': 'Hotel', 'Cost': '$20' }, 'Lunch': { 'Location': 'Café de Flore', 'Cost': '$30' }, 'Dinner': { 'Location': 'Le Jules Verne', 'Cost': '$100' }},
#                         'Pack': ['Comfortable shoes', 'Light jacket'],
#                         'Budget': '$500'
#                     },
#                     {{...}}
#                 ]
#             """
#         )
