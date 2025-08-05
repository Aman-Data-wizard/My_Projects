from PIL import Image
import os

# Settings
image_folder = 'D:\Python\Advance Python\images'  # raw string for Windows path
collage_name = 'my_collage.jpg'
cols = 3  # number of columns
padding = 10  # padding between images

# Collect images
image_files = [os.path.join(image_folder, img) for img in os.listdir(image_folder)
               if img.lower().endswith(('jpg', 'jpeg', 'png'))]

# Open images and resize with preserved aspect ratio
images = []
max_width = 0
max_height = 0

for img_path in image_files:
    img = Image.open(img_path)
    img.thumbnail((400, 400))  # Higher quality thumbnail
    images.append(img)
    if img.width > max_width:
        max_width = img.width
    if img.height > max_height:
        max_height = img.height

# Calculate rows
rows = (len(images) + cols - 1) // cols

# Create collage canvas
collage_width = cols * max_width + (cols - 1) * padding
collage_height = rows * max_height + (rows - 1) * padding
collage = Image.new('RGB', (collage_width, collage_height), color='white')

# Paste images into collage
x = 0
y = 0
for i, img in enumerate(images):
    collage.paste(img, (x, y))
    x += max_width + padding
    if (i + 1) % cols == 0:
        x = 0
        y += max_height + padding

# Save collage
collage.save(collage_name)
print(f"Collage saved as {collage_name}")
