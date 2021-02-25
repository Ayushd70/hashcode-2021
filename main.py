from classes import car, road, intersection

def parseData(inputFile):
    '''
    Returns a tuple: 
    ((D, I, F), streets, paths)
    '''

    # Read lines
    with open(inputFile, 'r') as f:
        data = f.readlines()
    # Current read index
    ci = 0
    D, I, S, V, F = list(map(int, data[ci].split()))
    ci += 1

    streets = []
    for _ in range(S):
        # each entry has b, e, l
        street = data[ci].split()
        street[0] = int(street[0])
        street[1] = int(street[1])
        street[3] = int(street[3])
        streets.append(street)
        ci += 1

    paths = []
    for _ in range(V):
        path = data[ci].split()
        path[0] = int(path[0])
        paths.append(path)
        ci += 1
    return ((D, I, F), streets, paths)

constants, streets, paths = parseData('a.txt')
D, I, F = constants

print(D, I, F, streets, paths)

roads = []
cars = []
intersections = []

for s in range(len(streets)):
    roads.append(road((streets[s][0], streets[s][1]), streets[s][2], streets[s][3]))

for p in range(len(paths)):
    cars.append(car(paths[0][1:]))

for i in range(I):
    intersections.append(intersection(I, roads))
    
