from PIL import Image

uncompressed_image_path = "high_P1030652.png"
compresseed_image_path = "compressed_higher_P1030652.jpg"

# compressed image pixel size
compareSize = 1024

quality = 90
optimizeJpeg = True

# Open the image file
with Image.open(uncompressed_image_path) as img:
    # Get the image size
    width, height = img.size

    # Check if the image is larger than the desired size
    if width > 1024 or height > 1024:
        # Resize the image while preserving aspect ratio
        img.thumbnail((1024, 1024))
    else:
        img.thumbnail((width, height))
        # Save the compressed image
    if not img.mode == 'RGB':
        img = img.convert('RGB')

    img.save(compresseed_image_path, optimize=optimizeJpeg, quality=quality)