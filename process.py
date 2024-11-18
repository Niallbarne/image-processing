from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def process_image(input_image_path, output_image_path, width, height):
    """
    Resize the image to the given width and height, and save it.

    Args:
        input_image_path (str): The path to the input image that needs to be resized.
        output_image_path (str): The path where the resized image will be saved.
        width (int): The target width to which the image will be resized.
        height (int): The target height to which the image will be resized.

    Returns:
        str: The path to the resized image that was saved.
    """
    # Open the image using Pillow
    image = Image.open(input_image_path)

    # Resize the image to the specified dimensions
    resized_image = image.resize((width, height))

    # Save the resized image to the output path
    resized_image.save(output_image_path)
    
    # Return the path to the resized image
    return output_image_path

def apply_colormap(input_image_path, output_image_path):
    """
    Apply a colormap to the image.

    Args:
        input_image_path (str): The path to the input image to which the colormap will be applied.
        output_image_path (str): The path where the colormap-applied image will be saved.

    Returns:
        str: The path to the image with the applied colormap.
    """
    # Open the image
    image = Image.open(input_image_path)
    
    # Convert the image to grayscale (if it isn't already)
    grayscale_image = image.convert("L")
    
    # Convert the image to a NumPy array (2D array)
    image_array = np.array(grayscale_image)
    
    # Apply a colormap using matplotlib (using 'jet' as an example)
    colormap_image = plt.get_cmap("jet")(image_array)  # Apply the colormap (e.g., 'jet')
    
    # Normalize the colormap image to [0, 255]
    colormap_image = (colormap_image[:, :, :3] * 255).astype(np.uint8)  # Use RGB channels, normalize to 0-255
    
    # Convert the colormap image back to a PIL Image (RGB format)
    colormap_image = Image.fromarray(colormap_image)
    
    # Save the colormap image
    colormap_image.save(output_image_path)
    
    # Return the path to the colormap image
    return output_image_path
