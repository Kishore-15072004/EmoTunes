import base64

# Path to the image file
image_path = 'tests/test_image.jpg'

# Load the image file and encode it to base64
with open(image_path, 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# Ensure correct padding
encoded_string += '=' * ((4 - len(encoded_string) % 4) % 4)

# Save the base64 string to a text file
with open('tests/test_image_base64.txt', 'w') as text_file:
    text_file.write(encoded_string)

print("Image successfully converted to base64 and saved.")
