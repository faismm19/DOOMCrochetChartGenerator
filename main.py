# Binary text visualizer, 2023
# Created by Mackenzie Faison

from PIL import Image, ImageDraw

width, height = 8, 34
box_size = 10

with open('binary.txt', 'r') as f:
    file_contents = f.read().replace(' ', '').replace('\n', '')

image = Image.new('RGB', ((width + 1) * box_size, (height + 1) * box_size), color='white')
draw = ImageDraw.Draw(image)

for i in range(height):
    draw.text((0, (i + 0.5) * box_size), str(i), fill='black')


for j in range(width):
    draw.text(((j + 0.5) * box_size, 0), str(j), fill='black')


for i, char in enumerate(file_contents):
    x = ((i % width) + 1) * box_size
    y = ((i // width) + 1) * box_size

fill = 'black' if char == '1' else 'white'
draw.rectangle((x, y, x + box_size, y + box_size), fill=fill)
draw.line((x, box_size, x, (height + 1) * box_size), fill='gray')
draw.line((box_size, y, (width + 1) * box_size, y), fill='gray')

image.save('output.png')
