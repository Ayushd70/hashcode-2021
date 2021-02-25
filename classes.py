class intersection:
    def __init__(self, number, roads):
        self.number = number
        # Roads objects
        self.roads = roads
        self.cycleIsCompleted = False
        # [(road, seconds)]
        self.cycle = []
        self.currTime = 0
        # {roads: [cars]}
        self.roadcars = {}
        self.currGreen = None

    def checkCycle(self):
        if len(self.cycle == len(self.roads)):
            self.cycleIsCompleted = True

    def getSmallestWeight(self):
        if self.checkCycle():
            return
        rWeight = None
        rName = None
        seconds = 0
        for road, cars in self.roadcars.items():
            # Already added to cycle
            if road in self.cycle:
                continue
            # Smallest otherwise
            smallest = min([c.weight for c in cars])
            seconds = cars.index(smallest) + 1
            if not rWeight or smallest < rWeight:
                rWeight = smallest
                rName = road
        # Add this to cycle
        self.cycle.append((rName, seconds))
        self.checkCycle()


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

    def move(self, time):
        self.currRoad = self.roadsLeft.pop(0)
        self.currTime += time

    def wait(self, time):
        self.currTime += time

    def calculateWeight(self):
        self.weight = sum([r.time for r in roadsLeft])