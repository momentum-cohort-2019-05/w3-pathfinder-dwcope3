from PIL import Image

class ElevationMap:
    def __init__(self, elevations):
        self.elevations = elevations

    def elevation_at_coordinate(self, x, y):
        return self.elevations[y][x]

    def min_elevation(self):
        return min([min(row) for row in self.elevations])

    def max_elevation(self):
        return max([max(row) for row in self.elevations])

    def intensity_at_coordinate(self, x, y, min_elevation, max_elevation):
        elevation = self.elevation_at_coordinate(x, y)

        return ((elevation - min_elevation) / (max_elevation - min_elevation)) * 255

    def draw_grayscale_gradient(self, filename, width, height):
        image = Image.new(mode='L', size=(width, height))
        min_elevation = self.min_elevation()
        max_elevation = self.max_elevation()
        for x in range (width):
            for y in range (height):
                intensity = int(self.intensity_at_coordinate(x,y,min_elevation, max_elevation))
                image.putpixel((x, y), (intensity))
        image.save(filename)
