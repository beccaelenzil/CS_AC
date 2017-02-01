import pygame
import random

from building import Building
from person import Person

class Scene():
    def __init__(self, width, height, screen, building_props):
        self.buildings = []
        self.width = width
        self.height = height
        self.screen = screen
        self.building_props = building_props
        x = width
        while x > 100:
            building = self.create_building()
            building.move(x)
            building.draw(screen)
            x -= random.randint(building.width+10, building.width+50)

    def next_tick(self):
        for building in self.buildings:
            building.move()
            if self.building_is_off_screen(building):
                self.remove_building(building)
            else:
                building.draw(self.screen)
        if self.can_new_building_be_created():
            self.create_building()


    #building directions

    def can_new_building_be_created(self):
        most_recent_building = self.buildings[-1]
        if self.building_is_on_screen(most_recent_building):
            return True
        else:
            return False

    def create_building(self):
        num_buildings = len(self.building_props)
        building_props_index = random.randint(0, num_buildings - 1)
        props = self.building_props[building_props_index]
        building = Building(props['width'] + random.randint(25,75), props['height'], props['image'])
        self.buildings.append(building)
        return building

    def remove_building(self, building):
        self.buildings.remove(building)

    def building_is_on_screen(self, building):
        if building.x<700 - building.width:
            return True
        else:
            return False

    def building_is_off_screen(self, building):
        if building.x< 0 - self.width:
            return True
        else:
            return False

    #person directions

    def create_person(self):
        props = self.building_props[0]
        person = Person(0, props['height'], props['image'])
        return person




