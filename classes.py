class intersection:
    def __init__(self, roads, cars, gLight):
        self.roads = roads
        self.cars = cars
        self.gLight = gLight

    # def determineLight():


class road:
    def __init__(self, cars):
        self.cars = cars


class car:
    # Pass in index of paths array as parameter
    def __init__(self, path, streets):
        self.path = path[1:]
        self.times = [0]

        for p in range(1, len(self.path)):
            for s in streets:
                if self.path[p] == s[2]:
                    self.times.append(self.times[p - 1] + s[3])

    def currRoad(self, simTime):
        for t in range(len(self.times)):
            if self.times[t] >= simTime:
                return self.path[t]

    def atIntersection(self, simTime):
        if simTime in self.times:
            return self.currRoad(simTime)
        else:
            return False

    def stopped(self, simTime):
        i = self.times.index(simTime)

        for t in range(i, len(self.times)):
            self.times[t] += 1
