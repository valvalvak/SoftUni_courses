from collections import deque

from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    astronaut_types = ("Biologist", "Geodesist", "Meteorologist")

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions_count = 0
        self.unsuccessful_missions_count = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type == "Biologist":
            bio = Biologist(name)
            if self.astronaut_repository.find_by_name(name):
                return f"{name} is already added."
            self.astronaut_repository.add(bio)
            return f"Successfully added {astronaut_type}: {name}."

        elif astronaut_type == "Geodesist":
            geo = Geodesist(name)
            if self.astronaut_repository.find_by_name(name):
                return f"{name} is already added."
            self.astronaut_repository.add(geo)
            return f"Successfully added {astronaut_type}: {name}."

        elif astronaut_type == "Meteorologist":
            met = Geodesist(name)
            if self.astronaut_repository.find_by_name(name):
                return f"{name} is already added."
            self.astronaut_repository.add(met)
            return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        planet = Planet(name, items.split(", "))
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        retired_astronaut = self.astronaut_repository.find_by_name(name)
        if retired_astronaut is None:
            return f"Astronaut {name} doesn't exists!"
        self.astronaut_repository.remove(retired_astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        if not self.planet_repository.find_by_name(planet_name):
            raise Exception("Invalid planet name!")
        astronauts_on_mission = deque()
        for astronaut in sorted(self.astronaut_repository.astronauts, key=lambda x: x.oxygen, reverse=True):
            if astronaut.oxygen >= 30 and len(astronauts_on_mission) < 6:
                astronauts_on_mission.append(astronaut)
            else:
                break
        if not len(astronauts_on_mission) > 0:
            raise Exception("You need at least one astronaut to explore the planet!")
        astronauts_count = len(astronauts_on_mission)
        current_astronaut = astronauts_on_mission.popleft()
        planet = self.planet_repository.find_by_name(planet_name)
        while planet.items:
            item = planet.items.pop()
            current_astronaut.breathe()
            current_astronaut.backpack.append(item)
            if current_astronaut.oxygen <= 0:
                if not astronauts_on_mission:
                    self.unsuccessful_missions_count += 1
                    return "Mission is not completed."
                astronauts_on_mission.popleft()
            self.successful_missions_count += 1
        return f"Planet: {planet} was explored. {astronauts_count} astronauts participated in collecting items."

    def report(self):
        result = f"{self.successful_missions_count} successful missions!\n"
        result += f"{self.unsuccessful_missions_count} missions were not completed!\n"
        for astronaut in self.astronaut_repository.astronauts:
            result += f"Astronauts' info:\nName: {astronaut.name}\nOxygen: {astronaut.oxygen}\n"
            if len(astronaut.backpack) > 0:
                result += f"Backpack items: {', '.join([item for item in astronaut.backpack])}\n"
            else:
                result += 'Backpack items: "none"\n'
        return result
