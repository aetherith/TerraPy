import noise
import numpy as np
from PIL import Image
from time import sleep
import copy

def generate_perlin_map(xsize, ysize, scale=100.0, octaves=6, persistence=0.5, lacunarity= 2.0):
    perlin_map = np.zeros((xsize, ysize))
    for i in range(xsize):
        for j in range(ysize):
            perlin_map[i][j] = noise.pnoise2(
                i / scale,
                j / scale,
                octaves=octaves,
                persistence=persistence,
                lacunarity=lacunarity,
                repeatx=xsize,
                repeaty=ysize,
                base=0
            )
    return perlin_map

def image_array_conversion(array):
    array = (array * 255).astype('uint8')
    array = np.clip(array, 0, 255)
    return array

xsize = 512
ysize = 512
base_world = generate_perlin_map(xsize, ysize)
world = copy.deepcopy(base_world)
image = Image.fromarray(world)
image.show()
sleep(10)
perlin_overlay_passes = 4
for p in np.random.binomial(n=1, p=0.5, size=perlin_overlay_passes):
    overlay = generate_perlin_map(xsize, ysize)
    if p:
        world = np.add(world, overlay)
    else:
        world = np.subtract(world, overlay)
    image = Image.fromarray(image_array_conversion(world))
    image.show()
    sleep(10)