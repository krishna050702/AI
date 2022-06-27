#taking values from text file
graph="D:\\4th sem\\AI\\PA\\graph"
heuristics="D:\\4th sem\AI\\PA\\heuristics"

hs = {}
cityIndex = {}
indexCity = []
n = 0 # number of cities
with open(heuristics,"r") as f:
  for line in f:
    temp = line.split(",")
    hs[temp[0].strip()] = int(temp[1].strip())
    cityIndex[temp[0].strip()] = n
    indexCity.append(temp[0].strip())
    n += 1
print(hs)
print(cityIndex)
print(indexCity)