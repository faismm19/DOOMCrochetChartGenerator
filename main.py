from PIL import Image, ImageDraw

# Set the size of the image and the size of each box in the grid
width, height = 16, 5098
box_size = 10

# Open the input file and read the contents
with open('binary.txt', 'r') as f:
    file_contents = f.read().replace(' ', '')

# Create a new image and drawing object
image = Image.new('RGB', ((width + 1) * box_size, (height + 1) * box_size), color='white')
draw = ImageDraw.Draw(image)

# Draw row numbers
for i in range(height):
    draw.text((0, (i + 0.5) * box_size), str(i), fill='black')

# Draw column numbers
for j in range(width):
    draw.text(((j + 0.5) * box_size, 0), str(j), fill='black')

# Iterate over the file contents and draw the grid
for i, char in enumerate(file_contents):
    # Calculate the x and y coordinates of the current box
    x = ((i % width) + 1) * box_size
    y = ((i // width) + 1) * box_size

    # Set the fill color based on the character
    fill = 'black' if char == '1' else 'white'

    # Draw the box and grid lines
    draw.rectangle((x, y, x + box_size, y + box_size), fill=fill)
    draw.line((x, box_size, x, (height + 1) * box_size), fill='gray')
    draw.line((box_size, y, (width + 1) * box_size, y), fill='gray')

# Save the image
image.save('output.png')
