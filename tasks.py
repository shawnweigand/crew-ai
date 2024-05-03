from crewai import Task
from textwrap import dedent

class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
                    **Task**: Develop a 7-Day Travel Itinerary
                    **Description**: Expand the city guide into a full 7-day travel itinerary with detailed
                        per-day plans, including weather forecasts, places to eat, packing suggestions, and
                        a budget breakdown. You MUST suggest actual places to visit, actual hotels to stay,
                        and actual restaurants to go to. This itinerary should cover all aspects of the trip,
                        from arrival to departure, integrating the city guide information with practical 
                        tracel logistics.

                    **Parameters**:
                    - City: {city}
                    - Trip Date: {travel_dates}
                    - Traveler Interests: {interests}

                    **Note**: {self.__tip_section()}
                """
            ),
            # expected_output="what it is and example of what it should look like",
            agent=agent,
            # context=[identify_city, gather_city_info],
            # callback=print OR email OR CSV
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
                    **Task**: Identify the Best City for the Trip
                    **Description**: Analyze and select the best city for the trip based on specific criteria
                        such as weather patterns, seasonal events, and travel costs. This task involves 
                        comparing multiple cities, considering factors like current weather conditions, 
                        upcoming cultural orseasonal events, and overall trcael expenses. Your final answer 
                        must be a detailed report on the chosen city, including actual flight costs, weather
                        forecast, and attractions.

                    **Parameters**:
                    - Origin: {origin}
                    - Cities: {cities}
                    - Traveler Interests: {interests}
                    - Travel Dates: {travel_dates}

                    **Note**: {self.__tip_section()} 
                """
            ),
            # expected_output="what it is and example of what it should look like",
            agent=agent,
            # async_execution=True
            # callback=print OR email OR CSV
        )

    def gather_city_info(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
                    **Task**: Gather In-depth City Guide Information
                    **Description**: Compile an in-depth guide for the selected city, gathering information
                        about key attractions, local customs, special events, and daily activity recommendations.
                        This guide should provide a thorough overview of what the city has to offer, including 
                        hidden gems, cultural hotspots, must-visit landmarks, weather forecasts, and high-level
                        costs.

                    **Parameters**:
                    - City: {city}
                    - Traveler Interests: {interests}
                    - Travel Dates: {travel_dates}

                    **Note**: {self.__tip_section()} 
                """
            ),
            # expected_output="what it is and example of what it should look like",
            agent=agent,
            # async_execution=True
            # callback=print OR email OR CSV
        )
