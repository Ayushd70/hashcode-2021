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
        print(self.path)
        print(self.times)

    def stopLight(self, timeStopped):

        self.minTime += timeStopped
