from PIL import Image, ImageColor
from PIL import ImageDraw

width = 540
height = 960
# Встановлює розміри вікна (полотна – canvas size) 540х960 пкс;
image = Image.new("RGB", (width, height))

draw = ImageDraw.Draw(image)

f = open('DS3.txt')
# Зчитує датасет з файлу;
for line in f:
    point_cord = line.split(" ")
    x = int(point_cord[0])
    y = int(point_cord[1])
    draw.point((x, y), fill=ImageColor.getrgb("red"))
    # Відображає точки за заданими координатами

image.save("empty.png", "PNG")
# Виводить результат в будь-який графічний формат.
