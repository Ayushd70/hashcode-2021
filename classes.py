class intersection:
    def __init__(self, number, roads):
        self.number = number
        # Roads objects
        self.roads = roads
        self.cycleIsCompleted = False
        # [(road, seconds)]
        self.cycle = []
        self.currTime = 0
        self.roadcars = {}
        self.currGreen = None

    def checkCycle(self):
        if len(self.cycle == len(self.roads)):
            self.cycleIsCompleted = True


class road:
    def __init__(self, intersections, name, time):
        self.intersections = intersections
        self.name = name
        self.time = time


class car:
    # Pass in index of paths array as parameter
    def __init__(self, road):
        self.currTime = 0
        self.weight = 0
        # Roads objects
        self.roadsLeft = road[1:]
        self.currRoad = road[0]

    def move(self):
        self.currRoad = roadsLeft.pop(0)
        self.currTime += time

    def wait(time):
        self.currTime += time

    def calculateWeight(self):
        self.weight = sum([r.time for r in roadsLeft])
