import pygame
import random
pygame.init()

from building import Building
from person import Person

#building properties

# widths:
width1 = 50
width2 = 75
width3 = 100
width4 = 125

# heights:
height1 = 100
height2 = 150
height3 = 175
height4 = 225
height5 = 250

#potential next heights:
height_transitions = {
    height1: [height1, height2, height3],
    height2: [height1, height2, height3, height4],
    height3: [height1, height2, height3, height4, height5],
    height4: [height2, height3, height4, height5],
    height5: [height3, height4, height5],
}

#potential buildings
def calc_building_props():
    building_props = [
        #{ 'width': width1, 'height': height1, 'image': pygame.image.load("images/50x100.png").convert() },
        { 'width': width4, 'height': height1, 'image': pygame.image.load("images/125x150.png").convert() },
        { 'width': width2, 'height': height2, 'image': pygame.image.load("images/75x150.png").convert() },
        { 'width': width3, 'height': height3, 'image': pygame.image.load("images/100x175.png").convert() },
        { 'width': width2, 'height': height4, 'image': pygame.image.load("images/75x225.png").convert() },
        { 'width': width3, 'height': height5, 'image': pygame.image.load("images/100x250.png").convert() },
    ]
    return building_props

class Scene():
    def __init__(self, width, height, screen):
        self.buildings = []
        self.width = width
        self.height = height
        self.screen = screen
        self.building_props = calc_building_props()
        self.last_height = height3
        self.person = Person()
        self.dt = 0

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
        self.person.draw(self.screen)
        self.person.update_position()
        self.dt += 1

    #building directions

    def can_new_building_be_created(self):
        most_recent_building = self.buildings[-1]
        if self.building_is_on_screen(most_recent_building):
            return True
        else:
            return False

    def create_building(self):
        #get legal transition heights for last height:
        legal_heights = height_transitions[self.last_height]

        #get buildings with legal heights:
        legal_building_props = [bp for bp in self.building_props if bp['height'] in legal_heights]
        num_buildings = len(legal_building_props)
        building_props_index = random.randint(0, num_buildings - 1)
        props = legal_building_props[building_props_index]
        building = Building(props['width'] + random.randint(25,75), props['height'], props['image'])
        self.buildings.append(building)
        self.last_height = building.height
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


