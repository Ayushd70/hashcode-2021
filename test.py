from classes import car


def parseData(inputFile):
    """
    Returns a tuple:
    ((D, I, F), streets, paths)
    """

    # Read lines
    with open(inputFile, "r") as f:
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


constants, streets, paths = parseData("a.txt")
D, I, F = constants

print(D, I, F, streets, paths)

c1 = car(paths[0], streets)
c2 = car(paths[1], streets)