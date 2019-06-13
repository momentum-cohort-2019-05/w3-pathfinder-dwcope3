# import PIL

file = "elevation_small.txt"

with open(file) as f:
    elevations = f.read().split()

# print(elevations)
print(max(elevations))
print(min(elevations))
max = 5648
min = 3139
