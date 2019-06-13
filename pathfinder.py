# import PIL

file = "elevation_small.txt"

with open(file) as f:
    coordinates = f.read().split()

# print(coordinates)
print(max(coordinates))
print(min(coordinates))
max = 5648
min = 3139
