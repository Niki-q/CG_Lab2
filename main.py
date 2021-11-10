from PIL import Image, ImageColor
from PIL import ImageDraw

width = 540
height = 960

image = Image.new("RGB", (width, height))

draw = ImageDraw.Draw(image)

f = open('DS9.txt')
for line in f:
    point_cord = line.split(" ")
    x = int(point_cord[0])
    y = int(point_cord[1])
    draw.point((x, y), fill=ImageColor.getrgb("red"))

image.save("empty.png", "PNG")